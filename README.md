# django-webpack-dev-server

[![PyPI version](https://badge.fury.io/py/django-webpack-dev-server.svg)](https://badge.fury.io/py/django-webpack-dev-server) [![Requirements Status](https://requires.io/github/Jitensid/django-webpack-dev-server/requirements.svg?branch=main)](https://requires.io/github/Jitensid/django-webpack-dev-server/requirements/?branch=main) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Django Webpack Dev Server is a Django app to create configuration files
for frontend such as React. It uses webpack and webpack_dev_server to
bundle your frontend code.

## Installation

Install using pip...

`pip install django-webpack-dev-server`

## Supported Frontend Library

1.  React (Javascript)
2.  React (Typescript)

## Quick start

1.  Add 'django_webpack_dev_server' to your INSTALLED_APPS in
    settings.py like this:

    ```python
        INSTALLED_APPS = [
            ...
            'django_webpack_dev_server',
        ]
    ```

2.  Default django app name is frontend and template is javascript. You can provide your name and template by running <br /> `python manage.py generate react --app_name your_app_name --template (javascript/typescript)`

3.  Run `python manage.py generate react` to create a django app with the default configuration.

4.  Add the new django app to your INSTALLED_APPS setting like in step 1.

5.  Add the path for the new django app in the urlpatterns of the project's urls.py like this:

    ```python
    from django.urls import path, include

    path("", include("your_app_name.urls")),
    ```

6.  Run `python manage.py runserver` to start the django's development
    server.

7.  `cd` into the newly created django app and run `npm start` and go to
    (<http://localhost:8080/>).

8.  Run `npm run build` to create a production build of your frontend code.

## License

MIT
