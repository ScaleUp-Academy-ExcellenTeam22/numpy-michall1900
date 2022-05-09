from numpy import ones, zeros
from numpy.typing import ArrayLike, NDArray


def add_vector_to_matrix(vector: ArrayLike, matrix: NDArray) -> None:
    """Add a vector to each row of a given matrix. The vector's size must be equal to the row's length of the matrix.

    :param vector: Array with one row.
    :param matrix: Any kind of matrix.
    :return: None.
    """
    try:
        matrix += vector
    except ValueError:
        print("Different size of vector and matrix.")


def main_add_vector_to_matrix() -> None:
    """Builds matrix and vector and prints the result after using the add_vector_to_matrix function.

    :return: None.
    """
    my_matrix = zeros((2, 3))
    print("Before adding vector , matrix:\n", my_matrix)
    my_vector = ones(5)
    add_vector_to_matrix(my_vector, my_matrix)
    print("After adding vector , matrix:\n", my_matrix)


if __name__ == '__main__':
    main_add_vector_to_matrix()
