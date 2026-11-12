import turtle as t


def stvorec(n, d):
    if n < 0:
        return
    else:
        for _ in range(4):
            t.fd(d / 2)
            stvorec(n - 1, d / 3)
            t.rt(90)


t.speed(0)
t.delay(0)
stvorec(3, 300)
t.done()
