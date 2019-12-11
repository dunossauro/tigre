"""Tigre."""
from typing import Any, Callable, Union
from selenium import webdriver
from tigre.core.meta import Builder
from tigre.core.helpers import CAPATILITIES, attr_to_caps


class Tigre(Builder):
    def __init__(self, default_caps: list = CAPATILITIES):
        self.default_caps = default_caps
        self.caps = {}
        self.fixed_caps = {}

    @property
    def capabilities(self):
        return {**self.fixed_caps, **self.caps}

    def __getattr__(self, attr: Any) -> Union[Callable, AttributeError]:
        def dynamic_setter(value: Any):
            value = str(value) if not isinstance(value, bool) else value
            self.caps.update({converted_attr: value})
            return self

        converted_attr = attr_to_caps(attr)

        if converted_attr in self.fixed_caps:
            return self.fixed_caps[converted_attr]

        if converted_attr in self.default_caps:
            setattr(self, converted_attr, dynamic_setter)
            return dynamic_setter
        else:
            raise AttributeError(f'Method {attr} is not a valid capability')

    def build(self):
        """
        Build a remote selenium remote webdriver using maked capabilities.

        TODO: think about how to parameterize the URL
        """
        return webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub",
            desired_capabilities={**self.fixed_caps, **self.caps},
        )

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(caps={self.capabilities})'
