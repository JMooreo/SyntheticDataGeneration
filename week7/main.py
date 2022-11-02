import csv
import random
import sys

import numpy as np
from numpy.random import MT19937
from numpy.random import RandomState

from entry import Entry

def split_dataset_into_train_test():
    rs = RandomState(42)
    random.seed(42)
    num_rows = 8419
    row_index_options = range(num_rows)
    test_row_indexes = [rs.choice(row_index_options, replace=False) for _ in range(int(num_rows * 0.25))]
    directory = "C:/Users/Justi/Programming/CI491/datasets"

    with open(f"{directory}/mushroom-expanded.csv") as full_dataset:
        with open("mushroom_test.csv", "w", newline='') as mush_test:
            with open("mushroom_train.csv", "w", newline='') as mush_train:
                reader = csv.reader(full_dataset, delimiter=",")
                headers = next(reader)
                train_writer = csv.writer(mush_train, delimiter=",")
                test_writer = csv.writer(mush_test, delimiter=",")

                train_writer.writerow(["MSID"] + headers)
                test_writer.writerow(["MSID"] + headers)

                for index, line in enumerate(reader):
                    if index in test_row_indexes:
                        test_writer.writerow([index] + line)
                    else:
                        train_writer.writerow([index] + line)


def main():
    label_map = {
        # "target-label": "Edibility",
        "cap-shape": "Shape",
        "cap-surface": "Surface",
        "cap-color": "Color",
        # "bruises": "Bruises",
        # "odor": "Odor",
        # "gill-attachment": "Attachment",
        # "gill-spacing": "Spacing",
        # "gill-size": "Size",
        "gill-color": "Color",
        "stalk-shape": "Shape",
        # "stalk-root": "Root",
        "stalk-surface-above-ring": "Surface",
        "stalk-surface-below-ring": "Surface",
        "stalk-color-above-ring": "Color",
        "stalk-color-below-ring": "Color",
        # "veil-type": "VeilType",
        "veil-color": "Color",
        # "ring-number": "Count",
        # "ring-type": "RingType",
        "spore-print-color": "Color",
        # "population": "Grouping",
        # "habitat": "Habitat"
    }

    row_label = "Mushroom"
    missing_data = "?"

    # Register all the entries so we can look at all the categories
    with open("mushroom_train.csv") as f:
        reader = csv.reader(f, delimiter=",")
        headers = next(reader)

        for line in reader:
            Entry(headers, line)

    with open("random_mushrooms_train.txt", "w") as f:
        with open("mushroom_train.csv") as mush_train:
            reader = csv.reader(mush_train, delimiter=",")
            headers = next(reader)

            for line in reader:
                mush_id = line[0]

                for index, attribute in enumerate(headers):

                    # Skip the ID
                    if index == 0:
                        continue

                    random_value = Entry.attribute_sets[attribute].choose_random(1)
                    head = f"\"{row_label}:{mush_id}\""
                    relation = f"\"{attribute}\""
                    abstract_label = label_map.get(attribute, attribute)
                    tail = f"\"{abstract_label}:{random_value}\""

                    if random_value != missing_data:
                        f.write(f"g.triple(head = {head}, relation = {relation}, tail = {tail})\n")

                f.write("\n")


if __name__ == "__main__":
    main()
