"""Tigre."""
from typing import Any, Callable, Union, Dict
from selenium import webdriver
from tigre.core import config
from tigre.core.meta import Builder
from tigre.core.helpers import CAPABILITIES, attr_to_caps


class Tigre(Builder):
    """Tigre base class."""
    def __init__(self, default_caps: list = CAPABILITIES):
        self._default_caps = default_caps
        self._caps = {}
        self._fixed_caps = {}

    @property
    def capabilities(self):
        return {**self._fixed_caps, **self._caps}

    def __getattr__(self, attr: Any) -> Union[Callable, AttributeError]:
        def dynamic_setter(value: Any):
            value = str(value) if not isinstance(value, bool) else value
            self._caps.update({converted_attr: value})
            return self

        converted_attr = attr_to_caps(attr)

        if converted_attr in self._fixed_caps:
            return self._fixed_caps[converted_attr]

        if converted_attr in self._default_caps:
            setattr(self, converted_attr, dynamic_setter)
            return dynamic_setter
        else:
            raise AttributeError(f'Method {attr} is not a valid capability')

    def build(self):
        """
        Build a remote selenium remote webdriver using maked capabilities.

        # NOTE: to set correct command_executor you can use config, like

        >>> from tigre import config
        >>> config.remote_url = 'my_remote_grid_url'
        """
        return webdriver.Remote(
            command_executor=config.remote_url,
            desired_capabilities={**self._fixed_caps, **self._caps},
        )

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(caps={self.capabilities})'
