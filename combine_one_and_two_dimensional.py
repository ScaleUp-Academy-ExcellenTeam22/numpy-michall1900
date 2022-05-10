from nptyping import NDArray, Shape
from typing import Any
from numpy import arange, nditer


def combine_one_and_two_dimensional(one_dimensional_array: NDArray[Shape[Any], Any],
                                    two_dimensional_array: NDArray[Shape[Any, Any], Any]) -> nditer:
    """Combine a one and a two-dimensional array and return an iterator to it.
    Got help from:
    https://www.geeksforgeeks.org/combining-a-one-and-a-two-dimensional-numpy-array/
    :param one_dimensional_array: One dimensional array
    :param two_dimensional_array: Two dimensional array.
    :return: A nditer.
    """
    try:
        return nditer([one_dimensional_array, two_dimensional_array])
    except ValueError as error:
        print(error)


def main_combine_one_and_two_dimensional() -> None:
    """Test combine_one_and_two_dimensional function with the example at the exercise.

    :return: None.
    """
    one_dimensional_array = arange(4)
    two_dimensional_array = arange(8).reshape(2, 4)
    print(f"One dimensional array:\n{one_dimensional_array}\n")
    print(f"Two dimensional array:\n{two_dimensional_array}\n")
    combined_array = combine_one_and_two_dimensional(one_dimensional_array, two_dimensional_array)
    if combined_array:
        for first_argument, second_argument in combined_array:
            print(f"{first_argument}: {second_argument}")


if __name__ == '__main__':
    main_combine_one_and_two_dimensional()
