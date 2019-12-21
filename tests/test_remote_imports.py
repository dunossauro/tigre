from unittest import TestCase


class TestRemoteModuleImports(TestCase):
    def test_should_import_firefox(self):
        from tigre.remote import firefox

        self.assertEqual(firefox.capabilities, {'browserName': 'firefox'})

    def test_should_import_firefox_with_version_99(self):
        from tigre.remote import firefox99

        self.assertEqual(
            firefox99.capabilities, {'browserName': 'firefox', 'version': '99'}
        )

    def test_should_import_firefox_with_version_3(self):
        from tigre.remote import firefox3

        self.assertEqual(
            firefox3.capabilities, {'browserName': 'firefox', 'version': '3'}
        )

    def test_should_import_chome(self):
        from tigre.remote import chrome

        self.assertEqual(chrome.capabilities, {'browserName': 'chrome'})

    def test_should_import_opera(self):
        from tigre.remote import opera

        self.assertEqual(opera.capabilities, {'browserName': 'opera'})


    def test_should_import_safari(self):
        from tigre.remote import safari

        self.assertEqual(safari.capabilities, {'browserName': 'safari'})
