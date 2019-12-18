# Tigre

Tigre was born to ease the confusing calls of selenium webdriver.

If you have problems with different APIs for calling remote, local or mobile browsers. If you are confused by so many different capabilities settings or have trouble with hard-to-maintain code. Tigre was designed especially for you.

## Get started

### Tigre installation

Tigre is supported by Python versions above 3.7. You can use Pyenv to help you create a Python 3.7+ version isolated from your Python global version.

#### Installing Pyenv

To install Pyenv, follow the [Pyenv repository](https://github.com/pyenv/pyenv) instructions.

After installing, run this to check if it's all correctly done:

    pyenv --version

#### Setting Pyenv

Install any Python version above 3.7. You can list available Pyenv Python versions using

    pyenv install -l

For example, to install Python 3.8.0

    pyenv install 3.8.0

Now, set chosen version in root directory as Python local version

    pyenv local 3.8.0

#### Installing Poetry

You'll need Poetry to create your development's environment.

To install Poetry, follow the [Poetry docs](https://python-poetry.org/docs/).

In order to check if it's all clear, run this

    poetry --version

#### Setting up the development environment

Clone this repository and in root directory run

    poetry update

This command will install (or update) all pyproject.toml dependencies inside a virtual environment.

### Running up Selenium Grid using Docker and docker-compose

Go to `docker_test_images` folder and using Docker and docker-compose you can run the test image with the following command:

    docker-compose -f docker-selenium-browsers.yaml up

Open a browser and go to `localhost:4444` to see if Selenium Grid Console is correctly up.

#### Definition enabling vnc and video recorder on firefox

```Python
>>> from tigre.remote import firefox

>>> ff = firefox.version(70.0).vnc(True).resolution('800x600').video(True).build()
<selenium.webdriver.remote.webdriver.WebDriver (session="38f70e50-6009-4623-8969-34a9331ebf0a")>

>>> ff.capabilities
{'browserName': 'firefox', 'version': '70.0', 'enableVNC': True, 'screenResolution': '800x600', 'enableVideo': True}
```

<details markdown="1">
<summary>Or import expecific version...</summary>

You can call directly what version you want <code>firefox70</code>

```python hl_lines="1 5"
>>> from tigre.remote import firefox70

>>> ff = firefox.vnc(True).resolution('800x600').video(True)
ff.capabilities
{'browserName': 'firefox', 'version': '70', 'enableVNC': True, 'screenResolution': '800x600', 'enableVideo': True}
```

</details>
