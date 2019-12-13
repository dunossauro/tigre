# Tigre

Tiger is a helper to instantiate your [selenium webdriver](https://selenium.dev/documentation/en/webdriver/) at the right time.

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
