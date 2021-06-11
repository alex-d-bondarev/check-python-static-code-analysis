# check-python-static-code-analysis
Check if different code analysis tools can detect ugly code in Python

## Goals

Example code is working, but is not very readable. 
I am looking for a tool or set of tools that will show me:
* how unreadable the code is
* some kind of code readability score that can be used in CI to block PRs
* what parts of the code need refactoring
* refactoring suggestions

## Optional Goal

* Find code formatters that can fix code readability
* Measure analysis time

## Out of scope

* Test coverage
* Test security

## Plan

1. Collect the list of code analysers
1. Run multiple code analysers and collect results

## The List

**Analysers:** (also known as linters)
* [Bandit](https://github.com/PyCQA/bandit)
* [Mccabe](https://github.com/PyCQA/mccabe)
* [MyPy](http://mypy-lang.org/)
* [pep8](https://pypi.org/project/pep8/)
* [pycodestyle](https://github.com/PyCQA/pycodestyle)
* [pydocstyle](https://github.com/PyCQA/pydocstyle)
* [PyFlakes](https://github.com/PyCQA/pyflakes)
* [Pylint](https://www.pylint.org/)
* [Radon](http://radon.readthedocs.io/en/latest/)
* [wemake-python-styleguide](https://github.com/wemake-services/wemake-python-styleguide)

**Formatters:**
* [Autopep8](https://github.com/hhatto/autopep8)
* [Black](https://github.com/ambv/black)
* [Isort](https://github.com/timothycrosley/isort)
* [Yapf](https://github.com/google/yapf)

**Packages** (contain 2 or more analysers and probably formatters):
* [Flake8](https://flake8.pycqa.org/en/latest/)
* [hacking](https://pypi.org/project/hacking/)
* [Pylama](https://github.com/klen/pylama)

## How to set up

1. Checkout this repository.
1. Ensure that you have installed the following:
   1. [pyenv](https://github.com/pyenv/pyenv). 
      It will help to manage python version automatically.
   1. [pipenv](https://pypi.org/project/pipenv/)
      It will manage python dependencies and python version.
1. Run `PIPENV_YES=true pipenv install --ignore-pipfile`

## Results _WIP_

### Bandit

Run as `pipenv run bandit -r ./app`.
Covers only security issues. Out of scope.

### McCabe

Check McCabe complexity. Did not show anything in a standalone mode. 
Does not meet any of my goals.

tried like:
```shell
pipenv shell
cd app/examples
python -m real_python --min 1 real_python.py
```

### Summary

| Name | Status | Comments |
|------|--------|----------|
| Bandit | :x: | Out of Scope |
| Mccabe | :x: | Does not meet my goals |

## My Conclusions

TBD

## References
* [Clean Code videos by Robert C. Martin](https://learning.oreilly.com/videos/clean-code/9780134661742/9780134661742-CODE_01_00_00)
* [isaak.dev - Python libraries to make your code readable, reliable and maintainable](https://isaak.dev/2020/08/python-libraries-to-make-your-code-readable-and-maintainable#code-style)
* [Opensourse - 7 Python libraries for more maintainable code](https://opensource.com/article/18/7/7-python-libraries-more-maintainable-code)
* [Real Python - Python Code Quality: Tools & Best Practices](https://realpython.com/python-code-quality/)
* [The Hitchhiker’s Guide to Python - Code Style](https://docs.python-guide.org/writing/style/)
