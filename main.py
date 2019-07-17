import pygame
import settings
import level
import rand_items
import character
pygame.init()


screen = pygame.display.set_mode(settings.SCREEN_SIZE)
pygame.display.set_caption("Projet 3 de Vincent NOWACZYK : MacGyver")
arial_font = pygame.font.SysFont("arial",50)
you_win = arial_font.render("You Won !!!",False,settings.WHITE)
level = level.Level(settings.LEVEL)  
macgyver = character.Character()
items = rand_items.Rand_items(3)
items.rand_items()


launched = True
while launched:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                macgyver.moves('right')
            if event.key == pygame.K_LEFT:
                macgyver.moves ('left')
            if event.key == pygame.K_UP:
                macgyver.moves('up')
            if event.key == pygame.K_DOWN:
                macgyver.moves ('down')


    level.disp_level(screen)
    macgyver.disp_character(screen)
    items.find_items(screen,macgyver.sprite_x,macgyver.sprite_y)
    items.disp_items(screen)
    if level.level[macgyver.sprite_x][macgyver.sprite_y] == 3:
        if items.all_items_found == True:
            screen.blit(you_win,(320,320))
            launched = False
        else:
            launched = False







    '''

    screen.blit(background,(0,0))
    level.disp_level(screen)
    screen.blit(macgyver.image,(macgyver.x,macgyver.y))
    screen.blit(items.needle,items.coords_pixel.needle_pix)
    
    
    if mac.found(level.needle_x,level.needle_y) == True:
        level.object_found = True
    if level.object_found == False:
        screen.blit(level.needle,(level.needle_pixel_x,level.needle_pixel_y))
    else:
        screen.blit(level.needle,(13*settings.SPRITE_SIZE,0))
    if mac.level[mac.sprite_x][mac.sprite_y] == 3:
        if level.object_found == True:
            screen.blit(you_win,(320,320))
            launched = False
        else:
            launched = False
            '''
    pygame.display.update()


pygame.quit()




'''
import pygame
import settings
import clas
pygame.init()


white = (255,255,255)
screen = pygame.display.set_mode(settings.SCREEN_SIZE)
background = pygame.image.load(settings.BACKGROUND).convert()
pygame.display.set_caption("Projet 3 de Vincent NOWACZYK : MacGyver")
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
            launched = False
        else:
            launched = False
    pygame.display.update()


pygame.quit()

'''