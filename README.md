# check-python-static-code-analysis

Check if different code analysis tools can detect ugly code in Python

## Goals

Example code is working, but is not very readable. I am looking for a tool or set of
tools that will show me:

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
* [MyPy](https://mypy.readthedocs.io/en/stable/getting_started.html)
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
* [flakehell](https://wemake-python-stylegui.de/en/latest/pages/usage/integrations/flakehell.html#flakehell)
* [hacking](https://pypi.org/project/hacking/)
* [Pylama](https://github.com/klen/pylama)
* [SonarQube](https://www.sonarqube.org/features/multi-languages/python/)

## How to set up

1. Checkout this repository.
1. Ensure that you have installed the following:
    1. [pyenv](https://github.com/pyenv/pyenv). It will help to manage python version
       automatically.
    1. [pipenv](https://pypi.org/project/pipenv/)
       It will manage python dependencies and python version.
1. Run `PIPENV_YES=true pipenv install --ignore-pipfile`

## First round

Quick check that at least one goal is met.
Mark tools that failed all goals as :x: in **Interim Summary**.
Mark tools that meet at least one goal as :white_check_mark: in **Interim Summary**.

### Bandit

Run as `pipenv run bandit -r ./app`. Covers only security issues. Out of scope.

### McCabe

Check McCabe complexity. Did not show anything in a standalone mode. Does not meet my
goals.

Tried like:

```shell
pipenv shell
cd app/examples
python -m real_python --min 1 real_python.py
```

### MyPy

Check optional static types. It has failed to check imports from main.py like:
`main.py:3: error: Cannot find implementation or library stub for module named "examples.simple_calculator"`  
Does not meet my goals.

Tried like:

```shell
pipenv run mypy ./app 
pipenv shell
cd app/exmples
mypy simple_calculator.py 
```

### pep8

Looks like it is outdated. Here is an output that I received:

> pep8 has been renamed to pycodestyle (GitHub issue #466)  
> Use of the pep8 tool will be removed in a future release.  
> Please install and use `pycodestyle` instead.

Tried like:

```shell
pipenv run pep8 ./app
```

### pycodestyle

Check code against some of the style conventions in PEP 8.  
It highlighted some "space" errors. Does not meet my goals.

Tried like:

```shell
pipenv run pycodestyle ./app
```

### PyFlakes

Check Python source files for errors. Does not meet my goals.

Tried like:

```shell
pipenv run python -m pyflakes ./app/
```

### Pylint

Check some pep8 style rules

Tried like:

```shell
pipenv run pylint ./app/
```

### Radon

Show code complexity.

Tried like:

```shell
pipenv run radon cc ./app/
pipenv run radon raw ./app/
pipenv run radon mi ./app/
pipenv run radon hal ./app/
```

### wemake-python-styleguide

The "strictest and most opinionated python linter". The README looks interesting.
Could not find how to run separately. Is designed as flake8 plugin.

Tried like:

```shell
pipenv run wemake-python-styleguide ./app/
```

### Interim Summary

| Name | Status | Comments |
|------|--------|----------|
| **Analysers** |
| Bandit | :x: | Out of Scope |
| Mccabe | :x: | Does not meet my goals |
| MyPy | :x: | Does not meet my goals |
| pep8 | :x: | Outdated |
| pycodestyle | :x: | Does not meet my goals |
| PyFlakes | :x: | Does not meet my goals |
| Pylint | :white_check_mark: | Meets naming goal |
| Radon | :white_check_mark: | Code complexity goal |
| wemake-python-styleguide | :raised_eyebrow: | Is Flake8 plugin |
| **Formatters:** |
| Autopep8 | :grey_question: | TBD |
| Black | :grey_question: | TBD |
| Isort | :grey_question: | TBD |
| Yapf | :grey_question: | TBD |
| **Packages** |
| Flake8 | :grey_question: | TBD |
| flakehell | :grey_question: | TBD |
| hacking | :grey_question: | TBD |
| Pylama | :grey_question: | TBD |
| SonarQube | :grey_question: | TBD |

## My Conclusions

TBD

## References

* [Clean Code videos by Robert C. Martin](https://learning.oreilly.com/videos/clean-code/9780134661742/9780134661742-CODE_01_00_00)
* [isaak.dev - Python libraries to make your code readable, reliable and maintainable](https://isaak.dev/2020/08/python-libraries-to-make-your-code-readable-and-maintainable#code-style)
* [Opensourse - 7 Python libraries for more maintainable code](https://opensource.com/article/18/7/7-python-libraries-more-maintainable-code)
* [Real Python - Python Code Quality: Tools & Best Practices](https://realpython.com/python-code-quality/)
* [The Hitchhiker’s Guide to Python - Code Style](https://docs.python-guide.org/writing/style/)
