import os

DEVELOPMENT_ASSETS_DIRECTORY_PATH = os.path.join(os.getcwd(), "assets")

APP_DIRECTORY_NAME = "APP"
SRC_DIRECTORY_NAME = "src"
TEMPLATES_DIRECTORY_NAME = "templates"
COMMON_ASSETS_DIRECTORY = "Common"
REACTJS = "reactjs"

# stores the paths of the reactjs template files which are loaded locally
DEV_REACTJS_TEMPLATES_PATHS_DICT = {
    "package.json-tpl": os.path.join(
        DEVELOPMENT_ASSETS_DIRECTORY_PATH, REACTJS, "package.json-tpl"
    ),
    "webpack.config.js-tpl": os.path.join(
        DEVELOPMENT_ASSETS_DIRECTORY_PATH, REACTJS, "webpack.config.js-tpl"
    ),
    "babel.config.json-tpl": os.path.join(
        DEVELOPMENT_ASSETS_DIRECTORY_PATH, REACTJS, "babel.config.json-tpl"
    ),
    "App.js-tpl": os.path.join(
        DEVELOPMENT_ASSETS_DIRECTORY_PATH, REACTJS, "App.js-tpl"
    ),
    "index.js-tpl": os.path.join(
        DEVELOPMENT_ASSETS_DIRECTORY_PATH, REACTJS, "index.js-tpl"
    ),
    "App.css-tpl": os.path.join(
        DEVELOPMENT_ASSETS_DIRECTORY_PATH, REACTJS, "App.css-tpl"
    ),
    "reactlogo.png": os.path.join(
        DEVELOPMENT_ASSETS_DIRECTORY_PATH, REACTJS, "reactlogo.png"
    ),
}

# Development template files for reactjs configuration
DEV_REACTJS_TEMPLATE_FILES = [
    (
        APP_DIRECTORY_NAME,
        "package.json",
        DEV_REACTJS_TEMPLATES_PATHS_DICT["package.json-tpl"],
    ),
    (
        APP_DIRECTORY_NAME,
        "webpack.config.js",
        DEV_REACTJS_TEMPLATES_PATHS_DICT["webpack.config.js-tpl"],
    ),
    (
        APP_DIRECTORY_NAME,
        "babel.config.json",
        DEV_REACTJS_TEMPLATES_PATHS_DICT["babel.config.json-tpl"],
    ),
    (SRC_DIRECTORY_NAME, "App.js", DEV_REACTJS_TEMPLATES_PATHS_DICT["App.js-tpl"]),
    (SRC_DIRECTORY_NAME, "index.js", DEV_REACTJS_TEMPLATES_PATHS_DICT["index.js-tpl"]),
    (SRC_DIRECTORY_NAME, "App.css", DEV_REACTJS_TEMPLATES_PATHS_DICT["App.css-tpl"]),
    (
        SRC_DIRECTORY_NAME,
        "reactlogo.png",
        DEV_REACTJS_TEMPLATES_PATHS_DICT["reactlogo.png"],
    ),
]
