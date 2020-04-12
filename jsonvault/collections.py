from typing import (
    List,
    Union
)

from jsonvault import data


class CollectionDefinition(object):

    def __init__(self, name: str, indexes: List[str] = None):
        """
        Class constructor

        :param name: Collection name
        :param indexes: Indexes definition
        """

        self.name = name
        self.indexes = indexes or []


class JsonCollection(object):

    def __init__(self, definition: CollectionDefinition):
        """
        Class constructor

        :arg definition: Collection name
        """

        self.definition = definition
        self._entries = dict()

    @property
    def name(self) -> str:
        """
        :return: Collection name
        """

        return self.definition.name

    def get(self, index: str) -> Union[data.Entry, None]:
        """
        Obtain an entry by key

        :param index: Entry key
        :return: The entry matching the index or None if not found.
        """

        if index not in self._entries:
            return None

        return data.Entry(index, self._entries[index])

    def put(self, entry: data.Entry):
        """
        Inserts an entry

        :param entry: Collection entry
        """

        self._entries[entry.key] = entry.value

    def delete(self, key: str):
        """
        Deletes an entry

        :param key: Key of the entry to delete
        """

        if key in self._entries:
            del self._entries[key]
