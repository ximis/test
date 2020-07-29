from prometheus_client import Counter
from prometheus_client import Gauge

c = Counter('my_failures', 'Description of counter')
print(c)
c.inc()  # Increment by 1
print(c)
c.inc(1.6)  # Increment by given value
print(c)
print(c.collect())

g = Gauge("my_gauge", "my description of gauge")
g.set(1)
g.inc(1)
g.dec(2)
g.track_inprogress()  # 在进入时加1，在退出时减一


@g.track_inprogress()
def f():
    pass
