import pygame
import settings
import clas
pygame.init()


white = (255,255,255)
screen = pygame.display.set_mode(settings.SCREEN_SIZE)
background = pygame.image.load(settings.BACKGROUND).convert()
pygame.display.set_caption("Projet 3 de Vincent : MacGyver")
arial_font = pygame.font.SysFont("arial",50)
you_win = arial_font.render("You Won !!!",False,white)

level = clas.Level()  
mac = clas.MacGyver()
level.rand_objects()

launched = True
while launched:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                mac.moves('right')
            if event.key == pygame.K_LEFT:
                mac.moves ('left')
            if event.key == pygame.K_UP:
                mac.moves('up')
            if event.key == pygame.K_DOWN:
                mac.moves ('down')

    screen.blit(background,(0,0))
    level.disp_level(screen)
    screen.blit(mac.macimg,(mac.x,mac.y))
    if mac.found(level.needle_x,level.needle_y) == True:
        level.object_found = True
    if level.object_found == False:
        screen.blit(level.needle,(level.needle_pixel_x,level.needle_pixel_y))
    else:
        screen.blit(level.needle,(13*settings.SPRITE_SIZE,0))
    if mac.level[mac.sprite_x][mac.sprite_y] == 3:
        if level.object_found == True:
            screen.blit(you_win,(320,320))
        else:
            launched = False
    pygame.display.update()


pygame.quit()
