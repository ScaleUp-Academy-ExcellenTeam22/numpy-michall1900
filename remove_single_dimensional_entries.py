from nptyping import NDArray
from numpy import random, squeeze


def remove_single_dimensional_entries(array: NDArray) -> NDArray:
    """Remove single-dimensional entries from a specified shape.

    :param array: Any kind of array.
    :return: Same array after removing single-dimensional entries.
    """
    return squeeze(array)


def main_remove_single_dimensional_entries() -> None:
    """Create a random array and remove from it single-dimensional entries.

    :return: None.
    """
    random_array = random.randint(0, 100, tuple([1, 5, 3, 1, 4]))
    print(f"Original array:\n{random_array}\n")
    print(f"Original shape: {random_array.shape}")
    new_array = remove_single_dimensional_entries(random_array)
    print(f"After remove single dimensional entries:\n{new_array}\n")
    print(f"New shape: {new_array.shape}")


if __name__ == '__main__':
    main_remove_single_dimensional_entries()
