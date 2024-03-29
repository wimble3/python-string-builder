"""
https://github.com/wimble3
python-string-builder library.
"""
from time import time
from unittest import TestCase

from settings import TESTS_ITERATIONS_NUM_LIST

from tests.helpers import (
    get_builder_string_example,
    get_join_string_example,
    get_plus_equal_string_example
)


class TimeTest(TestCase):
    """Test case for time optimization."""
    def test_time(self) -> None:
        """Tests time optimization.

        StringBuilder must be faster than other standard
        python variations of string concatenations
        (on a large number of concatenations).
        """
        for iteration_num in TESTS_ITERATIONS_NUM_LIST:
            time0 = time()
            get_builder_string_example(iteration_num)
            builder_time_delta = time() - time0

            time0 = time()
            get_plus_equal_string_example(iteration_num)
            plus_equal_time_delta = time() - time0

            time0 = time()
            get_join_string_example(iteration_num)
            join_time_delta = time() - time0

            self.assertLess(builder_time_delta, plus_equal_time_delta)
            self.assertLess(builder_time_delta, join_time_delta)
