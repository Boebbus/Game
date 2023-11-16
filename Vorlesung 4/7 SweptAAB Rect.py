import pygame as pg
from collider import *

WIDTH = 800
HEIGHT = 600
FPS = 60

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

PLAYER_FRICTION = -0.01
GRAVITY = 0.8

vec = pg.math.Vector2

# initialize pg and create window
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("My Game")
clock = pg.time.Clock()


def draw_text(text, size, col, x, y):
    # utility function to draw text on screen
    font_name = pg.font.match_font('arial')
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, col)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)


collider = Collider()

p = vec(30, 30)
mousepos = vec(0, 0)
vel = vec(0, 0)

player_image = pg.Surface((32, 32))
player_image.fill(WHITE)
player_rect = player_image.get_rect()
player_rect.topleft = (30, 30)

# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)

    # Process input (events)
    for event in pg.event.get():
        # check for closing window
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            player_rect.center = event.pos
        elif event.type == pg.MOUSEMOTION:
            mousepos.x, mousepos.y = event.pos
            vel = vec(mousepos - player_rect.center)

    # Render
    screen.fill(BLACK)
    # Rect
    image = pg.Surface((200, 200))
    static_rect = image.get_rect()
    static_rect.topleft = (300, 300)
    hit = collider.DynamicRectVsRect(player_rect, vel, static_rect)
    if hit:
        farbe = RED
    else:
        farbe = GREEN

    image.fill(farbe)
    screen.blit(image, static_rect)
    screen.blit(player_image, player_rect)
    pg.draw.line(screen, GREEN, player_rect.center, mousepos, 1)
    pg.draw.circle(screen, WHITE, collider.contact_point, 2)
    #pg.draw.circle(screen, BLUE, mousepos, 10)
    pg.draw.line(screen, WHITE, collider.contact_point,
                 collider.contact_point + collider.contact_normal*20, 1)
    txt = "t_near, t_far: ({:.5f}, {:.5f})".format(
        collider.t_hit_near, collider.t_hit_far)
    #draw_text(txt, 25, WHITE, 5, 5)

    # Double Buffering
    pg.display.flip()

pg.quit()
