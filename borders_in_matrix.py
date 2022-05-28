from numpy import ones


def main_borders_in_matrix() -> None:
    """Create a matrix with a size 10x10 while its borders are equal to 1 and inside 0.

    Got help from: https://www.w3resource.com/python-exercises/numpy/python-numpy-exercise-8.php .
    :return: None.
    """
    matrix = ones((10, 10), dtype="int64")
    matrix[1: -1, 1: -1] = 0
    print(matrix)


if __name__ == '__main__':
    main_borders_in_matrix()
