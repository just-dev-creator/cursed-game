import pygame
import sys
import random
import time
import threading
import os

def ressource_path(relative_path):
    if  hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)
# pygame.init()
screen = pygame.display.set_mode([
    600, 600
])
background = pygame.image.load(("background.png"))
clock = pygame.time.Clock()
player = {
    "x": 560,
    "y": 520,
    "speed": 3,
    "width": 40,
    "height": 80
}
pygame.display.set_caption("Cursed", "curses")
player_pos = pygame.rect.Rect(player["x"], player["y"], player["width"], player["height"])
wasd_enabled = False
finished = False
stopped = False



def player_movement():
    global finished
    global stopped
    pygame.init()
    while True:
        if pygame.event.get(pygame.QUIT):
            stopped = True
            sys.exit(0)
            exit(0)
        pressed_key = pygame.key.get_pressed()
        if not wasd_enabled:
            if pressed_key[pygame.K_UP]:
                # player_pos.move_ip(player_pos.x, (player_pos.y - player["speed"]))
                player_pos.move_ip(0, player["speed"] * -1)
            if pressed_key[pygame.K_RIGHT]:
                # player["x"] += player["speed"]
                player_pos.move_ip(player["speed"], 0)
            if pressed_key[pygame.K_DOWN]:
                # player["y"] += player["speed"]
                player_pos.move_ip(0, player["speed"])
            if pressed_key[pygame.K_LEFT]:
                # player["x"] -= player["speed"]
                player_pos.move_ip(-1 * player["speed"], 0)
        else:
            if pressed_key[pygame.K_w]:
                # player_pos.move_ip(player_pos.x, (player_pos.y - player["speed"]))
                player_pos.move_ip(0, player["speed"] * -1)
            if pressed_key[pygame.K_d]:
                # player["x"] += player["speed"]
                player_pos.move_ip(player["speed"], 0)
            if pressed_key[pygame.K_s]:
                # player["y"] += player["speed"]
                player_pos.move_ip(0, player["speed"])
            if pressed_key[pygame.K_a]:
                # player["x"] -= player["speed"]
                player_pos.move_ip(-1 * player["speed"], 0)
        if finished:
            screen.blit(background, (0,0))
        else:
            screen.fill((0, 0, 0))
        # pygame.draw.rect(screen, (255, 255, 0), (player["x"], player["y"], player["width"], player["height"]))
        pygame.draw.rect(screen, (0, 0, 255), player_pos)
        pygame.draw.rect(screen, (0, 255, 0), (0, 0, 40, 80))
        pygame.display.update()
        player_pos.clamp_ip(screen.get_rect())



        if player_pos.x == 0 & player_pos.y == 0:
            finished = True

        clock.tick(20)
#         0 0
#         560 520


def cursed():
    global wasd_enabled
    global stopped
    while True:
        if stopped:
            sys.exit()
        randint = random.randint(0, 10)
        if randint < 4:
            player["speed"] *= -1
        elif randint > 4 & randint < 6:
            wasd_enabled = not wasd_enabled
        time.sleep(random.randint(0, 7))


thread2 = threading.Thread(target=cursed)
thread2.start()
player_movement()

