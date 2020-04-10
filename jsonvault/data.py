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
