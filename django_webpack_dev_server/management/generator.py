# necessary imports
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


# Base Class to create a django app with frontend configuration
class Generator():
    # app_name is the name of the django app
    app_name = None

    # frontend_library_or_framework denotes the frontend framework or library requested
    frontend_library_or_framework = None

    # shell_parameter = True for windows based system
    # shell_parameter = False for non windows based system
    shell_parameter = None

    # set values of app_name, frontend_library_or_framework in the constructor
    def __init__(self, app_name, frontend_library_or_framework):
        self.app_name = app_name
        self.frontend_library_or_framework = frontend_library_or_framework
        self.shell_parameter = sys.platform == constants.WINDOWS_OS_IDENTIFIER

    # validate the app_name provided by the user
    def validate_appname(self):

        # if appname contains non alphanumeric characters then raise error
        if not self.app_name.isalnum():
            raise CommandError('App Name should be alphanumeric only')

    # check if system has node and npm installed
    def check_system_requirements(self):

        # command to check node in system
        command_for_node = 'node -v'

        # command to check npm in system
        command_for_npm = 'npm -v'

        # checks whether node is installed by getting node version
        subprocess_node_command = subprocess.run(
            shlex.split(command_for_node), capture_output=True)

        # checks whether npm is installed by getting npm version
        subprocess_npm_command = subprocess.run(shlex.split(
            command_for_npm), capture_output=True, shell=self.shell_parameter)

        # if either of the commands fail then raise an error
        if subprocess_node_command.returncode != 0 or subprocess_npm_command.returncode != 0:
            raise CommandError(
                'Seems like node or npm is not available in your system')

    # checks if django settings file is configured properly
    def check_django_settings(self):
        # if STATICFILES_DIRS value is missing then raise erorr and inform the user
        if len(settings.STATICFILES_DIRS) == 0:
            raise CommandError(
                'STATICFILES_DIRS attribute is missing in the django settings file')

    # creates templates directory and static directory inside the django app
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

    # Download Files and replace the parameters
    def download_template_files(self):

        template_files = constants.TEMPLATE_FILES_DICT.get(
            self.frontend_library_or_framework)

        # replace the parameters with appropriate values
        substitute_parameters = {
            'app_name': self.app_name
        }
        
        # content-type required for plain text files
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


            # Download the file from the Git Repository
            download_file = requests.get(download_url, stream=True)

            # write the contents of the file in the appropriate location
            with open(target_filepath, 'wb') as target_file:

                try:
                    target_file.write(download_file.content)

                except OSError as error:
                    raise CommandError(error)

            # if file is media file like image then no need for templating so skip them
            if download_file.headers['Content-Type'] != text_document_content_type:
                continue

            # open the text files and perform templating to replace the necessary parameters
            with open(target_filepath, 'r') as target_file:
                source_file = Template(target_file.read())
                modified_file_contents = source_file.substitute(
                    substitute_parameters)

            # write the updated file in the appropriate location
            with open(target_filepath, 'w') as target_file:

                try:
                    target_file.write(modified_file_contents)

                except OSError as error:
                    raise CommandError(error)

    # method to install the dependencies by running npm install command 
    def install_dependencies(self, thread_queue):
        os.chdir(self.app_name)

        # command to install node dependencies
        command_for_npm_install = 'npm install'

        # execute the npm install command for installing dependencies
        command = subprocess.Popen(
            shlex.split(command_for_npm_install), shell=self.shell_parameter, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        # get any data genrated by the command and display it on stdout
        while True:

            # read output lines one line at a time
            realtime_output = command.stdout.readline()

            # if output line is empty then terminate the loop
            if realtime_output == '' or command.poll() is not None:
                break
            elif realtime_output:
                print(realtime_output.strip().decode())
                sys.stdout.flush()

        os.chdir('../')
        # return the status of the installation command into the main thread
        thread_queue.put(command.returncode)

    # install the necessary dependencies and display a progress bar until it executes
    def install_dependencies_and_show_progress_bar(self):

        widgets = [
            'Installing Node Dependencies ',
            progressbar.AnimatedMarker()
        ]

        bar = progressbar.ProgressBar(
            widgets=widgets, maxval=progressbar.UnknownLength, redirect_stdout=True)
        bar.start()

        # thread_queue is used to fetch the output of the function executed in the other thread
        thread_queue = queue.Queue()
        count = 0

        # create a thread which will execute the npm install command
        thread1 = threading.Thread(target=self.install_dependencies, args=[
            thread_queue], name='thread1')

        # start the installation command by starting the thread
        thread1.start()

        # display the progress until the other thread is alive
        while thread1.is_alive():
            count += 1
            bar.update(count)

        # fetching status code of the command executed in other thread
        status = thread_queue.get()

        # if command failed then inform the user
        if status != 0:
            raise CommandError(
                'There were some errors while installing dependencies')

    # generate a django app with the selected frontend library or framework
    # Driver method which will execute the other methods
    def generate(self):
        self.validate_appname()
        self.check_system_requirements()
        self.check_django_settings()
        management.call_command('startapp', self.app_name)
        self.create_required_directories()
        self.download_template_files()
        self.install_dependencies_and_show_progress_bar()
