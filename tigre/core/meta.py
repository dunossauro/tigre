from abc import abstractmethod, abstractproperty, ABC


class Builder(ABC):
    """Builder interface."""

    # @abstractproperty
    # def capabilities(self):
    #     ...

    @abstractmethod
    def build(self):
        """Build method should return a webdriver."""
        ...
