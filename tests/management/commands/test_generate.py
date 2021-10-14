from django.core.management import call_command
from unittest import mock
from django_webpack_dev_server.management.generator import Generator


class TestCommand:
    """
    Test Class for testing the Command Class defined in the generate.py
    """

    @mock.patch.object(Generator, "generate")
    def test_command(self, mocked_Generator_generate):
        """
        Function to test the methods of the Command Class
        """
        # call the management command to test
        call_command("generate", "react")

        # assert that the generate method of the Generator class is called
        assert mocked_Generator_generate.called == True
