# django-webpack-dev-server

[![PyPI version](https://badge.fury.io/py/django-webpack-dev-server.svg)](https://badge.fury.io/py/django-webpack-dev-server)
[![codecov](https://codecov.io/gh/Jitensid/django-webpack-dev-server/branch/main/graph/badge.svg?token=D952NCAC8I)](https://codecov.io/gh/Jitensid/django-webpack-dev-server)
[![Requirements Status](https://requires.io/github/Jitensid/django-webpack-dev-server/requirements.svg?branch=main)](https://requires.io/github/Jitensid/django-webpack-dev-server/requirements/?branch=main)
[![CI](https://github.com/Jitensid/django-webpack-dev-server/actions/workflows/main.yml/badge.svg)](https://github.com/Jitensid/django-webpack-dev-server/actions/workflows/main.yml)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/Jitensid/django-webpack-dev-server/main.svg)](https://results.pre-commit.ci/latest/github/Jitensid/django-webpack-dev-server/main)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License MIT](https://img.shields.io/github/license/Jitensid/django-webpack-dev-server?color=purple)](https://github.com/Jitensid/django-webpack-dev-server/blob/main/LICENSE)

Django Webpack Dev Server is a command line Django reusable app to setup configuration files for React. It uses webpack and webpack_dev_server to
bundle your frontend code.

## Installation

Install using pip

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

3.  Run `python manage.py generate react` to create a django app with the default app_name and template.

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

## Important Links

1. [Check out Tech with Tim's Youtube Playlist for a detailed explanation in building Django and React Full Stack App.](https://www.youtube.com/watch?v=JD-age0BPVo&list=PLzMcBGfZo4-kCLWnGmK0jUBmGLaJxvi4j)

2. [Webpack Documentation if you want to change configurations.](https://v4.webpack.js.org/concepts/)

## Contributions

If you find an issue or have a new feature then feel free to make a Pull Request. Your Contributions are always welcomed.

### Running the Package in Development Mode

1. You can run the package in development mode by setting the "SOFTWARE_ENVIRONMENT_MODE" environment variable equal to "development".

2. Now you can load assets from your local system and the new changes can be tested.

## License

This project is provided under the [MIT License](https://github.com/Jitensid/django-webpack-dev-server/blob/main/LICENSE).
