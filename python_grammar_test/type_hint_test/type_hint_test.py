class Log:
    def __init__(self):
        print("this is init!")

    def info(self, msg):
        print(msg)


log: 'Log'


if __name__== '__main__':
    log.info("1341243")