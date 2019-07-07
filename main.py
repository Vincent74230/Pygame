import pygame
import settings
x = 0
y = 0
x_change =0
y_change =0
black = (0,0,0)


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(settings.SCREEN_SIZE)
        self.macgyver = pygame.image.load("MacGyver.png")
        self.launched = True


    def mac(self,x,y):
        self.screen.blit(self.macgyver,(x,y))
        pygame.display.update()


    def quit(self):  #fonction that manages the exit button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.launched = False
                


    def moves(self):
        for event in pygame.event.get(pygame.KEYDOWN):
            if event.key == pygame.K_DOWN:
                print("On va en bas")
            elif event.key == pygame.K_UP:
                print("On va en haut")
            elif event.key == pygame.K_LEFT:
                print("On va a gauche")
            else:
                print("On va a droite")


def main():
    game = Game()
    while game.launched:
        game.quit()
        game.mac(x,y)
    pygame.quit()


if __name__ == "__main__":
    main()