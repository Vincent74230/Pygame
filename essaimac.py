
import pygame
pygame.init()

SIZE = (640,480)
x=0
y=0
x_change = 0
colour = (50,50,50)

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('MacGyver')
clock = pygame.time.Clock()

macimage = pygame.image.load("MacGyver.png")

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
                #x += x_change
            elif event.key == pygame.K_LEFT:
                x_change = -5
                #x -= x_change
        if event.type == pygame.KEYUP:
            if event.type == pygame.K_LEFT or pygame.K_RIGHT:
                x_change = 0
     
    x += x_change
    pygame.display.update()
    clock.tick(60)
    mac(x,y)

pygame.quit()
quit()
