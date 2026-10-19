import random
import turtle as t


def slnko(x, y, n, s, l):
    t.speed(0)
    t.pendown()
    t.teleport(x, y)
    for i in range(n):
        t.lt(360 / n)
        t.fd(s)
        t.rt(90)
        t.fd(l)
        t.rt(90)
        t.fd(s)
        t.rt(90)
        t.fd(l)
        t.rt(90)
        t.fd(s)


X = random.randrange(-350, 301)
Y = random.randrange(100, 221)
N = random.randrange(5, 16)
S = random.randrange(10, 21)
L = random.randrange(30, 81)
slnko(X, Y, N, S, L)
t.done()
