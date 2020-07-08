import pytest


@pytest.fixture(params=[0, 1], ids=["spam", "ham"])
def a(request):
    return request.param


def test_a(a):
    print(a)


def idfn(fixture_value):
    if fixture_value == 1:
        return "eggs"
    else:
        return None


@pytest.fixture(params=[1, 2], ids=idfn)
def b(request):
    return request.param


def test_b(b):
    print(b)