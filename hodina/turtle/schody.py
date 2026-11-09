import turtle as t


def schod(d):
    if d > 300:
        return
    else:
        t.rt(122)
        t.fd(d)
        t.rt(90)
        t.fd(d)
        t.lt(90)
        schod(d+1)


t.seth(10)
t.speed(0)
schod(2)

t.done()
