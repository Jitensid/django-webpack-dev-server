from setuptools import setup, find_packages

package_description = 'A Django app to create configuration files for frontend Javascript framework.'

setup(
    name='django-webpack-dev-server',
    version='0.0.11',
    packages=find_packages(),
    license='MIT',
    author='Jiten Sidhpura',
    author_email='jitensidhpura2000@gmail.com',
    description=package_description,
    long_description=open('README.rst').read(),
    long_description_content_type='text/x-rst',
    url='https://github.com/Jitensid/django-webpack-dev-server',
    download_url='https://github.com/Jitensid/django-webpack-dev-server/archive/refs/tags/0.0.11.tar.gz',
    install_requires=['requests', 'progressbar2', 'python-dotenv'],
    keywords=['django', 'webpack', 'webpack_dev_server', 'react'],
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.8',
    ]
)
