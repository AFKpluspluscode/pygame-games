import random
import pygame
import math

#Keys
from pygame.locals import *

#Variables
SCREEN_HEIGHT = 720
SCREEN_WIDTH = 1280
GAME_NAME = "Game"

#To log
#LOG_INFO = "Log: "

player_spawn = [SCREEN_WIDTH/2, SCREEN_HEIGHT/2]
enemy_spawn = [SCREEN_WIDTH/4,SCREEN_WIDTH/4]
spawn = [SCREEN_WIDTH/2, SCREEN_HEIGHT/2]

def checkcollide(x1, y1, x2, y2):
    distance = math.sqrt((math.pow(x1-y1, 2)) + (math.pow(x2-y2, 2)))
    if distance < 60:
        return True
    else:
        return False

speed = 1

#Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
            super(Player, self).__init__()
            self.surf = pygame.image.load("sprites/player.png")
            self.rect = self.surf.get_rect()
    def update(self, pressed_keys):

        if pressed_keys[K_UP]:
            player_spawn[1] -= speed
        if pressed_keys[K_DOWN]:
            player_spawn[1] += speed
        if pressed_keys[K_LEFT]:
            player_spawn[0] -= speed
        if pressed_keys[K_RIGHT]:
            player_spawn[0] += speed

        if player_spawn[0] < -36:
            player_spawn[0] = -36
        if player_spawn[0] > 1198:
            player_spawn[0] = 1198
        if player_spawn[1] <= -9:
            player_spawn[1] = -9
        if player_spawn[1] >= 616:
            player_spawn[1] = 616
        
#Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load("sprites/player.png")
        self.rect = self.surf.get_rect()
    def ai(self):
        if random.randint(0, 1500) <= random.randint(0, 100):
            enemy_spawn[0] += random.randint(1, 3)
        if random.randint(0, 1500) <= random.randint(0, 100):
            enemy_spawn[0] -= random.randint(1, 3)
        if random.randint(0, 1500) <= random.randint(0, 100):
            enemy_spawn[1] += random.randint(1, 3)
        if random.randint(0, 1500) <= random.randint(0, 100):
            enemy_spawn[1] -= random.randint(1, 3)

        if enemy_spawn[0] < -36:
            enemy_spawn[0] = -36
        if enemy_spawn[0] > 1198:
            enemy_spawn[0] = 1198
        if enemy_spawn[1] <= -9:
            enemy_spawn[1] = -9
        if enemy_spawn[1] >= 616:
            enemy_spawn[1] = 616

        

#Start windows
pygame.init()
#print(LOG_INFO + "windows starting")

FONT = pygame.font.Font(None, 35)
#print(LOG_INFO + "font reloaded")

player = Player()
enemy = Enemy()
#print(LOG_INFO + "player and enemy reloaded")

#Set up window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#print(LOG_INFO + "windows maked")

#Caption
pygame.display.set_caption(GAME_NAME)



# Run until the user asks to quit
running = True
while running:

    #If user quits
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_s:
                speed += 1
            if event.key == K_a:
                speed -= 1
        if event.type == QUIT:
            running = False
            #print(LOG_INFO + "player quit")
            

    
    #White background
    screen.fill((255, 255, 255))

    #Blue circle on screen with 75 radius on middle
    pygame.draw.circle(screen, (0, 0, 255), spawn, 75)

    #Text
    text_s = FONT.render("S to increase speed by 1", True, (0, 0, 0), (255, 255, 255))
    text_a = FONT.render("A to decrease speed by 1", True, (0, 0, 0), (255, 255, 255))
    
    #Coordinates
    #text_x = FONT.render(str(player_spawn[0]), True, (0, 0, 0), (255, 255, 255))
    #text_y = FONT.render(str(player_spawn[1]), True, (0, 0, 0), (255, 255, 255))
    #text_x2 = FONT.render(str(enemy_spawn[0]), True, (0, 0, 0), (255, 255, 255))
    #text_y2 = FONT.render(str(enemy_spawn[1]), True, (0, 0, 0), (255, 255, 255))

    
    screen.blit(player.surf, (player_spawn))
    screen.blit(enemy.surf, (enemy_spawn))
    screen.blit(text_s, (10, 690))
    screen.blit(text_a, (10, 650))
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)
    enemy.ai()
    #screen.blit(text_x, spawn)
    #screen.blit(text_y, (640, 300))
    #screen.blit(text_x2, (123, 321))
    #screen.blit(text_y2, (321, 123))

    collidecheck = checkcollide(player_spawn[0], enemy_spawn[0], player_spawn[1], enemy_spawn[1])
    if collidecheck == True:
        player.kill()
        #print(LOG_INFO + "Player killed")
        running = False

    #Flip
    pygame.display.flip() 

#Stop
pygame.quit()
