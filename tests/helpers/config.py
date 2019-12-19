from contextlib import contextmanager
from tigre import config


@contextmanager
def config_wrapper(attr, value):
    """Manage tigre.configuration side-effects."""
    initial_state = getattr(config, attr)
    setattr(config, attr, value)
    yield
    setattr(config, attr, initial_state)
