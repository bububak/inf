import turtle as t

def bodka(d):
    if d > 30:
        t.dot(d)
        return
    else:
        t.dot(d)
        t.penup()
        t.fd(d*2)
        t.pendown()
        bodka(d+3)
        t.bk(d*2)


bodka(5)
t.done()
