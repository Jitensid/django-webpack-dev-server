import os

from django_webpack_dev_server.management.template_constants.development.reactjs_constants import (
    DEV_REACTJS_TEMPLATE_FILES,
)

from django_webpack_dev_server.management.template_constants.development.reactts_constants import (
    DEV_REACTTS_TEMPLATE_FILES,
)

DEVELOPMENT_ASSETS_DIRECTORY_PATH = os.path.join(os.getcwd(), "assets")

APP_DIRECTORY_NAME = "APP"
SRC_DIRECTORY_NAME = "src"
TEMPLATES_DIRECTORY_NAME = "templates"
COMMON_ASSETS_DIRECTORY = "Common"
REACTJS = "reactjs"

# Paths of the common template files which are loaded locally
DEV_COMMON_TEMPLATES_PATHS_DICT = {
    "urls.py-tpl": os.path.join(
        DEVELOPMENT_ASSETS_DIRECTORY_PATH, COMMON_ASSETS_DIRECTORY, "urls.py-tpl"
    ),
    "views.py-tpl": os.path.join(
        DEVELOPMENT_ASSETS_DIRECTORY_PATH, COMMON_ASSETS_DIRECTORY, "views.py-tpl"
    ),
    "index.html-tpl": os.path.join(
        DEVELOPMENT_ASSETS_DIRECTORY_PATH, COMMON_ASSETS_DIRECTORY, "index.html-tpl"
    ),
    "djangologo.png": os.path.join(
        DEVELOPMENT_ASSETS_DIRECTORY_PATH, COMMON_ASSETS_DIRECTORY, "djangologo.png"
    ),
}

# Development template files which are common for any frontend library or framework
DEV_COMMON_TEMPLATE_FILES = [
    (
        APP_DIRECTORY_NAME,
        "urls.py",
        os.path.join(
            DEVELOPMENT_ASSETS_DIRECTORY_PATH, COMMON_ASSETS_DIRECTORY, "urls.py-tpl"
        ),
    ),
    (
        APP_DIRECTORY_NAME,
        "views.py",
        os.path.join(
            DEVELOPMENT_ASSETS_DIRECTORY_PATH, COMMON_ASSETS_DIRECTORY, "views.py-tpl"
        ),
    ),
    (
        SRC_DIRECTORY_NAME,
        "djangologo.png",
        os.path.join(
            DEVELOPMENT_ASSETS_DIRECTORY_PATH, COMMON_ASSETS_DIRECTORY, "djangologo.png"
        ),
    ),
    (
        TEMPLATES_DIRECTORY_NAME,
        "index.html",
        os.path.join(
            DEVELOPMENT_ASSETS_DIRECTORY_PATH, COMMON_ASSETS_DIRECTORY, "index.html-tpl"
        ),
    ),
]

DEV_ALL_REACTJS_TEMPLATE_FILES = DEV_COMMON_TEMPLATE_FILES + DEV_REACTJS_TEMPLATE_FILES

DEV_ALL_REACTTS_TEMPLATE_FILES = DEV_COMMON_TEMPLATE_FILES + DEV_REACTTS_TEMPLATE_FILES
