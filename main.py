import pygame
import settings
import clas
pygame.init()
black = (0,0,0)


screen = pygame.display.set_mode(settings.SCREEN_SIZE)
background = pygame.image.load(settings.BACKGROUND).convert()

l = clas.Level()
mac = clas.MacGyver()
"""
screen.blit(background,(0,0))
l.disp_level(screen)
mac.moves(screen)
"""
pygame.display.update()

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

    pygame.time.Clock().tick(30)                
    screen.blit(background,(0,0))
    l.disp_level(screen)
    screen.blit(mac.mac,(mac.x,mac.y))
    pygame.display.update()


pygame.quit()
