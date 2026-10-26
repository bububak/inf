import random
import turtle as t


def padajuci_troj(l):
    t.setheading(random.randrange(360 - MAX_ANGLE, 360 + MAX_ANGLE) % 360)
    t.fd(l // 2)
    for _ in range(4):
        t.lt(120)
        t.fd(l)


NUM_OF_TRIANGLES = random.randrange(3, 8)
MAX_ANGLE = 20
MIN_L = 30
MAX_L = 100

t.speed(0)
t.teleport(0, -500)
for i in range(NUM_OF_TRIANGLES):
    padajuci_troj(random.randrange(MIN_L, MAX_L))

t.done()
