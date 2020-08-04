import sys


def my_except_hook(exctype, value, traceback):
    if exctype == KeyboardInterrupt:
        print("Handler code goes here")
    else:
        sys.__excepthook__(exctype, value, traceback)


sys.excepthook = my_except_hook

raise Exception

