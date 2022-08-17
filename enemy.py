#Enemy
enemy_img = pygame.image.load('enemy.png')
enemyX = random.randint(0, 736)
enemyY = random.randint(50, 150)
enemyX_change = 0
def enemy(x, y):
    screen.blit(enemy_img, (x, y))
