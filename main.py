import sys
import pygame
import settings



class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(settings.SCREEN_SIZE)

    def start(self):
        while 1:  #main loop of the game
            self.quit()

    def quit(self):  #fonction which manages the quit button
        for event in pygame.event.get(pygame.QUIT):
            sys.exit()

    def moves(self):
        

def main():
    game = Game()
    game.start()
    


if __name__ == "__main__":
    main()