import random
import turtle as t


def metla(x, y, l, n, s, angle):
    t.pendown()
    t.speed(0)
    t.teleport(x, y)
    t.seth(angle)
    t.fd(l)
    t.rt(45)

    for i in range(n + 1):
        t.fd(s)
        t.bk(s)
        t.lt(90 // n)

    t.teleport(x, y)
    t.seth(angle)


angle = random.randrange(360)

for i in range(5):
    x = random.randrange(-200, 200)
    y = random.randrange(-200, 200)
    l = random.randrange(100, 200)
    n = random.randrange(2, 10)
    s = random.randrange(30, 50)
    metla(x, y, l, n, s, angle)

t.done()
