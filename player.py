import pygame
import random
pygame.init()
#create the screen
screen = pygame.display.set_mode((800, 500))
#window title
pygame.display.set_caption("Adventure Begins")
#Player
player_img = pygame.image.load('spaceship.png')
playerX = 30
playerY = 100
playerX_change = 0
def player(x, y):
    screen.blit(player_img, (x, y))

#game loop
running = True
while running:
    #RGB = Red, Green, Blue 
    screen.fill((100, 55, 40))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if keystroke is pressed, check whether it's right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 800 - 64: #player image is of 64 pixels
        playerX = 736

    player(playerX, playerY)
    pygame.display.update()

