from unittest import TestCase
from tigre.remote.webdrivers import firefox, chrome, opera, safari


class TestFirefoxCapabilities(TestCase):
    def setUp(self):
        self.browser = firefox()

    def test_should_has_version_capability(self):
        self.assertEqual(self.browser.capabilities, {"browserName": "firefox"})


class TestOperaCapabilities(TestCase):
    def setUp(self):
        self.browser = opera()

    def test_should_has_version_capability(self):
        self.assertEqual(self.browser.capabilities, {"browserName": "opera"})


class TestChromeCapabilities(TestCase):
    def setUp(self):
        self.browser = chrome()

    def test_should_has_version_capability(self):
        self.assertEqual(self.browser.capabilities, {"browserName": "chrome"})


class TestSafariCapabilities(TestCase):
    def setUp(self):
        self.browser = safari()

    def test_should_has_version_capability(self):
        self.assertEqual(self.browser.capabilities, {"browserName": "safari"})
