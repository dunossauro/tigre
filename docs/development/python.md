# Python environment

## [Pyenv](#pyenv)

#### [Installing Pyenv](#installing-pyenv)

To install Pyenv, follow the [Pyenv repository](https://github.com/pyenv/pyenv) instructions to Unix-like, or [pyenv-win](https://github.com/pyenv-win/pyenv-win) to windows environments.

After installing, run this to check if it's all correctly done:

    pyenv --version

#### [Setting Pyenv](#setting-pyenv)

Install any Python version above 3.7. You can list available Pyenv Python versions using

    pyenv install -l

For example, to install Python 3.8.0

    pyenv install 3.8.0

Now, set chosen version in root directory as Python local version

    pyenv local 3.8.0


## [Poetry](#poetry)

#### [Installing Poetry](#installing-poetry)

You'll need Poetry to create your development's environment.

To install Poetry, follow the [Poetry docs](https://python-poetry.org/docs/).

In order to check if it's all clear, run this

    poetry --version

#### [Setting up the development environment](#setting-up-the-development-environment)

Clone this repository and in root directory run

    poetry update

This command will install (or update) all pyproject.toml dependencies inside a virtual environment.


## [Tox](#tox)
