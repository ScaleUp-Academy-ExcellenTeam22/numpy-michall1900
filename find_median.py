from numpy import median, random


def main_find_median() -> None:
    """Creates a random array and prints its median value.

    :return: None.
    """
    random_array = random.randint(0, 100, tuple(random.randint(1, 10) for _i in range(1, random.randint(2, 5))))
    print(f"Array:\n{random_array}\n\nMedian={median(random_array)}")


if __name__ == '__main__':
    main_find_median()
