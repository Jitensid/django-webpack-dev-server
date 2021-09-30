from django_webpack_dev_server.management.template_constants.development import (
    development_constants,
)
from django_webpack_dev_server.management.template_constants.production import (
    production_constants,
)

# To Identify if the operating system is windows based or not
WINDOWS_OS_IDENTIFIER = "win32"

APP_DIRECTORY_NAME = "APP"
SRC_DIRECTORY_NAME = "src"
TEMPLATES_DIRECTORY_NAME = "templates"

COMMON_ASSETS_DIRECTORY = "Common"

# Store the development template filenames with frontend library or framework as key
DEVELOPMENT_TEMPLATE_FILES_DICT = {
    "react_javascript": development_constants.DEV_ALL_REACTJS_TEMPLATE_FILES,
    "react_typescript": development_constants.DEV_ALL_REACTTS_TEMPLATE_FILES,
}


# Store template filenames with frontend library or framework as key
PROD_TEMPLATE_FILES_DICT = {
    "react_javascript": production_constants.PROD_ALL_REACTJS_TEMPLATE_FILES,
    "react_typescript": production_constants.PROD_ALL_REACTTS_TEMPLATE_FILES,
}

# show relevent error messages to the user
COMMAND_ERROR_MESSAGES_DICT = {
    "INVALID_APP_NAME_ERROR_MESSAGE": "App Name should be alphanumeric only",
    "SYSTEM_ERROR_MESSAGE": "Seems like node or npm is not available in your system",
    "STATICFILES_DIRS_MISSING_ERROR_MESSAGE": "STATICFILES_DIRS attribute is missing in the django settings file",
    "NPM_INSTALLATION_ERROR_MESSAGE": "There were some errors while installing dependencies",
}
