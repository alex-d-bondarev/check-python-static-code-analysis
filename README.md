# check-python-static-code-analysis
Check if different code analysis tools can detect ugly code in Python

## Goal

Example code is working, but is not very readable. 
I am looking for a tool or set of tools that will show me:
* how unreadable the code is
* some kind of code readability score that can be used in CI to block PRs
* what parts of the code need refactoring
* refactoring suggestions

## Optional Goal

* Find code formatters that can fix code readability
* Measure analysis time

## Plan

1. Collect the list of code analysers
1. Run multiple code analysers and collect results

## The List _WIP_

**Analysers:**
* [Bandit](https://github.com/PyCQA/bandit)
* [Mccabe](https://github.com/PyCQA/mccabe)
* [MyPy](http://mypy-lang.org/)
* [pep8](https://pypi.org/project/pep8/)
* [pycodestyle](https://github.com/PyCQA/pycodestyle)
* [pydocstyle](https://github.com/PyCQA/pydocstyle)
* [PyFlakes](https://github.com/PyCQA/pyflakes)
* [Pylint](https://www.pylint.org/)
* [Radon](http://radon.readthedocs.io/en/latest/)

**Formatters:**
* [Black](https://github.com/ambv/black)
* [Isort](https://github.com/timothycrosley/isort)

**Packages** (contain 2 or more analysers and probably formatters):
* [Flake8](https://flake8.pycqa.org/en/latest/)
* [hacking](https://pypi.org/project/hacking/)
* [Pylama](https://github.com/klen/pylama)

## Results

## My Conclusions

## References
* [Clean Code videos by Robert C. Martin](https://learning.oreilly.com/videos/clean-code/9780134661742/9780134661742-CODE_01_00_00)
* [Real Python - Python Code Quality: Tools & Best Practices](https://realpython.com/python-code-quality/)
* [The Hitchhiker’s Guide to Python - Code Style](https://docs.python-guide.org/writing/style/)
