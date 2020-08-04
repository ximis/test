import pytest

'''
网上搜了一下，说是由于版本的问题。 
'''


def pytest_addhooks(pulginmanager):
    from . import hooks
    pulginmanager.add_hookspecs(hooks)


@pytest.fixture()
def my_fixture(pytestconfig):
    print(pytestconfig.hook.pytest_my_hook(config=pytestconfig))
