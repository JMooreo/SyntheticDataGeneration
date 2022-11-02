from abc import abstractmethod
from typing import Any


class AttributeSet:
    def __init__(self):
        self.set = set()
        self.distribution_map = {}

    @abstractmethod
    def add_item(self, item) -> None:
        pass

    @abstractmethod
    def choose_random(self, n: int) -> Any:
        pass
