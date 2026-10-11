
# creds for the song: https://www.youtube.com/watch?v=8bch0KYfeOM

# original drawings for the assets coming soon :)

import pygame
from pygame.locals import *
import json

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Gardening")

clock = pygame.time.Clock()

update = pygame.image.load(r"assets\future_update.png")
update_large = pygame.transform.scale(update, (487, 47))

bg = pygame.image.load(r"assets\placeholder.png").convert()
bg_large = pygame.transform.scale(bg, (1000, 600))

xtree, ytree = 170, 170
tree = pygame.image.load(r"assets\tree.png").convert_alpha()
tree_large = pygame.transform.scale(tree, (xtree, ytree))
tree_coords = (45, 50)
tree_rect = tree_large.get_rect(topleft=tree_coords)

xflowers, yflowers = 100, 100
flowers = pygame.image.load(r"assets\flower.png").convert_alpha()
flowers_large = pygame.transform.scale(flowers, (xflowers, yflowers))
flowers_coords = (70, 300)
flowers_rect = flowers_large.get_rect(topleft=flowers_coords)

xbush, ybush = 150, 150
bush = pygame.image.load(r"assets\bush.png").convert_alpha()
bush_large = pygame.transform.scale(bush, (xbush, ybush))
bush_coords = (50, 450)
bush_rect = bush_large.get_rect(topleft=bush_coords)

active_surface = None
active_rect = None
moving = False
running = True

while running:

    cursor = pygame.mouse.get_pos()
    if tree_rect.collidepoint(cursor) or flowers_rect.collidepoint(cursor) or bush_rect.collidepoint(cursor):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        elif event.type == MOUSEBUTTONDOWN:
            if tree_rect.collidepoint(event.pos):
                active_surface = tree_large
                active_rect = tree_large.get_rect(topleft=tree_coords)
                moving = True
            elif flowers_rect.collidepoint(event.pos):
                active_surface = flowers_large
                active_rect = flowers_large.get_rect(topleft=flowers_coords)
                moving = True
            elif bush_rect.collidepoint(event.pos):
                active_surface = bush_large
                active_rect = bush_large.get_rect(topleft=bush_coords)
                moving = True

        elif event.type == MOUSEBUTTONUP:
            if moving and active_surface and active_rect:
                bg_large.blit(active_surface, active_rect)
            moving = False
            active_surface = None
            active_rect = None

        elif event.type == MOUSEMOTION and moving and active_rect:
            active_rect.move_ip(event.rel)

    screen.blit(bg_large, (0, 0))
    screen.blit(tree_large, tree_coords)
    screen.blit(flowers_large, flowers_coords)
    screen.blit(bush_large, bush_coords)
    screen.blit(update_large, (250, 550))

    if moving and active_surface and active_rect:
        screen.blit(active_surface, active_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()