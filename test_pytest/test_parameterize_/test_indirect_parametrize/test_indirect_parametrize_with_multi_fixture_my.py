import pytest

names = ["joy", "sam", "john"]


@pytest.fixture(params=names)
def fixture(request):
    if request.param == "joy":
        pytest.skip("joy is not saying")
    return request.param


def test_tt(fixture):
    print(fixture)