import pytest
import os


def pytest_generate_tests(metafunc):
    if "db" in metafunc.fixturenames:
        metafunc.parametrize("db", ["d1", "d2"], indirect=True)

    print(metafunc.definition.name)    #方法名
    print(metafunc.definition.fspath.purebasename)    #文件名
    print(os.path.basename(metafunc.definition.fspath.dirname))  #上级文件夹名
    # metafunc.fixturenames #默认值[]


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