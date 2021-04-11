# pyhumour

This is a module for the characterization and quantification of concise humour using 9 distinct computational features.
These features were inspired by [Ritchie's Incongruity-Resolution Theory](https://era.ed.ac.uk/handle/1842/3397), and are formulated as follows:


## Installation

Run the following to install:
```python
pip install pyhumour
```


## Usage


## Developing pyhumour

To install pyhumour, along with the tools you need to develop and run tests, run the following in your virtualenv:
```bash
pip install -e .[dev]
```


## Distributing pyhumour

```python
python setup.py bdist_wheel
```

```python
python setup.py sdist
```


## Pushing pyhumour (to pypi)

```bash
pip install twine
```

```python
twine upload dist/*
```


## Testing in different distributions of python

```bash
pip install tox
```

```python
tox
```
## Unit tests developed with unittest

### Running Unit Tests
Use the following command inside of git root directory to run the unit tests:
```python
nosetests -w ./ --with-coverage --cover-html --cover-package=./ --cover-erase --with-timer --timer-top-n 10
```
A folder called `cover` will be created in `src` post running the
command. You can open `cover/index.html` to view the lines (if any)
that need to be additionally covered in the unit tests.


## TODO

1. Use [cookiecutter](https://github.com/cookiecutter/cookiecutter) 
2. travis.yml
3. Badges
    - Code Coverage (Coveralls, codecov.io)
    - Quality Metrics (Code Climate, Landscape.io)
4. bumpversion - to manage versioning
5. Test on OSX & Windows