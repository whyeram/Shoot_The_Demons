#arrow
arrow_img = pygame.image.load('arrow.png')
arrowX = 0
arrowY = 400
arrowX_change = 0
arrowY_change = 15
arrow_state = "ready" #ready - you can't see the bullet on the screen
                       #fire - The bullet is currently moving
 #method for shooting the arrow
def shoot_arrow(x, y):
    global arrow_state
    arrow_state = "fire"
    screen.blit(arrow_img, (x + 2 , y + 9))
