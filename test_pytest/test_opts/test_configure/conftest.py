import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default='k8s',
        help="assign which env to use",
    )


@pytest.fixture(scope="session", autouse=True)
def init(request):
    print(request.config.option.env)
    print(request.config.option.cmdopt)
