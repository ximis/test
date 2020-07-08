

def pytest_generate_tests(metafunc):
    if "data" in metafunc.fixturenames:
        metafunc.parametrize("data", [{"aa":1, "bb":2, "cc":3}, {"aa":1, "bb":2, "cc":4}],ids=["one", "two"])

