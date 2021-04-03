# Unit tests developed with unittest

## Running Unit Tests
Use the following command inside of `src` to run the unit tests:
```python
nosetests -w ./ --with-coverage --cover-html --cover-package=./ --cover-erase --with-timer --timer-top-n 10
```
A folder called `cover` will be created in `src` post running the
command. You can open `cover/index.html` to view the lines (if any)
that need to be additionally covered in the unit tests.
