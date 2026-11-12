import random
import turtle as t


def ciara_vlocka(n, d):
    if n <= 0:
        t.fd(d / 3)
        t.lt(60)
        t.fd(d / 3)
        t.rt(120)
        t.fd(d / 3)
        t.lt(60)
        t.fd(d / 3)
        return
    else:
        ciara_vlocka(n - 1, d / 3)
        t.lt(60)
        ciara_vlocka(n - 1, d / 3)
        t.rt(120)
        ciara_vlocka(n - 1, d / 3)
        t.lt(60)
        ciara_vlocka(n - 1, d / 3)


def vlocka(n, d):
    for _ in range(3):
        ciara_vlocka(n, d)
        t.rt(120)


def ciara2(n, d):
    if n <= 0:
        t.fd(d / 3)
        t.lt(90)
        t.fd(d / 6)
        t.rt(90)
        t.fd(d / 3)
        t.rt(90)
        t.fd(d / 6)
        t.lt(90)
        t.fd(d / 3)
    else:
        ciara2(n - 1, d / 3)
        t.lt(90)
        ciara2(n - 1, d / 6)
        t.rt(90)
        ciara2(n - 1, d / 3)
        t.rt(90)
        ciara2(n - 1, d / 6)
        t.lt(90)
        ciara2(n - 1, d / 3)


def ciara3(n, d):
    if n <= 0:
        t.fd(d / 3)
        t.lt(90)
        t.fd(d / 3)
        t.rt(90)
        t.fd(d / 3)
        t.rt(90)
        t.fd(d / 3)
        t.lt(90)
        t.fd(d / 3)
        return
    else:
        ciara3(n - 1, d / 3)
        t.lt(90)
        ciara3(n - 1, d / 3)
        t.rt(90)
        ciara3(n - 1, d / 3)
        t.rt(90)
        ciara3(n - 1, d / 3)
        t.lt(90)
        ciara3(n - 1, d / 3)


def bin_strom(n, branch_count, angle_range, branch_length, d):
    if n < 0:
        t.pencolor("green")
        t.dot(d / 2)
        t.pencolor("brown")
    else:
        t.pencolor("brown")
        t.fd(d / 2)

        for _ in range(random.choice(range(branch_count[0], branch_count[1]))):
            temp_rot = (
                360 + random.randrange(-1 * (angle_range // 2), angle_range // 2)
            ) % 360
            t.lt(temp_rot)
            bin_strom(
                n - 1,
                branch_count,
                angle_range,
                branch_length,
                d * 0.1 * random.randrange(branch_length[0], branch_length[1]),
            )
            t.rt(temp_rot)
        t.bk(d / 2)


t.speed(0)
t.delay(0)
t.width(5)
t.seth(90)

# vlocka(2,500)
# ciara2(3, 500)
# ciara3(5, 500)
bin_strom(3, (2, 8), 120, (5, 8), 300)

t.done()
