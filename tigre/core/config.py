"""
Enviroments variables to make configuration more simple.

>>> from tigre import config

>>> config.remote_url = "http://localhost:4444/wd/hub"
"""
from os import environ


def env(key, config=None):
    """Get enviroment variables."""
    return environ.get(key, config)


remote_url = env('TIGRE_REMOTE_URL', 'http://localhost:4444/wd/hub')
