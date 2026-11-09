import turtle as t


def troj(n,d):
    if n < 0:
        return
    else:
        for _ in range(5):
            t.fd(d/2)
            t.lt(288)
            troj(n-1, d/3)
            t.rt(288)
            t.fd(d/2)
            t.rt(72)

t.speed(0)
t.delay(0)
troj(3,300)
t.done()
