import os
import sys
import shlex
import subprocess
import threading
import progressbar
import queue
from string import Template
from django.core.management.base import CommandError
from django.core import management
from django.conf import settings
from django_webpack_dev_server.management import constants
import requests


class Generator():
    app_name = None
    frontend_library_or_framework = None

    def __init__(self, app_name, frontend_library_or_framework):
        self.app_name = app_name
        self.frontend_library_or_framework = frontend_library_or_framework

    # validate the app_name provided by the user
    def validate_appname(self):

        if not self.app_name.isalnum():
            raise CommandError('App Name should be alphanumeric only')

    # check if system has node and npm installed
    def check_system_requirements(self):

        command_for_node = 'node -v'
        command_for_npm = 'npm -v'

        # checks whether npm is installed by getting node version
        subprocess_node_command = subprocess.run(
            shlex.split(command_for_node), capture_output=True)

        # Shell = True is required for windows based operating system only
        shell_parameter = sys.platform == constants.WINDOWS_OS_IDENTIFIER

        # checks whether npm is installed by getting npm version
        subprocess_npm_command = subprocess.run(shlex.split(
            command_for_npm), capture_output=True, shell=shell_parameter)

        # if either of the commands fail then raise error
        if subprocess_node_command.returncode != 0 or subprocess_npm_command.returncode != 0:
            raise CommandError(
                'Seems like node or npm is not available in your system')

    # checks if django settings file is configured properly
    def check_django_settings(self):
        if len(settings.STATICFILES_DIRS) == 0:
            raise CommandError(
                'STATICFILES_DIR attribute is missing in the django settings file')

    # create templates directory and static directory inside the django app
    def create_required_directories(self):

        static_directory_path, static_directory_name = os.path.split(
            settings.STATICFILES_DIRS[0])

        templates_directory_path = os.path.join(
            os.getcwd(), self.app_name, constants.TEMPLATES, self.app_name)

        static_directory_path = os.path.join(
            os.getcwd(), self.app_name, static_directory_name, self.app_name)

        src_directory_path = os.path.join(
            os.getcwd(), self.app_name, constants.SRC)

        try:
            os.makedirs(templates_directory_path)
            os.makedirs(static_directory_path)
            os.makedirs(src_directory_path)

        except OSError as error:
            raise CommandError(error)

    # Download Files and replace app_name parameter
    def download_template_files(self):

        template_files = constants.TEMPLATE_FILES_DICT.get(
            self.frontend_library_or_framework)

        substitute_parameters = {
            'app_name': self.app_name
        }

        text_document_content_type = 'text/plain; charset=utf-8'

        for directory_type, filename, download_url in template_files:
            target_filepath = os.getcwd()

            if directory_type == constants.APP:
                target_filepath = os.path.join(target_filepath, self.app_name)

            elif directory_type == constants.SRC:
                target_filepath = os.path.join(
                    target_filepath, self.app_name, constants.SRC)

            elif directory_type == constants.TEMPLATES:
                target_filepath = os.path.join(
                    target_filepath, self.app_name, constants.TEMPLATES, self.app_name)

            target_filepath = os.path.join(target_filepath, filename)

            download_file = requests.get(download_url, stream=True)

            with open(target_filepath, 'wb') as target_file:

                try:
                    target_file.write(download_file.content)

                except OSError as error:
                    raise CommandError(error)

            if download_file.headers['Content-Type'] != text_document_content_type:
                continue

            with open(target_filepath, 'r') as target_file:
                source_file = Template(target_file.read())
                modified_file_contents = source_file.substitute(
                    substitute_parameters)

            with open(target_filepath, 'w') as target_file:

                try:
                    target_file.write(modified_file_contents)

                except OSError as error:
                    raise CommandError(error)

    def install_dependencies(self, thread_queue):
        os.chdir(self.app_name)

        command_for_npm_install = 'npm install'

        command = subprocess.Popen(
            shlex.split(command_for_npm_install), shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        while True:
            realtime_output = command.stdout.readline()

            if realtime_output == '' or command.poll() is not None:
                break
            elif realtime_output:
                print(realtime_output.strip().decode())
                sys.stdout.flush()

        os.chdir('../')
        thread_queue.put(command.returncode)

    def install_dependencies_and_show_progress_bar(self):

        widgets = [
            'Installing Node Dependencies ',
            progressbar.AnimatedMarker()
        ]

        bar = progressbar.ProgressBar(
            widgets=widgets, maxval=progressbar.UnknownLength, redirect_stdout=True)
        bar.start()

        thread_queue = queue.Queue()
        count = 0

        thread1 = threading.Thread(target=self.install_dependencies, args=[
            thread_queue], name='thread1')
        thread1.start()

        while thread1.is_alive():
            count += 1
            bar.update(count)

        status = thread_queue.get()

        if status != 0:
            raise CommandError(
                'There were some errors while installing dependencies')

    # generate a django app with the selected frontend framework or library
    def generate(self):
        self.validate_appname()
        self.check_system_requirements()
        self.check_django_settings()
        management.call_command('startapp', self.app_name)
        self.create_required_directories()
        self.download_template_files()
        self.install_dependencies_and_show_progress_bar()
