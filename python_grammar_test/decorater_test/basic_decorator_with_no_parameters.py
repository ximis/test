

'''
无参装饰器
'''
def dec(func):
    print(dec)
    print(func.__name__)
    return func

@dec
def tt():
    print("tt")

tt()