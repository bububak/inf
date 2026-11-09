import turtle as t


def riadok(l, s):

    if l == 1:
        t.dot(s)
        t.color("red")
        t.dot(s/2)
    else:

        for _ in range(l):
            t.dot(s)
            t.fd(s * 2)

        t.bk(l * s * 2)
        t.lt(90)
        t.fd(s * 2)
        t.rt(90)
        t.fd(s)

        riadok(l - 1, s)

        t.bk(s)
        t.lt(90)
        t.bk(s * 2)
        t.rt(90)
        t.fd(l * s * 2)

        for _ in range(l):
            t.bk(s * 2)
            t.dot(s / 2)


t.penup()

riadok(5, 30)

t.done()
