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
