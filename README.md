# check-python-static-code-analysis

Check if different code analysis tools can detect ugly code in Python

## My Main Goals

Example code is working, but is not very readable. I am looking for a tool or set of
tools that will show me:

* how unreadable the code is
* some kind of code readability score that can be used in CI to block PRs
* what parts of the code need refactoring
* refactoring suggestions

## Optional Goals

* Find code formatters that can fix code readability
* Measure analysis time

## Out of scope

* Test coverage
* Test security

## Plan

1. Collect the list of code analysers
1. Run multiple code analysers and collect results

## The List

**Analysers:** (some of them are known as linters)

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
* [code_quality](https://github.com/ArthDubey/code_quality)

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

1. Quick check that at least one goal is met. 
2. No extra setup and config files will be created.
3. Mark tools that failed all goals as :x: in **Interim Summary**.
4. Mark tools that meet at least one goal as :white_check_mark: 
   in **Interim Summary**.

More details can be found [here](./ROUND_1_REASEARCH.md)

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
| Radon | :white_check_mark: | Meets readability score goal |
| wemake-python-styleguide | :raised_eyebrow: | Is Flake8 plugin |
| code_quality | :white_check_mark: | Finally something close to my goals |
| **Formatters** |
| Autopep8 | :x: | Does not meet my goals |
| Black | :white_check_mark: | 1 timer!? |
| Isort | :white_check_mark: | Make imports more readable |
| Yapf | :x: | Does not meet my goals |
| **Packages** |
| Flake8 | :x: | Does not meet my goals |
| flakehell | :x: | Fails to run |
| hacking | :x: | Failed to install |
| Pylama | :x: | Does not meet my goals |
| SonarQube | :x: | Does not meet my goals |

## Second round

1. Filter out duplicate tools if any.
1. Come up with the approach of using tools in CI/CD 
   to improve code readability over time.

More details can be found [here](./ROUND_2_REASEARCH.md)

## My final summary

### List of tools

| Name | Status | Comments |
|------|--------|----------|
| **Analysers** |
| Pylint | :grey_question: | Meets naming goal |
| Radon | :grey_question: | Meets readability score goal |
| wemake-python-styleguide | :grey_question: | Is Flake8 plugin |
| code_quality | :grey_question: | Finally something close to my goals |
| **Formatters** |
| Black | :grey_question: | 1 timer!? |
| Isort | :grey_question: | Make imports more readable |

### Steps to take

TBD

## References

* [Clean Code videos by Robert C. Martin](https://learning.oreilly.com/videos/clean-code/9780134661742/9780134661742-CODE_01_00_00)
* [isaak.dev - Python libraries to make your code readable, reliable and maintainable](https://isaak.dev/2020/08/python-libraries-to-make-your-code-readable-and-maintainable#code-style)
* [Opensourse - 7 Python libraries for more maintainable code](https://opensource.com/article/18/7/7-python-libraries-more-maintainable-code)
* [PyCQA - Organization for code quality tools (and plugins) for the Python programming language](https://github.com/PyCQA)
* [Real Python - Python Code Quality: Tools & Best Practices](https://realpython.com/python-code-quality/)
* [The Hitchhiker’s Guide to Python - Code Style](https://docs.python-guide.org/writing/style/)
