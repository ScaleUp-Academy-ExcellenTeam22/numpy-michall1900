from numpy import random


def main_sort_array() -> None:
    """Sort along with the first and the last axis of a random array.

    :return: None.
    """
    random_array = random.randint(0, 100, tuple(random.randint(1, 10) for _i in range(1, random.randint(2, 5))))
    print(f"Original array:\n{random_array}\n")
    random_array.sort(axis=0)
    print(f"Sort along the first axis:\n{random_array}\n")
    random_array.sort(axis=-1)
    print(f"Sort along the last axis:\n{random_array}\n")


if __name__ == '__main__':
    main_sort_array()
