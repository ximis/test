
class TestTT:
    @classmethod
    def setup_class(cls):
        print("this is setup class")

    @classmethod
    def teardown_class(cls):
        print("teardown class")

    def test_func(self):
        print("test_func  this is ")