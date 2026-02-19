# My first package
This package can be installed via pip from a local copy of the source code.

# Building
- First, make sure you are in a virtual environment. If you're not, do the following: create and activate you venv by running the following commands on the root of the repository:
`python3.10 -m venv .venv`
`source .venv/bin/activate`

- Install the dependencies
`pip install -r requirements.txt`

- Now, on the directory ex09, build the package
`python -m build`

- Install from local source code or wheel file
`pip install ./dist/ft_package-0.0.1.tar.gz`
or
`pip install ./dist/ft_package-0.0.1-py3-none-any.whl`

- Inspect metadata via `pip show -v ft_package`

- Open an interactive Python session and type the test provided in the subject
