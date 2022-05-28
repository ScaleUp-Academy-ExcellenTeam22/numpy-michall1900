from numpy import identity


def ones_on_a_diagonal() -> None:
    """Create and print 3-D matrix with ones on a diagonal and zeros elsewhere.

    :return: None.
    """
    matrix = identity(3)
    print(matrix)


if __name__ == '__main__':
    ones_on_a_diagonal()