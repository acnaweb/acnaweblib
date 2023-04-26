from setuptools import setup, find_packages

def readme():
    with open('README.md') as f:
        return f.read()

requirements = []

setup(
    name='acnaweblib',
    version='0.1.14',
    # description='Short description',
    long_description=readme(),
    long_description_content_type="text/markdown",
    author='Antonio Carlos de Lima Junior',
    author_email='antonioclj.ac@gmail.com',
    url='https://github.com/acnaweb/acnaweb-lib',
    packages=find_packages(include=['acnaweblib', 'acnaweblib.*']),
    install_requires=requirements,
    classifiers=[               
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3',        
        'Operating System :: OS Independent',
        'Natural Language :: Portuguese (Brazilian)',
        'Natural Language :: English',

      ],
    keywords='library test',
    license='MIT',
)
