import pytest
import random


# @pytest.fixture()
@pytest.fixture(scope="module", params=[1,2,3,4])
def data_provider():
    print("data provider init")
    yield random.randint(1,10)
    print ("test finish")


def test_a(data_provider):
    print(data_provider)


def test_b(data_provider):
    print(data_provider)


@pytest.fixture
def data_provider2():
    return random.randint(1,10)


def test_c(data_provider2, data_provider):
    print(data_provider2)
    print(data_provider)


def test_d(data_provider2):
    print(data_provider2)

