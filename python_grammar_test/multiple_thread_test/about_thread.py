import _thread


def my_pp():
    print("1")
    lock.release()


lock = _thread.allocate_lock()
lock.acquire()
_thread.start_new_thread(my_pp, ())
while lock.locked():
    pass
