from typing import Dict

from attribute_set import AttributeSet
from categorical_attribute_set import CategoricalAttributeSet
from numeric_attribute_set import NumericAttributeSet


class Entry:
    attribute_sets: Dict[str, AttributeSet] = {}

    def __init__(self, labels, attributes):
        self.attributes = {}

        for attribute, value in zip(labels, attributes):
            if not isinstance(value, float) and len(value) == 0:
                continue

            self.attributes[attribute] = value

            if attribute in Entry.attribute_sets:
                Entry.attribute_sets[attribute].add_item(value)
            else:
                try:
                    float(value)
                    Entry.attribute_sets[attribute] = NumericAttributeSet()
                except ValueError:
                    Entry.attribute_sets[attribute] = CategoricalAttributeSet()

    def __str__(self):
        return "\n".join(f'{key}: {val}' for key, val in self.attributes.items())
