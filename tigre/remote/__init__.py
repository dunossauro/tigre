from typing import Union
from tigre.core import Tigre
from importlib import import_module
from re import match, split


def __getattr__(attr: str) -> Union[Tigre, ImportError]:
    if match(r'(firefox|chrome)\d{,3}?', attr):
        *_, browser, version = split(r'^(firefox|chrome|opera)\d{,2}?', attr)
        webdriver = import_module('tigre.remote.webdrivers')
        browser = getattr(webdriver, browser)
        return browser().version(version) if version else browser()

    raise ImportError(f"cannot import name '{attr}' from 'tigre.remote'")
