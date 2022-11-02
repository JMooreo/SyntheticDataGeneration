import numpy as np
from attribute_set import AttributeSet


class NumericAttributeSet(AttributeSet):

    def __init__(self):
        super().__init__()
        self.list = list()

    def __str__(self):
        stats = {
            "min": min(self.list),
            "max": max(self.list),
            "std_dev": np.std(self.list),
            "mean": np.mean(self.list)
        }
        return f"{stats}"

    def add_item(self, item):
        self.list.append(float(item))

    def choose_random(self, n):
        choices = np.random.normal(np.mean(self.list), np.std(self.list), n)
        return list(choices) if n > 1 else choices[0]
