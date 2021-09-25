=========================
django-webpack-dev-server 
=========================

.. image:: https://badge.fury.io/py/django-webpack-dev-server.svg?
    :target: https://badge.fury.io/py/django-webpack-dev-server

.. image:: https://requires.io/github/Jitensid/django-webpack-dev-server/requirements.svg?branch=main
     :target: https://requires.io/github/Jitensid/django-webpack-dev-server/requirements/?branch=main
     :alt: Requirements Status



Django Webpack Dev Server is a Django app to create configuration files for frontend such as React. 
It uses webpack and webpack_dev_server to bundle your frontend code.

Installation
------------

Install using pip...

``pip install django-webpack-dev-server``

Supported Frontend Frameworks or Library
----------------------------------------

1. React (Javascript)
2. React (Typescript)


Quick start
-----------

1. Add 'django_webpack_dev_server' to your INSTALLED_APPS in settings.py like this::

    INSTALLED_APPS = [
        ...
        'django_webpack_dev_server',
    ]

2. Set the STATICFILES_DIRS attirbute in the settings.py file like this::

    import os
    
    ...
    
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static')
    ]

3. Run ``python manage.py generate react`` to create a django app which has reactjs configuration.

4. Default django app name is frontend. You can provide your name by running ``python manage.py generate react --app_name your_app_name``

5. Add the new django app to your INSTALLED_APPS setting like in step 1.

6. Configure urls.py of the project to point it to the newly created django app.

7. Run ``python manage.py runserver`` to start the django's development server.

8. cd into the newly created django app and run ``npm start`` and go to (http://localhost:8080/).

9. Run ``npm run build`` to create a production build of your frontend code.

License
-------
MIT