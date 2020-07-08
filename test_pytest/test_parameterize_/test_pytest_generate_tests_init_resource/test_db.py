
import pytest


def test_db_initialized(db):
    # a dummy test
    print(db.__class__.__name__)
        # pytest.fail("deliberately failing for demo purposes")


