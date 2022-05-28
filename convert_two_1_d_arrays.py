from functools import partial
from numpy import dstack, random


def main_convert_two_1_d_arrays() -> None:
    """Makes two random 1-D arrays and converts them in sequence depth wise into a 2-D array.

    :return: None.
    """
    make_random_1_d_array = partial(random.randint, low=1, high=100, size=random.randint(1, 10))
    first_array = make_random_1_d_array()
    second_array = make_random_1_d_array()
    print(f"Original arrays:\n{first_array}\n{second_array}\n")
    print(dstack((first_array, second_array)))


if __name__ == '__main__':
    main_convert_two_1_d_arrays()
