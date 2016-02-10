# Prettifier

[![Build Status](https://travis-ci.org/marinampires/prettifier.svg?branch=master)](https://travis-ci.org/marinampires/prettifier)

Library to prettifier big number as millions, billions and trillions

## Requirements
Have python 2.7 or higher installed

## Build 
Go to directory prettifier
Run command to generate the distribution
```bash
	$ cd prettifier
	$ python setup.py sdist
```
*** the distribution file (Prettifier-0.1.tar.gz) is alredy built in dist directory ***


## Install in your python enviroment
Copy the file Prettifier-0.1.tar.gz to an directory and unzip it.

Go to directory Prettifier-0.1

Run command to install it
```bash
	$ tar -zxvf Prettifier-0.1.tar.gz 
	$ cd Prettifier-0.1
	$ python setup.py install
```

## Usage
### Command Line Interface

```bash
    $ python -m prettifier.tool 12345
    12345

    $ python -m prettifier.tool 1234567899
    1.2B

    $ python -m prettifier.tool number
    The type is not a numeric value
```
### Python Library

```python
	>>> from prettifier.number_prettifier import prettify
	>>> number = 123456789
	>>> number_prettified = prettify(number)
	>>> print number_prettified
	123.4M
```

## TESTS
### Run tests
```bash
	$ python -m unittest -v tests.prettifier_test
```

