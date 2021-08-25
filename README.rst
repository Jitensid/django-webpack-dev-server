=====
django-webpack-dev-server
=====

Django Webpack Dev Server is a Django app to create configuration files for frontend Javascript framework. It uses webpack to bundle your frontend code.

Installation
-----------

Install using pip...

```
pip install django-webpack-dev-server
```

Quick start
-----------

1. Add "django-webpack-dev-server" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'django-webpack-dev-server',
    ]

2. Run ``python manage.py generate react`` to create a django app which has reactjs configuration.

3. Add the new django app to your INSTALLED_APPS setting like in step 1.

4. Configure urls.py of the project to point it to the newly created django app.

5. Start the django development server and cd into the new app and 
	run npm start

License
-----------
MIT