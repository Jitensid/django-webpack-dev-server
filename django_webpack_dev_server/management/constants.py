APP = 'APP'
SRC = 'src'
TEMPLATES = 'templates'

COMMON = 'Common'
REACTJS = 'reactjs'

REPO_BASE_URL = 'https://raw.githubusercontent.com/Jitensid/django-webpack-dev-server/main/assets/'

COMMON_TEMPLATE_FILENAMES = [
    (APP, 'urls.py', REPO_BASE_URL + COMMON + '/urls.py-tpl'),
    (APP, 'views.py', REPO_BASE_URL + COMMON + '/views.py-tpl'),
    (SRC, 'djangologo.jpg', REPO_BASE_URL + COMMON + '/djangologo.jpg'),
    (TEMPLATES, 'index.html', REPO_BASE_URL + COMMON + '/index.html-tpl'),
]

REACTJS_TEMPLATE_FILENAMES = [
    (APP, 'package.json', REPO_BASE_URL + REACTJS + '/package.json-tpl'),
    (APP, 'webpack.config.js', REPO_BASE_URL + REACTJS + '/webpack.config.js-tpl'),
    (APP, 'babel.config.json', REPO_BASE_URL + REACTJS + '/babel.config.json-tpl'),
    (SRC, 'App.js', REPO_BASE_URL + REACTJS + '/App.js-tpl'),
    (SRC, 'index.js', REPO_BASE_URL + REACTJS + '/index.js-tpl'),
    (SRC, 'App.css', REPO_BASE_URL + REACTJS + '/App.css-tpl'),
    (SRC, 'reactlogo.png', REPO_BASE_URL + REACTJS + '/reactlogo.png'),
]

REACTJS_TEMPLATE_FILENAMES = REACTJS_TEMPLATE_FILENAMES + COMMON_TEMPLATE_FILENAMES

TEMPLATE_FILES_DICT = {
    'react': REACTJS_TEMPLATE_FILENAMES,
}
