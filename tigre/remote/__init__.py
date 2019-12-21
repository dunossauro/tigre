from typing import Union
from tigre.core import Tigre
from importlib import import_module
from re import match, split

browsers_regex = r'(firefox|chrome|opera|safari)\d{,2}?'


def __getattr__(attr: str) -> Union[Tigre, ImportError]:
    if match(browsers_regex, attr):
        *_, browser, version = split(browsers_regex, attr)
        webdriver = import_module('tigre.remote.webdrivers')
        browser = getattr(webdriver, browser)
        return browser().version(version) if version else browser()

    raise ImportError(f"cannot import name '{attr}' from 'tigre.remote'")
