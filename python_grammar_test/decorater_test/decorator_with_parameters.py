def dec(data):
    print(data)

    def wrapper(func):
        print(func.__name__)
        print(data)
        return func

    return wrapper


@dec(data=1)
def mytest():
    print("tt")


mytest()
