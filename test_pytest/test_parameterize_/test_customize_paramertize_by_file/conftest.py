import yaml
import pytest

def pytest_generate_tests(metafunc):
    if "stringinput" in metafunc.fixturenames:
        metafunc.parametrize("stringinput", metafunc.config.getoption("stringinput"))


def file_source(arg_names, filename):
    data = yaml.load(open(filename), Loader=yaml.FullLoader)
    return pytest.mark.parametrize(arg_names, )