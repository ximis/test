'''
构造方法，python和java的的构造方法，都不能重载且不调用 super不会调用父类的构造方法
'''


class A:
    def __init__(self):
        print("this is class A")


class B(A):
    def __init__(self):
        super().__init__()
        print("this is class B")


b = B()
