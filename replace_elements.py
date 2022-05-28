from numpy import array
from nptyping import NDArray
from operator import eq, gt, lt
from typing import Literal


Operations = Literal["=", "<", ">"]


def replace_elements(matrix: NDArray, current_element: float, replace_to_element: float = 0,
                     operation: Operations = '=') -> NDArray:
    """Replace all numbers in a given array which are equal/ less/ greater (as a given operation) to a given number..

    :param matrix: Any kind of array/ matrix.
    :param current_element: The wanted element to replace.
    :param replace_to_element: The replacement element.
    :param operation: One of those strings "=", "<", ">".
    :return: Matrix after the replacing.
    """
    string_to_operator = {"=": eq, "<": lt, ">": gt}
    new_matrix = matrix.copy()
    new_matrix[string_to_operator[operation](new_matrix, current_element)] = replace_to_element
    return new_matrix


def main_replace_elements() -> None:
    """Test replace elements function.

    :return: None.
    """
    my_array = array([[1, -0.3, 5, 9], [3, 6, 18, 1], [5, 3, 17.9, 101]])
    print("Original array =\n", my_array, "\n")
    print("Replace all numbers that equal to 3 to 10:\n", replace_elements(my_array, 3, 10), "\n")
    print("Replace all numbers that less than 15 to 0:\n", replace_elements(my_array, 15, 0, "<"), "\n")
    print("Replace all numbers that bigger than 15 to 0:\n", replace_elements(my_array, 15, 0, ">"), "\n")


if __name__ == '__main__':
    main_replace_elements()
