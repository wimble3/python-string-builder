"""
https://github.com/wimble3
python-string-builder library.
"""
from unittest import TestCase

from string_builder import StringBuilder


class StringBuilderTest(TestCase):
    """Test case for StringBuilder class methods."""
    def test_append(self) -> None:
        """Tests append method."""
        builder: StringBuilder = StringBuilder()
        for _ in range(2):
            builder.append("test")
        self.assertEqual(str(builder), "testtest")
        builder.clear()

    def test_insert(self):
        """Tests insert method."""
        builder: StringBuilder = StringBuilder("test ")
        builder.insert(1, "test1 ")
        builder.insert(1, "test2 ")
        self.assertEqual(str(builder), "test test2 test1 ")
        builder.clear()

    def test_remove(self):
        """Tests remove method."""
        builder: StringBuilder = StringBuilder("Test string")
        builder.append(" ")
        builder.append("something")
        builder.append(" ")
        builder.append("last")
        builder.remove(-1)
        builder.remove(-1)
        self.assertEqual(str(builder), "Test string something")

        try:
            builder.remove(100)
        except IndexError:
            self.assertEqual(str(builder), "Test string something")
        builder.clear()

    def test_clear(self):
        """Tests clear method."""
        builder: StringBuilder = StringBuilder("Test string")
        builder.clear()
        self.assertEqual(str(builder), "")
