from numpy import linspace


def main_evenly_distributed_vector() -> None:
    """Create a vector of length 10 with values evenly distributed between 5- 50.

    :return: None.
    """
    vector = linspace(5, 50, 10, dtype='int64')
    print(vector)


if __name__ == '__main__':
    main_evenly_distributed_vector()
