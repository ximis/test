import pytest


@pytest.mark.parametrize("data,", [{"a":1,"b":2}, {"a":1,"b":3}], ids=["a","b"])
def test_dic_param(data):
    print(data)

