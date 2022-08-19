import pygame
import random
import math
pygame.init()

#create the screen
screen = pygame.display.set_mode((800, 500))

#window title
pygame.display.set_caption("Adventure Begins")

#icon
icon = pygame.image.load('demon.png')
pygame.display.set_icon(icon)

#background
background = pygame.image.load('background.png')
#Player
player_img = pygame.image.load('bow.png')
playerX = 400
playerY = 400
playerX_change = 0

#score
score = 0

#Enemy
enemy_img = pygame.image.load('demon.png')
enemyX = random.randint(0, 736)
enemyY = random.randint(50, 150)
enemyX_change = 2
enemyY_change = 30

def enemy(x, y):
    screen.blit(enemy_img, (x, y))
def player(x, y):
    screen.blit(player_img, (x, y))

#arrow
arrow_img = pygame.image.load('arrow.png')
arrowX = 0
arrowY = 400
arrowX_change = 0
arrowY_change = 15
arrow_state = "ready" #ready - you can't see the bullet on the screen
                       #fire - The bullet is currently moving
def shoot_arrow(x, y):
    global arrow_state
    arrow_state = "fire"
    screen.blit(arrow_img, (x + 2 , y + 9))

def isCollision(arrowX, arrowY, bulletX, bulletY):
    distance = math.sqrt( math.pow(arrowX - enemyX, 2) + math.pow(arrowY - enemyY, 2) )
    return distance < 27 #collision occurs if distance < 15 pixels

#game loop
running = True
while running:
    #RGB = Red, Green, Blue 
    # screen.fill((100, 55, 40))
    #background image
    screen.blit(background, (0, 0))
    #event input checkpoint
    for event in pygame.event.get():
        #close window -> quit game in terminal
        if event.type == pygame.QUIT:
            running = False
        # if keystroke is pressed, check whether it's right or left
        if event.type == pygame.KEYDOWN:
            #leftward movement
            if event.key == pygame.K_LEFT:
                playerX_change = -4
            #rightward movement
            if event.key == pygame.K_RIGHT:
                playerX_change = 4
            #bullet fire  
            if event.key == pygame.K_SPACE: 
                #shoot the bullet only if it is "ready" i.e. on the screen
                if arrow_state == "ready":
                    shoot_arrow(playerX, arrowY) 
                    arrowX = playerX 
        #key released 
        if event.type == pygame.KEYUP:
            #if the released key was a right or left arrow key 
            #then stop moving the player(bow) 
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    #new X-coord of player
    playerX += playerX_change
    #Checking for boundaries of spaceship so that it doesnt go out
    if playerX <= 0:
        playerX = 0
    elif playerX >= 800 - 64:
        playerX = 736
    #new X-coord of enemy
    enemyX += enemyX_change

    #moving enemy downwards if it hits the window boundary
    if enemyX <= 0:
        enemyX_change = 1
        enemyY += enemyX_change
    elif enemyX >= 800 - 64:
        enemyX = -1
        enemyY += enemyY_change
    #arrow movement
    if arrowY <= 0:
        arrowY = 400
        arrow_state = "ready"
    #shooting arrow movement 
    if arrow_state == "fire":
        shoot_arrow(arrowX, arrowY)
        arrowY -= arrowY_change
    #collision
    collision = isCollision(arrowX, arrowY, enemyX, enemyY)
    if collision and arrow_state == "fire":
        arrow_Y = 400
        arrow_state = "ready"
        score += 1
        print(score)  

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()

