import pytest


@pytest.fixture
def data_provider():
    print("this is fixture 1")


@pytest.mark.usefixtures("data_provider")
@pytest.fixture
def data_provider2():
    print("this is fixture 2")


@pytest.mark.usefixtures("data_provider2")
def test_a():
    print("this is test_a")