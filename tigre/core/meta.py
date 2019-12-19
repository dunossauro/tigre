from abc import abstractmethod, ABC


class Builder(ABC):
    """Builder interface."""

    @abstractmethod
    def build(self):
        """Build method should return a webdriver."""
        ...
