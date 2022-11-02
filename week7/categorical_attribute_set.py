from typing import Any

import numpy as np

from attribute_set import AttributeSet


class CategoricalAttributeSet(AttributeSet):
    def __str__(self):
        return f"{self.set}"

    def add_item(self, item):
        self.set.add(item)
        if item in self.distribution_map:
            self.distribution_map[item] = self.distribution_map[item] + 1
        else:
            self.distribution_map[item] = 0

    def choose_random(self, n: int) -> Any:
        choices = np.random.choice(list(self.set), n)
        return list(choices) if n > 1 else choices[0]
