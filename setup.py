from setuptools import setup, find_packages


requirements = []

setup(
    name='acnaweblib',
    version='0.1.0',
    description='Setting up a python package',
    author='Antonio Carlos de Lima Junior',
    author_email='antonioclj.ac@gmail.com',
    url='https://github.com/acnaweb/acnaweb-lib',
    packages=find_packages(include=['acnaweblib', 'acnaweblib.*']),
    install_requires=requirements
)
