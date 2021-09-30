import os

DEVELOPMENT_ASSETS_DIRECTORY_PATH = os.path.join(os.getcwd(), "assets")

APP_DIRECTORY_NAME = "APP"
SRC_DIRECTORY_NAME = "src"
TEMPLATES_DIRECTORY_NAME = "templates"
COMMON_ASSETS_DIRECTORY = "Common"
REACTTS = "reactts"

# stores the paths of the reactjs template files which are loaded locally
DEV_REACTTS_TEMPLATES_PATHS_DICT = {
    "package.json-tpl": os.path.join(
        DEVELOPMENT_ASSETS_DIRECTORY_PATH, REACTTS, "package.json-tpl"
    ),
    "webpack.config.js-tpl": os.path.join(
        DEVELOPMENT_ASSETS_DIRECTORY_PATH, REACTTS, "webpack.config.js-tpl"
    ),
    "babel.config.json-tpl": os.path.join(
        DEVELOPMENT_ASSETS_DIRECTORY_PATH, REACTTS, "babel.config.json-tpl"
    ),
    "tsconfig.json-tpl": os.path.join(
        DEVELOPMENT_ASSETS_DIRECTORY_PATH, REACTTS, "tsconfig.json-tpl"
    ),
    "module.d.ts-tpl": os.path.join(
        DEVELOPMENT_ASSETS_DIRECTORY_PATH, REACTTS, "module.d.ts-tpl"
    ),
    "App.tsx-tpl": os.path.join(
        DEVELOPMENT_ASSETS_DIRECTORY_PATH, REACTTS, "App.tsx-tpl"
    ),
    "index.tsx-tpl": os.path.join(
        DEVELOPMENT_ASSETS_DIRECTORY_PATH, REACTTS, "index.tsx-tpl"
    ),
    "App.css-tpl": os.path.join(
        DEVELOPMENT_ASSETS_DIRECTORY_PATH, REACTTS, "App.css-tpl"
    ),
    "reactlogo.png": os.path.join(
        DEVELOPMENT_ASSETS_DIRECTORY_PATH, REACTTS, "reactlogo.png"
    ),
}

# Development template files for reactjs configuration
DEV_REACTTS_TEMPLATE_FILES = [
    (
        APP_DIRECTORY_NAME,
        "package.json",
        DEV_REACTTS_TEMPLATES_PATHS_DICT["package.json-tpl"],
    ),
    (
        APP_DIRECTORY_NAME,
        "webpack.config.js",
        DEV_REACTTS_TEMPLATES_PATHS_DICT["webpack.config.js-tpl"],
    ),
    (
        APP_DIRECTORY_NAME,
        "babel.config.json",
        DEV_REACTTS_TEMPLATES_PATHS_DICT["babel.config.json-tpl"],
    ),
    (
        APP_DIRECTORY_NAME,
        "tsconfig.json",
        DEV_REACTTS_TEMPLATES_PATHS_DICT["tsconfig.json-tpl"],
    ),
    (
        SRC_DIRECTORY_NAME,
        "module.d.ts",
        DEV_REACTTS_TEMPLATES_PATHS_DICT["module.d.ts-tpl"],
    ),
    (SRC_DIRECTORY_NAME, "App.tsx", DEV_REACTTS_TEMPLATES_PATHS_DICT["App.tsx-tpl"]),
    (
        SRC_DIRECTORY_NAME,
        "index.tsx",
        DEV_REACTTS_TEMPLATES_PATHS_DICT["index.tsx-tpl"],
    ),
    (SRC_DIRECTORY_NAME, "App.css", DEV_REACTTS_TEMPLATES_PATHS_DICT["App.css-tpl"]),
    (
        SRC_DIRECTORY_NAME,
        "reactlogo.png",
        DEV_REACTTS_TEMPLATES_PATHS_DICT["reactlogo.png"],
    ),
]
