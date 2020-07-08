import pytest

#最后发现，如果是想按package算的话，我又想让每个函数运行。所以用了默认的。
@pytest.fixture(autouse=True)
def tlog():
    print("setup---")
    yield
    print("teardown---")
