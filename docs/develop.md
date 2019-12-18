# development

If you like Tigre purpose and would like to contribute this page can help you.

Tigre support only python3.7+ and you need version 3.7+ to develop. We recommend that you use `Pyenv` to manage many python enviroments. Basic instructions can be found below.

For develop we recommend `Poetry` and configuration can be found below too.

To manipulate remote webdrivers, we has a `docker_test_image` on own reporsitory, but we recommends `Selenoid` containers. Are more stable

## Pyenv

#### Installing Pyenv

To install Pyenv, follow the [Pyenv repository](https://github.com/pyenv/pyenv) instructions to Unix-like, or [pyenv-win](https://github.com/pyenv-win/pyenv-win) to windows enviroments.

After installing, run this to check if it's all correctly done:

    pyenv --version

#### Setting Pyenv

Install any Python version above 3.7. You can list available Pyenv Python versions using

    pyenv install -l

For example, to install Python 3.8.0

    pyenv install 3.8.0

Now, set chosen version in root directory as Python local version

    pyenv local 3.8.0


## Poetry

#### Installing Poetry

You'll need Poetry to create your development's environment.

To install Poetry, follow the [Poetry docs](https://python-poetry.org/docs/).

In order to check if it's all clear, run this

    poetry --version

#### Setting up the development environment

Clone this repository and in root directory run

    poetry update

This command will install (or update) all pyproject.toml dependencies inside a virtual environment.


## Docker environment

### Running up Selenium Grid using Docker and docker-compose

Go to `docker_test_images` folder and using Docker and docker-compose you can run the test image with the following command:

    docker-compose -f docker-selenium-browsers.yaml up

Open a browser and go to `localhost:4444` to see if Selenium Grid Console is correctly up.
