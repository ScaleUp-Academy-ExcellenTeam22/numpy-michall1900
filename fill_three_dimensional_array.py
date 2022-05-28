import numpy as np


def main_fill_three_dimensional_array() -> None:
    """ Create an array with a size of 300 x 400 x 5 and fill it with random unsigned int numbers.

    Got help from:
    https://www.w3resource.com/python-exercises/numpy/python-numpy-random-exercise-17.php
    :return: None.
    """
    my_array = np.random.randint(0, 256, (300, 400, 5), np.uint8)
    print(my_array)


if __name__ == '__main__':
    main_fill_three_dimensional_array()
