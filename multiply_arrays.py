from functools import partial
from numpy.random import randint
from nptyping import NDArray


def multiply_arrays(left_multiply_array: NDArray, right_multiply_array: NDArray) -> NDArray:
    """Multiply two arrays with the same size value by value.

    :param left_multiply_array: Any array.
    :param right_multiply_array: Any array with the same size as the first one.
    :return: Array with the result.
    """
    try:
        return left_multiply_array * right_multiply_array
    except ValueError:
        print("Different matrix size.")


def main_multiply_arrays() -> None:
    """Test on multiply_arrays function.

    :return: None.
    """
    random_matrix = partial(randint, 1, 5, (5, 5))
    first_matrix = random_matrix()
    second_matrix = random_matrix()
    print("First matrix =\n", first_matrix, "\n")
    print("Second matrix =\n", second_matrix, "\n")
    print("After multiply= \n", multiply_arrays(first_matrix, second_matrix))


if __name__ == '__main__':
    main_multiply_arrays()
