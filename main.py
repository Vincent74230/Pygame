import sys
import pygame
import settings
x = 0
y = 0

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(settings.SCREEN_SIZE)
        self.macgyver = pygame.image.load("MacGyver.png")
        self.screen.blit(self.macgyver,(x,y))
        pygame.display.update()

    def start(self):
        while 1:  #main loop of the game
            self.quit()
            self.moves()

    def quit(self):  #fonction which manages the quit button
        for event in pygame.event.get(pygame.QUIT):
            sys.exit()

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
    game.start()
    


if __name__ == "__main__":
    main()