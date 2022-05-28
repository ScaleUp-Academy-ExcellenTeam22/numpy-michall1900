from numpy import arange


def main_vector_zero_to_twenty() -> None:
    """Create a vector with values in the range [0,20]. After that, turn the values [9-15] negative.

    :return: None.
    """
    vector = arange(21)
    vector[9:16] *= -1
    print(vector)


if __name__ == '__main__':
    main_vector_zero_to_twenty()
