import pytest


@pytest.fixture
def values(request):
    return [1, 2]


'''
this test not work, I just want to test, if the values can work.
'''


@pytest.mark.parametrize("tt", values())
def test_tt(tt):
    print(tt)
