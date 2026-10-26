import random
import turtle as t


def obdlznik(a, b):
    for _ in range(2):
        t.fd(a)
        t.rt(90)
        t.fd(b)
        t.rt(90)


def slnko(n, strana, luc):
    for _ in range(n):
        t.lt(360 / n)
        obdlznik(strana, luc)
        t.fd(strana)


X = random.randrange(-350, 301)
Y = random.randrange(100, 221)
N = random.randrange(5, 16)
S = random.randrange(10, 21)
L = random.randrange(30, 81)

t.speed(0)
t.teleport(X, Y)
slnko(N, S, L)
t.done()
