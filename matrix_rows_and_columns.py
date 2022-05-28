from nptyping import NDArray
from numpy.random import randint
from typing import Tuple


def matrix_rows_and_columns_number(any_matrix: NDArray) -> Tuple[int, int]:
    """Return the number of rows and columns of any kind of a given matrix.

    :param any_matrix: Any kind of matrix.
    :return: A tuple, while its first value is the rows' number and its second value is the columns' number.
    """
    shapes = any_matrix.shape
    # If the given matrix is a one-dimensional array, the number of rows is 1.
    # If the given matrix is empty, return (0, 0).
    return shapes[-2:] if len(shapes) >= 2 else (1, shapes[0]) if len(shapes) == 1 else (0, 0)


def main_matrix_rows_and_columns() -> None:
    """Creates a random matrix with integer values and calculates its rows' and columns' numbers.

    return: None.
    """
    random_matrix = randint(0, 100, tuple(randint(1, 10) for _i in range(1, randint(2, 5))))
    print(random_matrix, "\n")
    my_rows_and_columns = matrix_rows_and_columns_number(random_matrix)
    print(f"Rows = {my_rows_and_columns[0]}.\nColumns = {my_rows_and_columns[1]}.")


if __name__ == '__main__':
    main_matrix_rows_and_columns()
