"""
https://github.com/wimble3
python-string-builder library.
"""
from settings import TESTS_APPENDED_STRING, TESTS_FIRST_STRING

from string_builder import StringBuilder


def get_builder_string_example(iterations_num: int) -> StringBuilder:
    """Gets builder instance with test data."""
    builder: StringBuilder = StringBuilder(TESTS_FIRST_STRING)
    for _ in range(iterations_num):
        builder.append(TESTS_APPENDED_STRING)
    return builder


def get_plus_equal_string_example(iterations_num: int) -> str:
    """Gets string instance with test data.

    Using standard python case '+='.
    """
    string: str = TESTS_FIRST_STRING
    for _ in range(iterations_num):
        string += TESTS_APPENDED_STRING
    return string


def get_join_string_example(iterations_num: int) -> str:
    """Gets string instance with test data.

    Using standard python case with join() function.
    """
    string: str = TESTS_FIRST_STRING
    for _ in range(iterations_num):
        string.join(TESTS_APPENDED_STRING)
    return string
