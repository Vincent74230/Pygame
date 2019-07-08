import pygame
import settings
black = (0,0,0)
clock = pygame.time.Clock()


class Game:
    """ Class which contains all the attributes of the game"""
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(settings.SCREEN_SIZE)
        self.macgyver = pygame.image.load(settings.MACIMG)
        self.launched = True


    def mac(self,tupl):
        self.screen.blit(self.macgyver,tupl)
        #self.screen.fill(black)
        pygame.display.update()


    def quit(self):  #fonction that manages the exit button
            if event.type == pygame.QUIT:
                self.launched = False
                
"""
    def moves(self):
        x,y = 0,0
        x_change,y_change = 0,0
        if event.key == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_change = -5
            elif event.key == pygame.K_DOWN:
                y_change = 5
        y += y_change
        return x,y
   """     


def main():
    game = Game()
    while game.launched:
        for event in pygame.event.get():
            game.quit()
            game.mac(0,0)
        
    pygame.quit()


if __name__ == "__main__":
    main()