import pytest

from jsonvault.collections import (
    CollectionDefinition,
    JsonCollection
)
from jsonvault.data import Entry


def test_create_definition():
    """
    Scenario. A collection definition is created.
    Expected result. Definition should be successfully created.
    """

    name = "collection"
    definition = CollectionDefinition(name)

    assert definition is not None
    assert definition.name == name
    assert type(definition.indexes) == list
    assert not definition.indexes


def test_create_definition_with_indexes():
    """
    Scenario. A collection definition is created with indexes defined.
    Expected result. Definition should be succesfully created.
    """

    name = "collection"
    definition = CollectionDefinition(name)

    assert definition is not None
    assert definition.name == name
    assert type(definition.indexes) == list
    assert not definition.indexes


def test_create_collection():
    """
    Scenario. A collection is created.
    Expected result. Collection should be successfully created.
    """

    name = "collection"
    definition = CollectionDefinition(name)
    collection = JsonCollection(definition)

    assert collection is not None
    assert collection.name == name


@pytest.mark.xfail(strict=True, reason="Waiting on implementation")
def test_collection_get_entry_not_found():
    """
    Scenario. Retrieve an non-existent entry from a collection.
    Expected result. No entry is found.
    """

    index = "key"
    collection = JsonCollection(CollectionDefinition("collection"))

    entry = collection.get(index)
    assert entry is None


@pytest.mark.xfail(strict=True, reason="Waiting on implementation")
def test_collection_get_non_existing_entry():
    """
    Scenario. Retrieve an non-existing entry from a collection.
    Expected result. No entry is found.
    """

    index = "key"
    collection = JsonCollection(CollectionDefinition("collection"))

    entry = collection.get(index)
    assert entry is None


@pytest.mark.xfail(strict=True, reason="Waiting on implementation")
def test_collection_put_entry():
    """
    Scenario. Insert an entry in a collection.
    Expected result. Entry is inserted and no exceptions are thrown.
    """

    entry = Entry("key", "value")
    collection = JsonCollection(CollectionDefinition("collection"))

    collection.put(entry)


@pytest.mark.xfail(strict=True, reason="Waiting on implementation")
def test_collection_get_existing_entry():
    """
    Scenario. Retrieve an existing entry from a collection.
    Expected result. Entry is is successfully read and matches the written one.
    """

    expected_entry = Entry("key", "value")
    collection = JsonCollection(CollectionDefinition("collection"))

    collection.put(expected_entry)
    entry = collection.get(expected_entry.key)
    assert entry == expected_entry


@pytest.mark.xfail(strict=True, reason="Waiting on implementation")
def test_collection_delete_non_existing_entry():
    """
    Scenario. Delete a non-existing entry from a collection.
    Expected result. Delete doesn't throw any exception.
    """

    key = "key"
    collection = JsonCollection(CollectionDefinition("collection"))

    collection.delete(key)


@pytest.mark.xfail(strict=True, reason="Waiting on implementation")
def test_collection_delete_existing_entry():
    """
    Scenario. Delete a existing entry from a collection.
    Expected result. Delete doesn't throw any exception and entry can't be found afterwards.
    """

    key = "key"
    collection = JsonCollection(CollectionDefinition("collection"))

    collection.put(Entry(key, "value"))
    collection.delete(key)
    entry = collection.get(key)
    assert entry is not None
