import allure
import pytest


@allure.step
def simple_step(step_param1, step_param2 = None):
    pass


@pytest.mark.parametrize('param1', [True, False], ids=['id explaining value 1', 'id explaining value 2'])
def test_parameterize_with_id(param1):
    simple_step(param1)


@pytest.mark.parametrize('param1', [True, False])
@pytest.mark.parametrize('param2', ['value 1', 'value 2'])
def test_parametrize_with_two_parameters(param1, param2):
    simple_step(param1, param2)


@pytest.mark.parametrize('param1', [True], ids=['boolean parameter id'])
@pytest.mark.parametrize('param2', ['value 1', 'value 2'])
@pytest.mark.parametrize('param3', [1])
def test_parameterize_with_uneven_value_sets(param1, param2, param3):
    simple_step(param1, param3)
    simple_step(param2)

def test_step_only():
    simple_step(1,2)
    simple_step(2,3)

@allure.step
def test_case_label_step():
    simple_step(2,3)
    simple_step(3,2)

@allure.step
class MyClass():
    def simple_step2(self,params1, params2):
        pass

tt = MyClass()
def test_class_step_label():
    tt.simple_step2(2,3)
    tt.simple_step2(4,5)



