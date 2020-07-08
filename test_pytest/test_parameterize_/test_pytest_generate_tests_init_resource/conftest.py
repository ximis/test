import pytest


def pytest_generate_tests(metafunc):
    if "db" in metafunc.fixturenames:
        metafunc.parametrize("db", ["d1", "d2"], indirect=True)


class DB1:
    "one database object"


class DB2:
    "alternative database object"


@pytest.fixture
def db(request):
    print("connect db")
    if request.param == "d1":
        return DB1()
    elif request.param == "d2":
        return DB2()
    else:
        raise ValueError("invalid internal test config")
    # yield
    print("clear db")