# pyhumour

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


## TODO

0. Use [cookiecutter](https://github.com/cookiecutter/cookiecutter) 
1. Manifest
2. travis.yml
3. Badges
    - Code Coverage (Coveralls, codecov.io)
    - Quality Metrics (Code Climate, Landscape.io)
4. bumpversion - to manage versioning
5. Test on OSX & Windows