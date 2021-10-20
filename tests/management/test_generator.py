import io
import os
import queue
from unittest import mock

import pytest
from django.core.management.base import CommandError
from django_webpack_dev_server.management import constants
from django_webpack_dev_server.management.generator import Generator


# A pytest fixture used to create a Generator object
@pytest.fixture
def app_generator():

    # Create the Generator object
    app_generator = Generator(
        app_name="frontend", frontend_library_or_framework="react_javascript"
    )

    # return the Generator object to the test
    return app_generator


class TestGeneratorClass:
    """
    Test Class for testing the Generator Class defined in generator.py
    """

    def test_validate_app_name(self):
        """
        Function to test the validate_app_name method of the Generator Class
        """

        # Create the Generator object and pass an invalid app_name to test
        app_generator = Generator(
            app_name="frontend@@@", frontend_library_or_framework="react_javascript"
        )

        # Check if CommandError is raised when the method is called with invalid app_name
        with pytest.raises(CommandError) as CommandErrorException:
            app_generator.validate_appname()

        # assert the message of the exception
        assert (
            str(CommandErrorException.value)
            == constants.COMMAND_ERROR_MESSAGES_DICT["INVALID_APP_NAME_ERROR_MESSAGE"]
        )

    @mock.patch("subprocess.run")
    def test_check_system_requirements(self, mocked_subprocess_run, app_generator):
        """
        Function to test the check_system_requirements method of the Generator Class
        """

        # mock the subprocess run method and set response to 0
        # Response 0 means that the command ran successfully
        mocked_subprocess_run.return_value.returncode = 0

        # call the method to test
        app_generator.check_system_requirements()

        # assert that the subprocess run method was called 2 times
        assert mocked_subprocess_run.call_count == 2

        # Reset the mock
        mocked_subprocess_run.reset_mock()

        # mock the subprocess run method and set response to 1
        # Response 1 means that the command did not ran successfully
        mocked_subprocess_run.return_value.returncode = 1

        # Check if CommandError is raised when the method is called
        with pytest.raises(CommandError) as CommandErrorException:
            # call the method to test
            app_generator.check_system_requirements()

        # assert the message of the exception
        assert (
            str(CommandErrorException.value)
            == constants.COMMAND_ERROR_MESSAGES_DICT["SYSTEM_ERROR_MESSAGE"]
        )

        # assert that the subprocess run method was called 2 times
        assert mocked_subprocess_run.call_count == 2

    @mock.patch("os.makedirs")
    def test_create_required_directories(self, mocked_os_makedirs, app_generator):
        """
        Function to test the create_required_directories method of the Generator Class
        """

        # call the method to test
        app_generator.create_required_directories()

        # assert that the os makedirs method is called 3 times
        assert mocked_os_makedirs.call_count == 3

        # reset the mock
        mocked_os_makedirs.reset_mock()

        # Check if CommandError is raised when the method is called
        with pytest.raises(CommandError) as CommandErrorException:
            exception_message = "Error while creating directories"

            # Raise OSError when the os makedirs method is called to
            mocked_os_makedirs.side_effect = OSError(exception_message)

            # call the method to test
            app_generator.create_required_directories()

        # assert that the os makedirs method is called 1 time
        assert mocked_os_makedirs.call_count == 1

        # assert the message of the exception
        assert str(CommandErrorException.value) == exception_message

    def test_check_if_file_is_text_document(self, app_generator):
        """
        Function to test the check_if_file_is_text_document method of the Generator Class
        """

        # file of type text document
        text_document_filename = "generator.py"

        # file of type non text document
        non_text_document_filename = "reactlogo.png"

        # assert True if file is of text document type
        assert (
            # call the method to test
            app_generator.check_if_file_is_text_document(text_document_filename)
            == True
        )

        # assert False if file is not of text document type
        assert (
            # call the method to test
            app_generator.check_if_file_is_text_document(non_text_document_filename)
            == False
        )

    def test_get_target_path_of_template_file(self, app_generator):
        """
        Function to test the get_target_path_of_template_file method of the Generator Class
        """
        filename = "webpack.config.js-tpl"

        # create the path for a while that will be stored under APP directory
        target_app_directory_filepath = os.path.join(
            os.getcwd(), app_generator.app_name
        )

        # create the path for a while that will be stored under src directory
        target_src_directory_filepath = os.path.join(
            os.getcwd(), app_generator.app_name, constants.SRC_DIRECTORY_NAME
        )

        # create the path for a while that will be stored under templates directory
        target_templates_directory_filepath = os.path.join(
            os.getcwd(),
            app_generator.app_name,
            constants.TEMPLATES_DIRECTORY_NAME,
            app_generator.app_name,
        )

        # create the final path for a particular file
        target_filepath = os.path.join(target_app_directory_filepath, filename)

        # assert the file path created and returned by the class method
        assert (
            # call the method to test
            app_generator.get_target_path_of_template_file(
                filename, constants.APP_DIRECTORY_NAME
            )
            == target_filepath
        )

        # create the final path for a particular file
        target_filepath = os.path.join(target_src_directory_filepath, filename)

        # assert the file path created and returned by the class method
        assert (
            # call the method to test
            app_generator.get_target_path_of_template_file(
                filename, constants.SRC_DIRECTORY_NAME
            )
            == target_filepath
        )

        # create the final path for a particular file
        target_filepath = os.path.join(target_templates_directory_filepath, filename)

        # assert the file path created and returned by the class method
        assert (
            # call the method to test
            app_generator.get_target_path_of_template_file(
                filename, constants.TEMPLATES_DIRECTORY_NAME
            )
            == target_filepath
        )

    @mock.patch("requests.get")
    @mock.patch("builtins.open", new_callable=mock.mock_open, read_data="My data")
    def test_download_template_files(
        self, mocked_builtins_open, mocked_requests_get, app_generator
    ):
        """
        Function to test the download_template_files method of the Generator Class
        """

        # call the method to test
        app_generator.download_template_files()

        # assert the number of times the file open is called
        assert mocked_builtins_open.call_count == 29

        # assert the number of times the get request is made
        assert mocked_requests_get.call_count == 11

        # reset the mocks
        mocked_builtins_open.reset_mock()
        mocked_requests_get.reset_mock()

        # Check if CommandError is raised when the method is called
        with pytest.raises(CommandError) as CommandErrorException:

            exception_message = "Error while writing in the file"

            # Raise OSError during the file write operation
            mocked_builtins_open.return_value.write.side_effect = OSError(
                exception_message
            )

            # call the method to test
            app_generator.download_template_files()

        # assert the message of the exception
        assert str(CommandErrorException.value) == exception_message

        mocked_builtins_open.reset_mock()
        mocked_requests_get.reset_mock()

        # Check if CommandError is raised when the method is called
        with pytest.raises(CommandError) as CommandErrorException:

            exception_message = "Error while writing in the file"

            # Raise OSError during the file write operation
            mocked_builtins_open.return_value.write.side_effect = [
                "No Error for 1st call",
                OSError(exception_message),
            ]

            # call the method to test
            app_generator.download_template_files()

        # assert the message of the exception
        assert str(CommandErrorException.value) == exception_message

    @mock.patch("builtins.open", new_callable=mock.mock_open, read_data="My data")
    @mock.patch("shutil.copy")
    def test_load_assets_from_local(
        self, mocked_shutil_copy, mocked_builtins_open, app_generator
    ):
        """
        Function to test the load_assets_from_local method of the Generator Class
        """

        # call the method to test
        app_generator.load_assets_from_local()

        # assert that shutil copy and open functions are called
        assert mocked_builtins_open.called == True
        assert mocked_shutil_copy.called == True

        # reset the mocks
        mocked_shutil_copy.reset_mock()
        mocked_builtins_open.reset_mock()

        # Check if CommandError is raised when the method is called
        with pytest.raises(CommandError) as CommandErrorException:
            exception_message = "Error while writing in the file"

            # Raise OSError during the file write operation
            mocked_builtins_open.return_value.write.side_effect = OSError(
                exception_message
            )

            # call the method to test
            app_generator.load_assets_from_local()

        # assert the message of the exception
        assert str(CommandErrorException.value) == exception_message
        # assert that shutil copy and open functions are called
        assert mocked_builtins_open.called == True
        assert mocked_shutil_copy.called == True

    @mock.patch("subprocess.Popen")
    @mock.patch("os.chdir")
    def test_install_dependencies(
        self,
        mocked_os_chdir,
        mocked_subprocess_popen,
        app_generator,
    ):

        """
        Function to test the test_install_dependencies method of the Generator Class
        """

        # create a queue object which is passed to a thread
        thread_queue = queue.Queue()

        # 0 means that command ran successfully
        command_return_code = 0

        # mocked the subprocess and set the returncode value to command_return_code
        mocked_subprocess_popen.return_value.returncode = command_return_code

        # mocked the subprocess and set the stdout value to some non empty output
        mocked_subprocess_popen.return_value.stdout = io.BytesIO(b"Command\nOutput")

        # mocked the subprocess and set the return value of poll method to None and then non-empty output
        mocked_subprocess_popen.return_value.poll.side_effect = [
            None,
            "Non-empty Output",
        ]

        # call the method to test
        app_generator.install_dependencies(thread_queue)

        # assert that os chdir method is called 2 times
        assert mocked_os_chdir.call_count == 2
        # assert that subprocess popen method is called 1 time
        assert mocked_subprocess_popen.call_count == 1

        # assert that the queue receives the value from subprocess Popen
        # and value equal to the command_return_code
        assert thread_queue.get() == command_return_code

    @mock.patch("queue.Queue")
    @mock.patch("threading.Thread")
    @mock.patch("progressbar.ProgressBar.update")
    def test_install_dependencies_and_show_progress_bar(
        self,
        mocked_progressbar_ProgressBar_update,
        mocked_threading_thread,
        mocked_queue_Queue,
        app_generator,
    ):

        """
        Function to test the install_dependencies_and_show_progress_bar method of the Generator Class
        """

        # different values for thread is_alive method
        thread_is_alive_values = [True, True, True, False]

        # set the mocked threading thread is_alive method with the thread_is_alive_values list
        mocked_threading_thread.return_value.is_alive.side_effect = (
            thread_is_alive_values
        )

        # set the mocked queue with the value 0
        # 0 implies installation was successful
        mocked_queue_Queue.return_value.get.return_value = 0

        # call the method to test
        app_generator.install_dependencies_and_show_progress_bar()

        # assert that the mocked threading thread was called 1 time
        assert mocked_threading_thread.call_count == 1

        # assert that the mocked progress bar was updated to the number
        # of values present in the thread_is_alive_values list
        assert mocked_progressbar_ProgressBar_update.call_count == len(
            thread_is_alive_values
        )

        # Reset the mocks
        mocked_threading_thread.reset_mock()
        mocked_queue_Queue.reset_mock()
        mocked_progressbar_ProgressBar_update.reset_mock()

        # set the mocked threading thread is_alive method with the thread_is_alive_values list
        mocked_threading_thread.return_value.is_alive.side_effect = (
            thread_is_alive_values
        )

        # set the mocked queue with the value 1
        # 1 implies installation was not successful
        mocked_queue_Queue.return_value.get.return_value = 1

        # Check if CommandError is raised when the method is called
        with pytest.raises(CommandError) as CommandErrorException:
            # call the method to test
            app_generator.install_dependencies_and_show_progress_bar()

        # assert that the mocked threading thread was called 1 time
        assert mocked_threading_thread.call_count == 1

        # assert that the mocked progress bar was updated to the number
        # of values present in the thread_is_alive_values list
        assert mocked_progressbar_ProgressBar_update.call_count == len(
            thread_is_alive_values
        )

        # assert the message of the exception
        assert (
            str(CommandErrorException.value)
            == constants.COMMAND_ERROR_MESSAGES_DICT["NPM_INSTALLATION_ERROR_MESSAGE"]
        )

    @mock.patch.object(
        Generator, "install_dependencies_and_show_progress_bar", return_value=None
    )
    @mock.patch.object(Generator, "load_assets_from_local", return_value=None)
    @mock.patch.object(Generator, "create_required_directories", return_value=None)
    @mock.patch("django.core.management.call_command")
    @mock.patch.object(Generator, "check_system_requirements", return_value=None)
    def test_generate_in_development_mode(
        self,
        mocked_generator_check_system_requirements,
        mocked_management_call_command,
        mocked_create_required_directories,
        mocked_load_assets_from_local,
        mocked_install_dependencies_and_show_progress_bar,
        app_generator,
    ):

        """
        Function to test the generate method of the Generator Class
        """

        # call the method to test
        app_generator.generate()

        # assert that all the methods of the Generator class are called
        assert mocked_generator_check_system_requirements.called == True
        assert mocked_create_required_directories.called == True
        mocked_management_call_command.assert_called_once_with(
            "startapp", app_generator.app_name
        )
        assert mocked_load_assets_from_local.called == True
        assert mocked_install_dependencies_and_show_progress_bar.called == True

    @mock.patch.object(
        Generator, "install_dependencies_and_show_progress_bar", return_value=None
    )
    @mock.patch.object(Generator, "download_template_files", return_value=None)
    @mock.patch.object(Generator, "create_required_directories", return_value=None)
    @mock.patch("django.core.management.call_command")
    @mock.patch.object(Generator, "check_system_requirements", return_value=None)
    def test_generate_in_production_mode(
        self,
        mocked_generator_check_system_requirements,
        mocked_management_call_command,
        mocked_create_required_directories,
        mocked_download_template_files,
        mocked_install_dependencies_and_show_progress_bar,
        app_generator,
    ):

        """
        Function to test the generate method of the Generator Class
        """

        # set the environment variable SOFTWARE_ENVIRONMENT_MODE to production
        # to test that the download_template_files method is called or not

        # create the monkeypatch object
        monkeypatch = pytest.MonkeyPatch()

        # set the environment variable SOFTWARE_ENVIRONMENT_MODE to production
        monkeypatch.setenv("SOFTWARE_ENVIRONMENT_MODE", "production")

        # assert that the environment variable has changed
        assert os.environ["SOFTWARE_ENVIRONMENT_MODE"] == "production"

        # call the method to test
        app_generator.generate()

        # assert that all the methods of the Generator class are called
        assert mocked_generator_check_system_requirements.called == True
        assert mocked_create_required_directories.called == True
        mocked_management_call_command.assert_called_once_with(
            "startapp", app_generator.app_name
        )
        assert mocked_download_template_files.called == True
        assert mocked_install_dependencies_and_show_progress_bar.called == True
