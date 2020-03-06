from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='proyectoPython',
    version='0.0.1',
    description='Simulacion aplicacion de gestion de comercio...',
    long_description=long_description,
    url='https://pypi.python.org',
    author='finfanterodal',
    license='GNU GPLv3',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Topic :: Utilities',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
    ],
    keywords='proyectoPython',
    packages=['App'],
)
