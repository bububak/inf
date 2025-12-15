import pygame as pg
import random
pg.init()

ScreenInfo = pg.display.Info()
WIDTH, HEIGHT = ScreenInfo.current_w,ScreenInfo.current_h
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("box dodging")
clock = pg.time.Clock()
fps = 60
speed = 360 / fps
es = speed / 2
s = 50  # size of player and enemies

R = 0
G = 255
B = 255

ENEMYSPAWN = pg.USEREVENT + 1
time_add = 1.0 / fps

# Fonts and text
end_font = pg.font.Font(pg.font.get_default_font(), 100)
text_surface = end_font.render("GAME OVER", True, "White")
text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))

# Game variables
enemies = []
game_ended = False
time = 0.0

# Player rectangle (initial position)
player = pg.Rect(WIDTH // 2 - s // 2, HEIGHT // 2 - s // 2, s, s)

# Set the enemy spawn rate (milliseconds)
t = 100
pg.time.set_timer(ENEMYSPAWN, t)

def reset_game():
    global player, enemies, game_ended, time
    player = pg.Rect(WIDTH // 2 - s // 2, HEIGHT // 2 - s // 2, s, s)
    enemies = []
    game_ended = False
    time = 0.0
    pg.time.set_timer(ENEMYSPAWN, t)  # Restart enemy spawn timer

class Enemy:
    def __init__(self):
        spawnpoint = random.randint(20, WIDTH - 40)
        self.color = (255, random.randint(0, 50), random.randint(0, 50))
        direction_num = random.randint(0, 3)
        if direction_num == 0:
            self.d = [0, es]
            self.coords = [spawnpoint, -s]
        if direction_num == 1:
            self.d = [-es, 0]
            self.coords = [WIDTH, spawnpoint]
        if direction_num == 2:
            self.d = [0, -es]
            self.coords = [spawnpoint, HEIGHT]
        if direction_num == 3:
            self.d = [es, 0]
            self.coords = [-s, spawnpoint]
        self.rectangle = pg.Rect(self.coords[0], self.coords[1], s, s)

    def move(self):
        if not game_ended:
            for i in range(len(self.coords)):
                self.coords[i] = self.coords[i] + self.d[i]
            self.rectangle = pg.Rect(self.coords[0], self.coords[1], s, s)

def events():
    global run, game_ended
    for e in pg.event.get():
        if e.type == pg.QUIT:
            run = False
        if e.type == ENEMYSPAWN:
            spawn_enemy()
        if e.type == pg.KEYDOWN:
            if e.key == pg.K_SPACE and game_ended:
                reset_game()
            if e.key == pg.K_ESCAPE:
                run = False

def collision_check(opps):
    global run, game_ended
    for e in opps:
        if player.colliderect(e.rectangle):
            game_ended = True
    if game_ended:
        screen.blit(text_surface, text_rect)

def spawn_enemy():
    global enemies
    enemy = Enemy()
    enemies.append(enemy)

def draw_enemy(opps):
    for e in opps:
        e.move()
        pg.draw.rect(screen, e.color, e.rectangle)

def player_move():
    key = pg.key.get_pressed()
    if not game_ended:
        if key[pg.K_w]:
            player.y += -speed
        if key[pg.K_s]:
            player.y += speed
        if key[pg.K_a]:
            player.x += -speed
        if key[pg.K_d]:
            player.x += speed
    pg.draw.rect(screen, (R, G, B), player)

def draw_time():
    global time, time_add, game_ended
    if not game_ended:
        time += time_add
    time_surface = end_font.render(str(round(time, 2)), True, "White")
    time_rect = text_surface.get_rect(topleft=(0, 0))
    screen.blit(time_surface, time_rect)

# Main game loop
run = True
while run:
    screen.fill((0, 0, 0))

    player_move()
    draw_enemy(enemies)
    collision_check(enemies)
    events()
    draw_time()

    pg.display.update()
    clock.tick(fps)

pg.quit()