from tigre.core import Tigre


class chrome(Tigre):
    def __init__(self):
        super().__init__()
        self._fixed_caps = {"browserName": "chrome"}


class firefox(Tigre):
    def __init__(self):
        super().__init__()
        self._fixed_caps = {"browserName": "firefox"}


class opera(Tigre):
    def __init__(self):
        super().__init__()
        self._fixed_caps = {"browserName": "opera"}


class safari(Tigre):
    def __init__(self):
        super().__init__()
        self._fixed_caps = {"browserName": "safari"}
