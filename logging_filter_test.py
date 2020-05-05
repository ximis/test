import logging
from random import choice


class MyFilter(logging.Filter):
    IPS = ["10.12.13.233", "22.22.22.22"]

    def filter(self, record):
        record.ip = choice(MyFilter.IPS)
        return True


if __name__ == '__main__':
    filter = MyFilter()
    logger = logging.getLogger()
    logging.basicConfig(format="%(asctime)-15s %(ip)-15s %(message)s", level= logging.DEBUG)

    logger.addFilter(MyFilter())
    logger.setLevel(logging.DEBUG)

    logger.warning("this is the warning info")
    logger.critical("???")
