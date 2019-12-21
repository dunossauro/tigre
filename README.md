# Tigre  :tiger:

Tigre is a helper to instantiate your [selenium webdriver](https://selenium.dev/documentation/en/webdriver/) at the right time.

## Motivation

[Python selenium](https://selenium-python.readthedocs.io) provides some alternatives for you to call your browser, but if you want to use a [remote browser](https://selenium-python.readthedocs.io/getting-started.html#selenium-remote-webdriver),  you will have to configure a lot of [capabilities](https://selenium-python.readthedocs.io/api.html#desired-capabilities). Tigre's main idea is to make it easier to use remote browsers, such as the use in grids [grids](https://selenium.dev/documentation/en/grid/), in [load balancers](https://aerokube.com/ggr/latest/), in [mobile automation](https://pypi.org/project/Appium-Python-Client/) or even using [docker images](https://aerokube.com/selenoid/).


## Tested on

- [docker-selenium](https://github.com/SeleniumHQ/docker-selenium)
  - grid ([see file](./docker_test_images))
    - chrome
    - firefox
  - stadalone
    - chrome (standalone-chrome:3.141.59-xenon)
    - firefox (selenium/standalone-firefox:3.141.59-xenon)

- [selenoid](https://aerokube.com/selenoid/latest/)
  - grid (by cm)
    - chrome
    - firefox
    - opera


## Not tested yet
- [docker-android](https://github.com/budtmo/docker-android)
  - grid
  - standalone


## TODO

- Grid tools
  - [x] standalone
  - [x] docker-selenium
  - [x] selenoid
  - [x] zalenium
  - [ ] Authentication :fire:

- Webdriver features
  - [x] Remote webdrivers
  - [ ] Local webdrivers
  - [ ] Android webdrivers
  - [ ] iOS webdrivers
  - [ ] Test using paid tools (EX: SauceLabs)

- Continuous integration stuff
  - [ ] Python 3.7
  - [ ] Python 3.8
  - [ ] Docker integration

- Documentation
  - [ ] Start mkdocs

- more a lot of things

## Simple example

example using remote webdriver.

```python
>>> from tigre.remote import firefox

# complex definition enabling vnc and video recorder on firefox 70.0
>>> ff = firefox.version(70.0).vnc(True).resolution('800x600').video(True).build()
<selenium.webdriver.remote.webdriver.WebDriver (session="38f70e50-6009-4623-8969-34a9331ebf0a")>

>>> ff.capabilities
{'browserName': 'firefox', 'version': '70.0', 'enableVNC': True, 'screenResolution': '800x600', 'enableVideo': True}
```

## Dynamic importing example
```python
>>> from tigre.remote import firefox70

# complex definition enabling vnc and video recorder on firefox 70.0
>>> ff = firefox.vnc(True).resolution('800x600').video(True)
ff.capabilities
{'browserName': 'firefox', 'version': '70', 'enableVNC': True, 'screenResolution': '800x600', 'enableVideo': True}
```
