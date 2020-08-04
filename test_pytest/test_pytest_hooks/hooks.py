def pytest_my_hook(config):
    """
    Print all active hooks to the screen.
    """
    print(config.hook)
