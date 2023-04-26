# Welcome to acnaweblib

![version](https://img.shields.io/badge/version-0.1.18-blue.svg?cacheSeconds=2592000) 
![licence](https://img.shields.io/badge/licence-MIT-green.svg?cacheSeconds=2592000)

This is a Python library for testing

## Installation

`acnaweblib` supports Python 3.8 and higher.

### System-wide or user-wide installation with pipx

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install `acnaweblib`.

```bash
$ pip install acnaweblib
```

## Usage

```python
from acnaweblib import calculator

# returns 6
result = calculator.add(4,2)

```

## Developing

Development requires Python 3.8+; otherwise you'll get false positive type failures.

To work on the `acnaweblib` code: pull the repository, create and activate a virtualenv, then run:

```bash
make dev
```

Testing

```bash
make test
```

Publish

```bash
make push
```



## Author

👤 **Antonio Carlos de Lima Junior**

* Website: https://www.linkedin.com/in/acnaweb/
* Github: [@acnaweb](https://github.com/acnaweb)
* LinkedIn: [@acnaweb](https://linkedin.com/in/acnaweb)


## References

- [Pypi Classifiers](https://pypi.org/classifiers/)
- [Python Packaging Tutorial](https://www.devdungeon.com/content/python-packaging-tutorial)
- [A Practical Guide to Using Setup.py](https://godatadriven.com/blog/a-practical-guide-to-using-setup-py/)