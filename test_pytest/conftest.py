import pytest


@pytest.fixture
def logs():
    print("start---")
    yield
    print("end -----")