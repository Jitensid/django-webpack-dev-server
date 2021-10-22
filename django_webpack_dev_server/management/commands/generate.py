# Contains the code for the generate command

from django.core.management.base import BaseCommand
from django_webpack_dev_server.management.generator import Generator


class Command(BaseCommand):
    help = "Creates a django app which has the frontend configuration"

    def add_arguments(self, parser):

        # adding subparser for react
        subparsers = parser.add_subparsers(
            help="Command to create a django app which has the frontend configuration",
            dest="frontend_library_or_framework",
        )

        subparsers.required = True

        # add a parser for react because it can be javascript or typescript
        react_parser = subparsers.add_parser(
            "react",
            help="Command to have django app with React for Frontend Development",
        )

        language_choices = ["javascript", "typescript"]
        # add the optional app_name argument with the default value as frontend
        react_parser.add_argument(
            "--app_name", help="Frontend Django App Name", default="frontend"
        )

        # add the optional template argument with the default value as javascript
        # template argument can be either javascript or typescript
        react_parser.add_argument(
            "--template",
            help="Language for the React Project",
            default="javascript",
            choices=language_choices,
        )

    def show_success_message(self, message):
        """
        :param message: message to be shown in stdout with success style
        """
        self.stdout.write(self.style.SUCCESS(message))

    def handle(self, *args, **options):

        # get the django app_name and the frontend_library_or_framework
        # specified by the user
        app_name = options["app_name"]
        frontend_library_or_framework = options["frontend_library_or_framework"]

        # if the frontend_library_or_framework is react
        if frontend_library_or_framework == "react":
            # fetch the template argument
            template = options["template"]

            # append it to the frontend_library_or_framework
            # react and javascript -> react_javascript for React Javascript
            # react and typescript -> react_typescript for React Typescript
            frontend_library_or_framework += "_" + template

        # Create a Generator object and pass app_name and frontend_library_or_framework
        app_generator = Generator(
            app_name=app_name,
            frontend_library_or_framework=frontend_library_or_framework,
        )
        # start building the new django app
        app_generator.generate()

        # show success messages to the user after the command is successfully
        # executed
        self.show_success_message("\n\nYour App is Ready !!!")
        self.show_success_message(
            f"Add {app_name} in the INSTALLED_APPS list in the project's settings.py file"
        )
        self.show_success_message(
            f"Add {app_name}.urls in urlpatterns of the project's urls.py"
        )
        self.show_success_message(
            "Start the Django Server and cd into your app and run npm start"
        )
