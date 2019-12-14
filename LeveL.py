'''class 'level' which take a list named 'level' in settings.
- method disp_level which displays level on the screen from a list on settings
- method 'message' which displays welcome message, win and loose message on the screen'''
import pygame
import settings


class Level:
    """ Generates a labyrinth from a list in settings file, and 3 objects randomly
    in reachable areas of the labyrinth (see manual in settings file) """
    def __init__(self, level):
        self.level = level
        self.background = pygame.image.load(settings.BACKGROUND).convert()
        self.wall = pygame.image.load(settings.WALL).convert()
        self.bones = pygame.image.load(settings.BONES).convert_alpha()
        self.skeleton = pygame.image.load(settings.SKELETON).convert_alpha()
        self.guard = pygame.image.load(settings.GUARD).convert_alpha()
        self.sign = pygame.image.load(settings.SIGN).convert_alpha()

    def disp_level(self, screen):
        """Method that blits background and generates a labyrinth automaticly from a list 'level'
        in settings"""

        screen.blit(self.background, (0, 0))

        line_number = 0
        for line in self.level:
            square_number = 0
            for sprite in line:
                x = square_number * settings.SPRITE_SIZE
                y = line_number * settings.SPRITE_SIZE
                if sprite == 1:
                    screen.blit(self.wall, (x, y))
                elif sprite == 2:
                    screen.blit(self.bones, (x, y))
                elif sprite == 3:
                    screen.blit(self.guard, (x, y))
                elif sprite == 5:
                    screen.blit(self.skeleton, (x, y))
                elif sprite == 6:
                    screen.blit(self.sign, (x, y))
                square_number += 1
            line_number += 1

    def message(self, screen, listt):
        """ Method that displays a message on the screen for 3 seconds,
        it takes a list as parameter"""
        n = len(listt)
        for i in range(0, n):
            screen.blit(self.background, (0, 0))
            screen.blit(listt[i], (0, 200))
            pygame.display.update()
            pygame.time.delay(3000)
