from nptyping import NDArray
from numpy import argsort, array


class Student:
    """Class student.
    :param identifier: Student's id.
    :param height: Student's height.

    """

    def __init__(self, identifier:str, height: float):
        """Constructor
        """
        self.identifier = identifier
        self.height = height

    def __lt__(self, other: 'Student'):
        """Receive another student and return true if its height > current student.

        :param other: Other Student object.
        :return: True if left student's height < other student's height.
        """
        return self.height < other.height

    def __str__(self) -> str:
        """Return student's details (id : height)

        :return: Student's details.
        """
        return f"{self.identifier}: {self.height}\n"


def print_array_content(any_array: NDArray) -> None:
    """ Prints the array's content element by element.
    :param any_array: Array
    :return: None.
    """
    print("Content:")
    for element in any_array:
        print(element)


def main_increasing_height_order() -> None:
    """Sort student id with increasing height of the students from given students id and heights.
    After, print the integer indices that describe the sort order by multiple columns and the sorted data.
    :return: None.
    """
    students_list = [Student("1325", 182.5), Student("1367", 152), Student("1234", 168.7), Student("2345", 122.5)]
    my_array = array(students_list)
    print("Before sorting:\n")
    print_array_content(my_array)
    indices = argsort(my_array)
    my_array.sort()
    print("After sorting:\n")
    print(f"Indices:\n{indices}\n")
    print_array_content(my_array)


if __name__ == '__main__':
    main_increasing_height_order()
