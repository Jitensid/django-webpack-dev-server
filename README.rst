=========================
django-webpack-dev-server 
=========================

.. image:: https://badge.fury.io/py/django-webpack-dev-server.svg?
    :target: https://badge.fury.io/py/django-webpack-dev-server
    
|

Django Webpack Dev Server is a Django app to create configuration files for frontend Javascript framework. It uses webpack to bundle your frontend code.

Installation
------------

Install using pip...

``pip install django-webpack-dev-server``

Supported Frontend Frameworks or Library
----------------------------------------

1. React (Javascript)


Quick start
-----------

1. Add "django_webpack_dev_server" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'django_webpack_dev_server',
    ]

2. Run ``python manage.py generate react`` to create a django app which has reactjs configuration.

3. Default django app name is frontend. You can provide your name by running ``python manage.py generate react --app_name your_app_name``

4. Add the new django app to your INSTALLED_APPS setting like in step 1.

5. Configure urls.py of the project to point it to the newly created django app.

6. Run ``python manage.py runserver`` to start the django's development Server.

7. cd into the newly created django app and run ``npm start``

License
-------
MIT