# pyhumour

This is a module for the characterization and quantification of concise humour using 10 distinct computational features.
These features were inspired by [Ritchie's Incongruity-Resolution Theory](https://era.ed.ac.uk/handle/1842/3397), and are formulated as follows:
1. Obviousness (`obviousness`)
2. Compatibility (`compatibility`)
3. Inappropriateness (`inappropriateness`)
4. Humorous Conflict (`humorous_conflict`)
5. Non-humorous Conflict (`non_humorous_conflict`)
6. Adjective Absurdity (`adjective_absurdity`)
7. Humorous Noun Absurdity (`humorous_noun_absurdity`)
8. Non-humorous Noun Absurdity (`non_humorous_noun_absurdity`)
9. HMM Probability (`hmm_probability`)
10. N-Gram Probability (`ngram_probability`)


## Example
```python
import pyhumour
a = pyhumour.PyHumour([<humorous_corpus>], [<non_humorous_corpus>])
a.fit()
a.obviousness('this is an obvious statement')
```


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

### Pushing to testpypi

```python
twine upload --repository testpypi dist/*
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