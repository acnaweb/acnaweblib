clean: 
	pip uninstall acnaweblib -y

install: clean
	python setup.py install

dev: clean
	pip install -e .
	pip install -r requirements-dev.txt

build:
	python -m build

help:
	python setup.py --help-commands	

lint:
	python setup.py flake8

test:
	python setup.py test	

package: 
	rm -rf dist
	python setup.py sdist 

push: test package 
	twine upload dist/*

