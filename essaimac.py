import pygame
import settings
import clas
pygame.init()
black = (0,0,0)


screen = pygame.display.set_mode(settings.SCREEN_SIZE)
background = pygame.image.load(settings.BACKGROUND).convert()

l = clas.Level()
screen.blit(background,(0,0))
l.disp_level(screen)

pygame.display.update()

launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False

pygame.quit()



"""
screen = pygame.display.set_mode(settings.SCREEN_SIZE)
pygame.key.set_repeat(30,10)

background = pygame.image.load(settings.BACKGROUND).convert()
screen.blit(background,(0,0))

MacGyver = pygame.image.load(settings.MACIMG).convert_alpha()
rect_mac = MacGyver.get_rect()

my_rect = pygame.Rect(200,0,300,300)
pygame.draw.rect(screen,black,my_rect)

screen.blit(MacGyver,rect_mac)


pygame.display.update()

launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
        if rect_mac.colliderect(my_rect):
            rect_mac = rect_mac.move(0,0)
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    rect_mac = rect_mac.move(-1,0)
                elif event.key == pygame.K_RIGHT:
                    rect_mac = rect_mac.move(1,0)
                elif event.key == pygame.K_UP:
                    rect_mac = rect_mac.move(0,1)
                elif event.key == pygame.K_DOWN:
                    rect_mac = rect_mac.move(0,1)


    screen.blit(background,(0,0))
    screen.blit(MacGyver,rect_mac)
    pygame.draw.rect(screen,black,my_rect)
    pygame.display.update()



        


pygame.quit()

"""