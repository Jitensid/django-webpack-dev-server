# necessary imports
import os
import queue
import shlex
import shutil
import subprocess
import sys
import threading
from string import Template

import progressbar
import requests
from django.core import management
from django.core.management.base import CommandError

# import the constants module
from django_webpack_dev_server.management import constants
from dotenv import load_dotenv

# load the environment variables
load_dotenv()


class Generator:
    """
    Base Class to create a django app with the necessary frontend configuration
    """

    # set the values of app_name, frontend_library_or_framework in the constructor
    def __init__(self, app_name, frontend_library_or_framework):
        """
        Constructor to set up the app_name and frontend_library_or_framework variables of the class
        :param app_name str: Name of the django app with frontend configuration
        :param frontend_library_or_framework str: Denotes the configuration to setup in the django app.
        """

        # app_name is the name of the django app which will have the frontend configuration
        self.app_name = app_name

        # frontend_library_or_framework denotes the frontend framework or library requested from the command line
        self.frontend_library_or_framework = frontend_library_or_framework

        # static_directory_name is the name of the the static directory inside the django app
        self.static_directory_name = "static"

        # set the shell_parameter according to the operating system of the user
        # shell_parameter = True for windows based system
        # shell_parameter = False for non windows based system
        self.shell_parameter = sys.platform == constants.WINDOWS_OS_IDENTIFIER

    def validate_appname(self):
        """
        Validates the app name of the django app provided by the user via commandline
        """
        # if appname contains non alphanumeric characters then raise error and inform the user
        if not self.app_name.isalnum():
            raise CommandError(
                constants.COMMAND_ERROR_MESSAGES_DICT["INVALID_APP_NAME_ERROR_MESSAGE"]
            )

    def check_system_requirements(self):
        """
        Checks if system has node and npm installed with the help of the
        subprocess module
        """
        # command to check node in system
        command_for_node = "node -v"

        # command to check npm in system
        command_for_npm = "npm -v"

        # checks whether node is installed by getting node version
        subprocess_node_command = subprocess.run(
            shlex.split(command_for_node),
            capture_output=True,
            shell=self.shell_parameter,
        )

        # checks whether npm is installed by getting npm version
        subprocess_npm_command = subprocess.run(
            shlex.split(command_for_npm),
            capture_output=True,
            shell=self.shell_parameter,
        )

        # if either of the commands fail then raise an error and inform the user
        if (
            subprocess_node_command.returncode != 0
            or subprocess_npm_command.returncode != 0
        ):
            raise CommandError(
                constants.COMMAND_ERROR_MESSAGES_DICT["SYSTEM_ERROR_MESSAGE"]
            )

    def create_required_directories(self):
        """
        Creates templates directory and static directory inside the django
        app which will have the frontend configuration
        """

        # create the path for the templates directory
        templates_directory_path = os.path.join(
            os.getcwd(),
            self.app_name,
            constants.TEMPLATES_DIRECTORY_NAME,
            self.app_name,
        )

        # create the path for the static directory
        static_directory_path = os.path.join(
            os.getcwd(), self.app_name, self.static_directory_name, self.app_name
        )

        # create the path for the src directory
        src_directory_path = os.path.join(
            os.getcwd(), self.app_name, constants.SRC_DIRECTORY_NAME
        )

        # create the necessary directories inside the newly created django app
        try:
            os.makedirs(templates_directory_path)
            os.makedirs(static_directory_path)
            os.makedirs(src_directory_path)

        except OSError as error:
            raise CommandError(error)

    def check_if_file_is_text_document(self, filename):
        """
        Check whether file is of form textdocument or an media file with the help of file extension
        :param filename str: name of the file to check
        :return is_text_document bool: Whether the file is text document or a media file
        """

        is_text_document = True

        # get the extension of the file from the filename
        _, file_extension = os.path.splitext(filename)

        # list of non text document file extensions
        non_text_document_file_extensions = [".png"]

        # if the file extension is in the extensions list then return False
        if file_extension in non_text_document_file_extensions:
            return not is_text_document

        # return the boolean value
        return is_text_document

    def get_target_path_of_template_file(self, filename, directory_type):
        """
        Finds the path where the file will be placed after modifications
        :param filename str: name of the file to get the path
        :param directory_type str: name of the directory where file will be stored
        :return target_filepath str: final filepath of the file after it is substituted with the parameters
        """

        # initialize the target_filepath as the current working directory
        target_filepath = os.getcwd()

        # append the specific path as per the directory in which the file would be stored
        if directory_type == constants.APP_DIRECTORY_NAME:
            target_filepath = os.path.join(target_filepath, self.app_name)

        elif directory_type == constants.SRC_DIRECTORY_NAME:
            target_filepath = os.path.join(
                target_filepath, self.app_name, constants.SRC_DIRECTORY_NAME
            )

        elif directory_type == constants.TEMPLATES_DIRECTORY_NAME:
            target_filepath = os.path.join(
                target_filepath,
                self.app_name,
                constants.TEMPLATES_DIRECTORY_NAME,
                self.app_name,
            )

        # append the filename into the target_filepath
        target_filepath = os.path.join(target_filepath, filename)

        # return the target_filepath
        return target_filepath

    def download_template_files(self):
        """
        Download template files from the Git Repository and substitute the
        necessary parameters
        """

        # get all template files as per the requirement
        template_files = constants.PROD_TEMPLATE_FILES_DICT.get(
            self.frontend_library_or_framework
        )

        # replace the parameters with appropriate values
        substitute_parameters = {"app_name": self.app_name}

        # iterate all the tempate filenames
        for directory_type, filename, download_url in template_files:

            # get the path where the file will be stored
            target_filepath = self.get_target_path_of_template_file(
                filename, directory_type
            )

            # Download the files from the Git Repository
            download_file = requests.get(download_url, stream=True)

            # write the contents of the file in the appropriate location
            with open(target_filepath, "wb") as target_file:

                try:
                    target_file.write(download_file.content)

                except OSError as error:
                    raise CommandError(error)

            # if file is not a type of text document then do not perform
            # string templating for it
            if not self.check_if_file_is_text_document(filename):
                continue

            # open the file and perform templating to replace the necessary parameters
            with open(target_filepath, "r") as target_file:
                # read the file contents and substitute the parameters
                source_file = Template(target_file.read())
                modified_file_contents = source_file.substitute(substitute_parameters)

            # write the updated file in the appropriate location
            with open(target_filepath, "w") as target_file:

                try:
                    target_file.write(modified_file_contents)

                except OSError as error:
                    raise CommandError(error)

    def load_assets_from_local(self):
        """
        A development only method executed when SOFTWARE_ENVIRONMENT_MODE == development
        It loads the assets files from local system instead of downloading from the
        Git Repository
        """

        # get all template files as per the requirement
        template_files = constants.DEVELOPMENT_TEMPLATE_FILES_DICT.get(
            self.frontend_library_or_framework
        )

        # replace the parameters with appropriate values
        substitute_parameters = {"app_name": self.app_name}

        # iterate all the tempate filenames
        for directory_type, filename, local_asset_file_path in template_files:

            # get the path where the file will be stored
            target_filepath = self.get_target_path_of_template_file(
                filename, directory_type
            )

            # copy the template file from the local assets directory to the target path
            shutil.copy(local_asset_file_path, target_filepath)

            # if file is not a type of text document then do not template that file
            if not self.check_if_file_is_text_document(filename):
                continue

            # open the files and perform templating to replace the necessary parameters
            with open(target_filepath, "r") as target_file:
                source_file = Template(target_file.read())
                modified_file_contents = source_file.substitute(substitute_parameters)

            # write the updated file in the appropriate location
            with open(target_filepath, "w") as target_file:

                try:
                    target_file.write(modified_file_contents)

                except OSError as error:
                    raise CommandError(error)

    def install_dependencies(self, thread_queue):
        """
        Installs the node dependencies by executing npm install command
        :param thread_queue Queue: Queue which will pass the status of the command
        to main thread
        """
        # set the current working directory to the newly created django app
        os.chdir(self.app_name)

        # command to install node dependencies
        command_for_npm_install = "npm install"

        # execute the npm install command for installing dependencies
        command = subprocess.Popen(
            shlex.split(command_for_npm_install),
            shell=self.shell_parameter,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )

        # get any data genrated by the command and display it on stdout
        while True:

            # read output lines one line at a time
            realtime_output = command.stdout.readline()

            # if output line is empty then terminate the loop
            if realtime_output == "" or command.poll() is not None:
                break
            elif realtime_output:
                # display messages in stdout
                print(realtime_output.strip().decode())
                sys.stdout.flush()

        # set the working directory to the original value
        os.chdir("../")
        # return the status of the installation command into the main thread
        thread_queue.put(command.returncode)

    def install_dependencies_and_show_progress_bar(self):
        """
        Install the necessary node dependencies and display a progress bar
        while the installation command executes
        """
        # setting the progress bar message and type
        widgets = ["Installing Node Dependencies ", progressbar.AnimatedMarker()]

        # create an indefinite progressbar because time for installing dependencies is not equal for all users
        bar = progressbar.ProgressBar(
            widgets=widgets, max_value=progressbar.UnknownLength, redirect_stdout=True
        )
        bar.start()

        # thread_queue is used to fetch the output of the function executed in the other thread
        thread_queue = queue.Queue()
        count = 0

        # create a thread which will execute the npm install command
        thread1 = threading.Thread(
            target=self.install_dependencies, args=[thread_queue], name="thread1"
        )

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
                constants.COMMAND_ERROR_MESSAGES_DICT["NPM_INSTALLATION_ERROR_MESSAGE"]
            )

    def generate(self):
        """
        Generates a django app with the selected frontend library or framework
        Driver method which will execute the other methods
        """
        self.validate_appname()
        self.check_system_requirements()
        management.call_command("startapp", self.app_name)
        self.create_required_directories()

        # In development mode the assets will be loaded from the local system
        if os.environ.get("SOFTWARE_ENVIRONMENT_MODE") == "development":
            print("Loading the Assets Locally")
            self.load_assets_from_local()

        # In production mode the assets will be downloaded from the Git Repository
        else:
            self.download_template_files()

        self.install_dependencies_and_show_progress_bar()
