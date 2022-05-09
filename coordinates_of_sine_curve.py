from numpy import arange, pi, sin
from matplotlib import pyplot, style


def print_sine_curve_with_x_range(start_range: float = -4 * pi, end_range: float = 4 * pi, step: float = 0.1) -> None:
    """Get a range of x values, compute sin(x), set data, and plot the points.
    Got help from:
    https://www.w3resource.com/python-exercises/numpy/basic/numpy-basic-exercise-40.php
    :param start_range: Starting value to compute x.
    :param end_range: End value to compute x.
    :param step: Steps between start and end.
    :return: None.
    """
    sin_parameters_range = arange(start_range, end_range, step)
    sin_result = sin(sin_parameters_range)
    pyplot.plot(sin_parameters_range, sin_result)
    pyplot.show()


def main_coordinates_of_sine_curve() -> None:
    """Test print_sine_curve_with_x_range function.

    :return: None.
    """
    print_sine_curve_with_x_range(-3, 3, 0.05)


if __name__ == '__main__':
    main_coordinates_of_sine_curve()
