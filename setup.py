import os
from setuptools import setup, find_packages


def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


setup(
    name = 'stencil-flask',
    version = '0.1.dev',
    description = 'Flask app template',
    author = 'Dima Kukushkin',
    author_email = 'dima@kukushkin.me',
    long_description=read('README.rst') + '\n\n' + read('HISTORY.rst'),
    packages = find_packages(),
    include_package_data = True,
    install_requires = [
        'Stencil',
    ],
    entry_points = {
        'stencils': [
            'flask = stencil_flask.flask:Flask',
        ],
    }
)
