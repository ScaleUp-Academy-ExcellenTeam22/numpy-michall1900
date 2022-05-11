import numpy as np


def compute_days(year: str, month: str) -> np.datetime64:
    """Return the number of days (in np.datetime64 object) of a specific month and year.

    Note: The month's template should be a string with two characters (between 01 to 12).
    Got help from:
    https://www.geeksforgeeks.org/count-the-number-of-days-of-a-specific-month-using-numpy/
    :param year: Year's string.
    :param month: Month string with two characters between 01 to 12.
    :return: The number of days of a specific month and year.
    """
    end_month = str(int(month) + 1) if month != '12' else '1'
    end_year = year if month != '12' else str(int(year) + 1)

    if len(end_month) == 1:
        end_month = '0' + end_month

    return np.datetime64(end_year + '-' + end_month + '-01') - np.datetime64(year + '-' + month + '-01')


def main_count_number_of_days() -> None:
    """Test compute days.

    :return:None.
    """
    print(f"Number of days, February, 2016:\n{compute_days('2016', '02')}")
    print(f"Number of days, February, 2017:\n{compute_days('2017', '02')}")
    print(f"Number of days, February, 2018:\n{compute_days('2018', '02')}")


if __name__ == '__main__':
    main_count_number_of_days()
