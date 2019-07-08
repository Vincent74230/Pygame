import pygame
import settings
pygame.init()


SIZE = (640,480)
x=0
y=0
x_change = 0
y_change = 0
black = (0,0,0)

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('MacGyver')
clock = pygame.time.Clock()

macimage = pygame.image.load(settings.MACIMG).convert()
fond = pygame.image.load(settings.BACKGROUND).convert()

def mac(x,y):
    screen.blit(macimage,(x,y))

launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                x_change = 5
            elif event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_UP:
                y_change = -5
            elif event.key == pygame.K_DOWN:
                y_change = 5
        if event.type == pygame.KEYUP:
            if event.type == pygame.K_LEFT or pygame.K_RIGHT:
                x_change = 0
            if event.type == pygame.K_UP or pygame.K_DOWN:
                y_change = 0

     
    x += x_change
    y += y_change
    
    screen.blit(fond,(0,0))
    mac(x,y)
    pygame.display.update()
    clock.tick(40)
    

pygame.quit()
quit()