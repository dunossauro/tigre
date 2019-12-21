# Development

If you like Tigre purpose and would like to contribute this page can help you.

Tigre supports only python 3.7+ and you need version 3.7+ to develop. We recommend that you use `Pyenv` to manage many Python environments. Basic instructions can be found below.

For development we recommend `Poetry` and configuration can be found below too.

To manipulate remote webdrivers, we have a `docker_test_image` on this repository, but we recommend `Selenoid` containers. They are more stable.

## Pyenv

#### Installing Pyenv

To install Pyenv, follow the [Pyenv repository](https://github.com/pyenv/pyenv) instructions to Unix-like, or [pyenv-win](https://github.com/pyenv-win/pyenv-win) to windows environments.

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

With Docker initialized you can follow one of these steps below.

### Running up Selenium Grid

Go to `docker_test_images` folder and using Docker and docker-compose you can run the test image with the following command:

    docker-compose -f docker-selenium-browsers.yaml up

Open a browser and go to `localhost:4444` to see if Selenium Grid Console is correctly up.

### Running up Selenoid

First, install Selenoid following the (oficial docs)[https://aerokube.com/selenoid/latest/].

After installing, run

    ./cm selenoid start --vnc

To use Selenoid UI, also run

    ./cm selenoid-ui start

Now, open a browser in `localhost:8080` and you'll see Selenoid UI.

### Running up Zalenium

Take a look at [Zalenium docs](https://github.com/zalando/zalenium) and install Zalenium.

However, to make you buy time, you'll only need run these three steps:

    # Pull docker-selenium
    docker pull elgalu/selenium

    # Pull Zalenium
    docker pull dosel/zalenium

    sudo docker run --rm -ti --name zalenium -p 4444:4444 \
        -v /var/run/docker.sock:/var/run/docker.sock \
        -v /tmp/videos:/home/seluser/videos \
        --privileged dosel/zalenium start

Now, proceed at `localhost:4444` and you'll see Selenium Grid Hub up.


## Registering a node into the hub

To register a node on selenium hub, you will need to download and install [Java
SE Development Kit](https://www.oracle.com/technetwork/java/javase/downloads/jdk13-downloads-5672538.html)

After installing Java SE you have to download [selenium-server-standalone](https://selenium.dev/downloads/) and move the file for the active working directory.

After that you need to have sure you're running the Selenium Hub on port 4444, and then run this command, it will register a node into your Selenium Hub:

```
java -jar selenium-server-standalone-<version>.jar -role node -hubHost localhost -hubPort 4444
```
