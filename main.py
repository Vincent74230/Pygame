import sys
import pygame
import settings



class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(settings.SCREEN_SIZE)

    def start(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

def main():
    game = Game()
    game.start()
    


if __name__ == "__main__":
    main()