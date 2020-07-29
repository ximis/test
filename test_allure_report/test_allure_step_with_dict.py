import pytest
import allure


@allure.step
def send(data):
    print(data)
    print("what's this?")


@pytest.mark.parametrize('data', [{"a": 1, "b": 2}, {"a": 3, "b": 3}], ids= lambda x: str(x))
def test_step_with_dict(data):
    send(data)
