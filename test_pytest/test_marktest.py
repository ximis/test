import pytest

pytestmark = pytest.mark.joytest

@pytest.mark.webtest
def test_send_http():
    print("this use to send http")


def test_something_quick():
    pass


def test_another():
    pass


class TestClass:
    def test_method(self):
        pass