clean: 
	pip uninstall acnaweblib -y

install:
	python setup.py install

dev:
	pip install -e .
	pip install -r requirements-dev.txt

build:
	python -m build

help:
	python setup.py --help-commands	

package: 
	rm -rf dist
	python setup.py sdist 

publish: package
	twine upload dist/*


