from setuptools import setup, find_packages

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='django-videokit',

    version='0.0.3',

    description='Video storage and processing for Django',
    long_description=long_description,

    url='https://github.com/pstreck/django-videokit',

    author='Philip Streck',
    author_email='philip.streck@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],

    # What does your project relate to?
    keywords='django video development',

    packages=find_packages(exclude=['tests', 'example']),
)
