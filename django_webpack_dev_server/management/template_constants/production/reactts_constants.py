APP_DIRECTORY_NAME = "APP"
SRC_DIRECTORY_NAME = "src"
TEMPLATES_DIRECTORY_NAME = "templates"

# Production React Ts Template files having Github Repository Links
REACTTS_TEMPLATES_URLS_DICT = {
    "package.json-tpl": "https://raw.githubusercontent.com/Jitensid/django-webpack-dev-server/main/assets/reactts/package.json-tpl",
    "webpack.config.js-tpl": "https://raw.githubusercontent.com/Jitensid/django-webpack-dev-server/main/assets/reactts/webpack.config.js-tpl",
    "babel.config.json-tpl": "https://raw.githubusercontent.com/Jitensid/django-webpack-dev-server/main/assets/reactts/babel.config.json-tpl",
    "tsconfig.json-tpl": "https://raw.githubusercontent.com/Jitensid/django-webpack-dev-server/main/assets/reactts/tsconfig.json-tpl",
    "module.d.ts-tpl": "https://raw.githubusercontent.com/Jitensid/django-webpack-dev-server/main/assets/reactts/module.d.ts-tpl",
    "App.tsx-tpl": "https://raw.githubusercontent.com/Jitensid/django-webpack-dev-server/main/assets/reactts/App.tsx-tpl",
    "index.tsx-tpl": "https://raw.githubusercontent.com/Jitensid/django-webpack-dev-server/main/assets/reactts/index.tsx-tpl",
    "App.css-tpl": "https://raw.githubusercontent.com/Jitensid/django-webpack-dev-server/main/assets/reactts/App.css-tpl",
    "reactlogo.png": "https://raw.githubusercontent.com/Jitensid/django-webpack-dev-server/main/assets/reactts/reactlogo.png",
}

# Template files specific to react ts configuration
PROD_REACTTS_TEMPLATE_FILES = [
    (
        APP_DIRECTORY_NAME,
        "package.json",
        REACTTS_TEMPLATES_URLS_DICT["package.json-tpl"],
    ),
    (
        APP_DIRECTORY_NAME,
        "webpack.config.js",
        REACTTS_TEMPLATES_URLS_DICT["webpack.config.js-tpl"],
    ),
    (
        APP_DIRECTORY_NAME,
        "babel.config.json",
        REACTTS_TEMPLATES_URLS_DICT["babel.config.json-tpl"],
    ),
    (
        APP_DIRECTORY_NAME,
        "tsconfig.json",
        REACTTS_TEMPLATES_URLS_DICT["tsconfig.json-tpl"],
    ),
    (SRC_DIRECTORY_NAME, "module.d.ts", REACTTS_TEMPLATES_URLS_DICT["module.d.ts-tpl"]),
    (SRC_DIRECTORY_NAME, "App.tsx", REACTTS_TEMPLATES_URLS_DICT["App.tsx-tpl"]),
    (SRC_DIRECTORY_NAME, "index.tsx", REACTTS_TEMPLATES_URLS_DICT["index.tsx-tpl"]),
    (SRC_DIRECTORY_NAME, "App.css", REACTTS_TEMPLATES_URLS_DICT["App.css-tpl"]),
    (SRC_DIRECTORY_NAME, "reactlogo.png", REACTTS_TEMPLATES_URLS_DICT["reactlogo.png"]),
]
