APP_DIRECTORY_NAME = "APP"
SRC_DIRECTORY_NAME = "src"
TEMPLATES_DIRECTORY_NAME = "templates"

# Production React Js Template files having Github Repository Links
REACTJS_TEMPLATES_URLS_DICT = {
    "package.json-tpl": "https://raw.githubusercontent.com/Jitensid/django-webpack-dev-server/main/assets/reactjs/package.json-tpl",
    "webpack.config.js-tpl": "https://raw.githubusercontent.com/Jitensid/django-webpack-dev-server/main/assets/reactjs/webpack.config.js-tpl",
    "babel.config.json-tpl": "https://raw.githubusercontent.com/Jitensid/django-webpack-dev-server/main/assets/reactjs/babel.config.json-tpl",
    "App.js-tpl": "https://raw.githubusercontent.com/Jitensid/django-webpack-dev-server/main/assets/reactjs/App.js-tpl",
    "index.js-tpl": "https://raw.githubusercontent.com/Jitensid/django-webpack-dev-server/main/assets/reactjs/index.js-tpl",
    "App.css-tpl": "https://raw.githubusercontent.com/Jitensid/django-webpack-dev-server/main/assets/reactjs/App.css-tpl",
    "reactlogo.png": "https://raw.githubusercontent.com/Jitensid/django-webpack-dev-server/main/assets/reactjs/reactlogo.png",
}

# Template files specific to react js configuration
PROD_REACTJS_TEMPLATE_FILES = [
    (
        APP_DIRECTORY_NAME,
        "package.json",
        REACTJS_TEMPLATES_URLS_DICT["package.json-tpl"],
    ),
    (
        APP_DIRECTORY_NAME,
        "webpack.config.js",
        REACTJS_TEMPLATES_URLS_DICT["webpack.config.js-tpl"],
    ),
    (
        APP_DIRECTORY_NAME,
        "babel.config.json",
        REACTJS_TEMPLATES_URLS_DICT["babel.config.json-tpl"],
    ),
    (SRC_DIRECTORY_NAME, "App.js", REACTJS_TEMPLATES_URLS_DICT["App.js-tpl"]),
    (SRC_DIRECTORY_NAME, "index.js", REACTJS_TEMPLATES_URLS_DICT["index.js-tpl"]),
    (SRC_DIRECTORY_NAME, "App.css", REACTJS_TEMPLATES_URLS_DICT["App.css-tpl"]),
    (SRC_DIRECTORY_NAME, "reactlogo.png", REACTJS_TEMPLATES_URLS_DICT["reactlogo.png"]),
]
