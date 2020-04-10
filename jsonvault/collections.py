from typing import List

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
        self._layers = dict()

    @property
    def name(self) -> str:
        """
        :return: Collection name
        """

        return self.definition.name

    def get(self, index: str) -> data.Entry:
        """
        Obtain an entry by key

        :param index: Entry key
        """

        raise NotImplementedError()

    def put(self, entry: data.Entry):
        """
        Inserts an entry

        :param entry: Collection entry
        """

        raise NotImplementedError()

    def delete(self, key: str):
        """
        Deletes an entry

        :param key: Key of the entry to delete
        """

        raise NotImplementedError()
