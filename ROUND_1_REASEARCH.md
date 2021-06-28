# Round 1 research

Steps taken to make initial comparison of tools

[Link to main README](https://github.com/alex-d-bondarev/check-python-static-code-analysis#first-round-summary)

## Analysers

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

## Formatters

### Autopep8

Did small changes to code. Pycharm provides more options. 
Need to specify each file separately.Tried like:

Tried like:
```shell
pipenv run autopep8 --in-place ./app/examples/real_python.py
```

### Black

"Blackened code looks the same regardless of the project you're reading."
Has a specific formatting approach. 
I liked some changes and did not like others. 
Not my style, but may be helpful to run one time in legacy projects,
and fix ugly code. 

Tried like:
```shell
pipenv run black ./app/
```

### Isort

Sort imports alphabetically, and automatically separated into sections and by type.
I like the way it organises imports.

Tried like:
```shell
pipenv run black ./app/
```

### Yapf

"Reformats code to the best formatting that conforms to the ... 
'clang-format', developed by Daniel Jasper". Looks similar to PyCharm for me.

Tried like:
```shell
pipenv run yapf -r -i ./app
```

## Packages

### Flake8

"Your Tool For Style Guide Enforcement".
IMHO some warnings were irrelevant. 
PyCharm shows more helpful information about warnings that are relevant to 
my goals. 

Tried like:
```shell
 pipenv run flake8 --benchmark --statistics -v ./app/ --output-file=flake8.log
```

## Main README

[Link to main README](https://github.com/alex-d-bondarev/check-python-static-code-analysis#first-round-summary)
