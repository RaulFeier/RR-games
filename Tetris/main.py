import pygame

pygame.init()

screen_width = 1080
screen_high = 1920

pygame.display.set_caption('Tetris');
win = pygame.display.set_mode((screen_width, screen_high))

run = True

# pictures  
back_ground= pygame.image.load('Tetris/Pictures/back_ground.png')

def Game_Window():
    win.blit(back_ground, (0, 0))
    font = pygame.font.SysFont('Fira code', 30)
    eep = font.render('il iubesc pe Raul',0 , ('Purple'))
    win.blit(eep, (screen_width // 2, screen_high // 2))
    pygame.display.update()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    Game_Window()


pygame.quit()
