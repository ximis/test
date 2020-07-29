class A:
    g_v = None

    def __init__(self):
        if A.g_v is None:
            print("I will init this varible!")
            g_v = 1


from threading import Thread

l1 = []
for i in range(100000):
    t = Thread(target=A)
    t.start()
    l1.append(t)
for t in l1:
    t.join()
print(A.a)
