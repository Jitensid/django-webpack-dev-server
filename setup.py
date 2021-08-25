from distutils.core import setup

package_description = 'A Django app to create configuration files for frontend Javascript framework.'

setup(
    name='django-webpack-dev-server',
    version='0.0.3',
    license='MIT',
    author='Jiten Sidhpura',
    author_email='jitensidhpura2000@gmail.com',
    description=package_description,
    long_description=open('README.rst').read(),
    url='https://github.com/Jitensid/django-webpack-dev-server',
    download_url='https://github.com/Jitensid/django-webpack-dev-server/archive/refs/tags/0.0.3.tar.gz',
    requires=['requests', 'progressbar2'],
    keywords=['django', 'webpack', 'webpack_dev_server', 'react'],
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.8',
    ]
)
