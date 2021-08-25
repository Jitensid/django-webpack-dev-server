from distutils.core import setup

package_description = 'Django Webpack Dev Server is a Django app to create configuration files for frontend Javascript framework It uses webpack to bundle your frontend code.'

setup(
    name='django_webpack_dev_server',
    packages=['django_webpack_dev_server'],
    version='0.1',
    license='MIT',
    author='Jiten Sidhpura',
    author_email='jitensidhpura2000@gmail.com',
    description=package_description,
    url='https://github.com/Jitensid/django_webpack_dev_server',
    download_url='https://github.com/Jitensid/django_webpack_dev_server/archive/refs/tags/0.0.1.tar.gz',
    requires=['requests', 'progressbar2'],
    keywords=['django', 'webpack', 'webpack_dev_server', 'react'],
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3+',
    ]
)
