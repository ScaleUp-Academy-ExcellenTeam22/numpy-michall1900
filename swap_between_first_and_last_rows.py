from numpy import random


def main_swap_between_first_and_last_rows() -> None:
    """Create a matrix with size 4x4 and swap between the first and the last rows.
    return: None.
    """
    matrix = random.randint(0, 100, (4, 4))
    print("Matrix = \n", matrix)
    new_matrix = matrix.copy()
    new_matrix[[0, -1]] = new_matrix[[-1, 0]]
    print("New matrix =\n", new_matrix)
    print("Matrix = \n", matrix)


if __name__ == '__main__':
    main_swap_between_first_and_last_rows()
