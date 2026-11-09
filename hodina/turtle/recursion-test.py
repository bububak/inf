import turtle as t

def spirala(d,a):
    print(f"in {d}, {a}")
    if d > 100 or a < 0: # trivialny pripad
        t.dot(30)
        t.pencolor("red")
        # t.lt(180)
        return
    else:
        t.fd(d)
        t.rt(a)
        spirala(d+5,a)
        t.lt(a)
        t.fd(d)



spirala(2, 90)
t.done()
