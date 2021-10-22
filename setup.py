from setuptools import setup, find_packages

package_description = (
    "A Django app to setup configuration files for React in a Django Project."
)

keywords_list = [
    "django",
    "react",
    "webpack4",
    "webpack_dev_server",
    "command-line",
    "project-generator",
    "template-generator",
    "javascript",
    "typescript",
]

setup(
    name="django-webpack-dev-server",
    version="0.0.16",
    packages=find_packages(),
    license="MIT",
    author="Jiten Sidhpura",
    author_email="jitensidhpura2000@gmail.com",
    description=package_description,
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Jitensid/django-webpack-dev-server",
    download_url="https://github.com/Jitensid/django-webpack-dev-server/archive/refs/tags/0.0.16.tar.gz",
    install_requires=["requests", "progressbar2", "python-dotenv"],
    keywords=keywords_list,
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Code Generators",
        "Framework :: Django",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
