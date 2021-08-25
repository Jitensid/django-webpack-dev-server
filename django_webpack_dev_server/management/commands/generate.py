# Check if NPM and NODE is present in the system
# Create a normal Django app with the specified name
# Copy package.json file and install dependencies
# Copy other template files
# Run the complete project

import argparse
import subprocess
from django_webpack_dev_server.management.generator import Generator
from django.core.management.base import BaseCommand, CommandParser, CommandError
from django.core import management
from django.conf import settings


class Command(BaseCommand):
    help = 'Creates a django app which has the configuration files for the frontend framework'

    def add_arguments(self, parser):
        subparsers = parser.add_subparsers(
            help='Commands for the creating django app which has configurations of frontend framework', dest='frontend_library_or_framework', required=True)

        react_parser = subparsers.add_parser(
            'react', help='Command for using React for Frontend Development')

        react_parser.add_argument(
            '--app_name', help='Frontend App Name', default='frontend')

    def show_success_message(self, message):
        self.stdout.write(self.style.SUCCESS(message))

    def handle(self, *args, **options):
        app_name = options['app_name']
        frontend_library_or_framework = options['frontend_library_or_framework']

        app_generator = Generator(app_name=app_name,
                                  frontend_library_or_framework=frontend_library_or_framework)

        app_generator.generate()

        self.show_success_message(' Your App is Ready !!!')
        self.show_success_message(
            'Do not forget to add {0} in  the INSTALLED_APPS in the project settings file'.format(app_name))
        self.show_success_message(
            'Start the Django Server and cd into your app and run npm start')
