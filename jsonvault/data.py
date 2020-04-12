from typing import Any


class Entry(object):

    def __init__(self, key: str, value: Any):
        """
        Class constructor

        :param key: Entry primary key
        :param value: Entry value
        """

        self.key = key
        self.value = value

    def __eq__(self, other: Any) -> bool:
        """
        Equality comparison operator

        :param other: Other entry.
        :return: True if both entries are equal, False otherwise.
        """

        return type(self) == type(other) and self.key == other.key and self.value == other.value
