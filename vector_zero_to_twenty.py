from numpy import array


def main_vector_zero_to_twenty() -> None:
    """Create a vector with values in range [0,20]. After it, turn the values in the range [9-15] to negative once.

    :return: None.
    """
    vector = array(range(21))
    vector[9:16] *= -1
    print(vector)


if __name__ == '__main__':
    main_vector_zero_to_twenty()
