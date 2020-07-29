from typing import NewType

UserId = NewType('UserId', int)


def get_user_info(id: UserId):
    pass


if __name__ == '__main__':
    get_user_info(-1)
    get_user_info(UserId(2))
