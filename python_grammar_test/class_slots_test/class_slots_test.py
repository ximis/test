class A:
    FOO = 1

    def __init__(self):
        self.instance = 1


class B:
    __slots__ = ["insa"]
    FOO = 1


