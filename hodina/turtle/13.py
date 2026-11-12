import turtle as t


def troj(n, d):
    if n < 0:
        return
    else:
        for _ in range(3):
            t.rt(60)
            troj(n - 1, d / 2)
            t.lt(60)
            t.fd(d)
            t.lt(120)


t.speed(0)
t.delay(0)
troj(3, 300)
t.done()
