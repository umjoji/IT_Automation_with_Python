#!/usr/bin/python3

from count_from_by import CountFromBy

g = CountFromBy(100, 10)

print(g.val)
print(g.incr)
g.increase()
print(g.val)
g.decrease()
print(g.val)
