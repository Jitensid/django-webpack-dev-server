from django_webpack_dev_server.management.template_constants.production.reactjs_constants import (
    PROD_REACTJS_TEMPLATE_FILES,
)

from django_webpack_dev_server.management.template_constants.production.reactts_constants import (
    PROD_REACTTS_TEMPLATE_FILES,
)

APP_DIRECTORY_NAME = "APP"
SRC_DIRECTORY_NAME = "src"
TEMPLATES_DIRECTORY_NAME = "templates"


COMMON_TEMPLATES_URLS_DICT = {
    "urls.py-tpl": "https://raw.githubusercontent.com/Jitensid/django-webpack-dev-server/main/assets/Common/urls.py-tpl",
    "views.py-tpl": "https://raw.githubusercontent.com/Jitensid/django-webpack-dev-server/main/assets/Common/views.py-tpl",
    "index.html-tpl": "https://raw.githubusercontent.com/Jitensid/django-webpack-dev-server/main/assets/Common/index.html-tpl",
    "djangologo.png": "https://raw.githubusercontent.com/Jitensid/django-webpack-dev-server/main/assets/Common/djangologo.png",
}

# Template files that will be common for any frontend library or framework
COMMON_TEMPLATE_FILES = [
    (APP_DIRECTORY_NAME, "urls.py", COMMON_TEMPLATES_URLS_DICT["urls.py-tpl"]),
    (APP_DIRECTORY_NAME, "views.py", COMMON_TEMPLATES_URLS_DICT["views.py-tpl"]),
    (
        SRC_DIRECTORY_NAME,
        "djangologo.png",
        COMMON_TEMPLATES_URLS_DICT["djangologo.png"],
    ),
    (
        TEMPLATES_DIRECTORY_NAME,
        "index.html",
        COMMON_TEMPLATES_URLS_DICT["index.html-tpl"],
    ),
]

PROD_ALL_REACTJS_TEMPLATE_FILES = COMMON_TEMPLATE_FILES + PROD_REACTJS_TEMPLATE_FILES

PROD_ALL_REACTTS_TEMPLATE_FILES = COMMON_TEMPLATE_FILES + PROD_REACTTS_TEMPLATE_FILES
