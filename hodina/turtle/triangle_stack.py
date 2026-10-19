import random
import turtle as t


def triangle(l, angle):
    t.pendown()
    t.setheading(angle)
    t.fd(l // 2)
    for i in range(4):
        t.lt(120)
        t.fd(l)


NUM_OF_TRIANGLES = random.randrange(3, 8)
MAX_ANGLE = 15
MIN_L = 100
MAX_L = 200

t.teleport(0, -500)
for i in range(NUM_OF_TRIANGLES):
    a = random.randrange(360 - MAX_ANGLE, 360 + MAX_ANGLE) % 360
    triangle(random.randrange((MIN_L * 2) // 2, (MAX_L * 2) // 2), a)

t.done()
