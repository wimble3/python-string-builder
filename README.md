# StringBuilder #

## What is this? ##
StringBuilder is a data type that is used to work with variable length strings. It provides methods for adding, deleting, and replacing characters in a string without creating new String objects, which increases performance when working with large amounts of data.


## Installation ##

    pip install python-string-builder


## Quickstart ##
For using builder you should create StringBuilder instance and work with his public methods:


    builder = StringBuilder("This is first string")
    for i in range(10**5):
        builder.append("This is appended string")
    print(builder)
    builder.clear()


## Time tests ##
StringBuilder faster than other standard python variations of string concatenations (on a large number of concatenations).

This is table from quickstart example tests:

| Iterations num | StringBuilder         | '+=' operator        | str.join()            |
|----------------|-----------------------|----------------------|-----------------------|
| 10**1          | 0.0 (very fast)       | 0.0 (very fast)      | 0.0 (very fast)       |
| 10**2          | 0.0 (very fast)       | 0.0 (very fast)      | 0.0 (very fast)       |
| 10**3          | 0.0 (very fast)       | 0.0 (very fast)      | 0.0009987354278564453 |
| 10**4          | 0.0 (very fast)       | 0.002000093460083008 | 0.002001047134399414  |
| 10**5          | 0.006998538970947266  | 0.019001007080078125 | 0.021995067596435547  |
| 10**6          | 0.07500171661376953a  | 0.7380020618438721   | 0.21000170707702637   |



### Documentation ###
    def append(self, string: str) -> None:
        """Appends string to data list."""

    def insert(self, index: int, string: str, raise_ex: bool = True) -> None:
        """Inserts string by index to data list.

        Parameter raise_ex is responsible for whether to throw an exception
        in the case of IndexError or throw a warning.
        """

    def remove(self, index: int, raise_ex: bool = True):
        """Removes string by index from data list.

        Parameter raise_ex is responsible for whether to throw an exception
        in the case of IndexError or throw a warning.
        """

    def clear(self) -> None:
        """Clears data list.

        It is recommended to call each time a StringBuilder instance
        is no longer needed.
        """



## Developer ##
https://github.com/wimble3
