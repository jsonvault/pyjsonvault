import pytest

from jsonvault.data import Entry


def test_create_entry():
    """
    Scenario. An entry is created.
    Expected result. Entry should be created successfully.
    """

    key, value = "key1", "value"
    entry = Entry(key, value)

    assert entry is not None
    assert entry.key == key
    assert entry.value == value


def test_entry_equality_compare():
    """
    Scenario. Two equal entries are compared.
    Expected result. Comparison should return True.
    """

    key, value = "key", "value"
    entry = Entry(key, value)
    other_entry = Entry(key, value)

    assert entry == other_entry


def test_entry_equality_compare_different_type():
    """
    Scenario. Two equal entries are compared.
    Expected result. Comparison should return True.
    """

    key, value = "key", "value"
    entry = Entry(key, value)

    assert entry != value


@pytest.mark.parametrize("first_entry_tuple, second_entry_tuple", [
    (("key", "value"), ("key", "value_different")),
    (("key", "value"), ("key_different", "value")),
    (("key", "value"), ("key_different", "value_different"))
])
def test_entry_equality_compare_different_content(first_entry_tuple, second_entry_tuple):
    """
    Scenario. Two equal entries are compared.
    Expected result. Comparison should return True.
    """

    first_entry = Entry(*first_entry_tuple)
    second_entry = Entry(*second_entry_tuple)
    assert first_entry != second_entry
