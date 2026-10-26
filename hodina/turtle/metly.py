import random
import turtle as t


def metla(l, n, s):
    x, y = t.pos()
    angle = t.heading()

    t.fd(l)
    t.rt(45)
    for _ in range(n + 1):
        t.fd(s)
        t.bk(s)
        t.lt(90 // n)

    t.teleport(x, y)
    t.seth(angle)


t.seth(random.randrange(360))
t.speed(0)

for _ in range(5):
    x = random.randrange(-200, 200)
    y = random.randrange(-200, 200)
    l = random.randrange(100, 200)
    n = random.randrange(2, 10)
    s = random.randrange(30, 50)

    t.teleport(x, y)
    metla(l, n, s)

t.done()
