import numpy as np
from matplotlib.pyplot import imsave


def main_french_flag() -> None:
    """Create an image of the french flag using NumPy.

    :return: None.
    """
    french_flag_array = np.ones((300, 600, 3))
    french_flag_array[0: 300, 0: 200] = [0, 0, 1]
    french_flag_array[0: 300, 400: 600] = [1, 0, 0]
    imsave("./french_flag.png", french_flag_array)


if __name__ == '__main__':
    main_french_flag()
