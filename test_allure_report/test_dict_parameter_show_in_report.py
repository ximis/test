import pytest


def idfns(data):
    return str(data)


@pytest.mark.parametrize("data", [{"a": 1, "b": 2}, {"a": 3, "b": 3}], ids=lambda x: str(x))
def test_dict(data):
    print(data)
