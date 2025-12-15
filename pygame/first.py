import pygame

pygame.init()


def get_events():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


W, H = 500, 500
fps = 60

running = True
color = "black"
root = pygame.display.set_mode((500, 500))


while running:
    get_events()
    root.fill(color)

    if color == "red":
        color = "green"
    else:
        color = "red"

    pygame.display.flip()
