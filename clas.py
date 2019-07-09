import pygame
import settings



class Level:
    def __init__(self):
        self.level = settings.LEVEL


    def disp_level(self,screen):
        wall = pygame.image.load(settings.WALL).convert()
        bones = pygame.image.load(settings.BONES).convert_alpha()
        line_number =0
        for line in self.level:
            square_number = 0
            for sprite in line:
                x = square_number * settings.SPRITE_SIZE
                y = line_number * settings.SPRITE_SIZE
                if sprite == 1:
                    screen.blit(wall, (x,y))
                elif sprite == 2:
                    screen.blit(bones,(x,y))
                square_number += 1
            line_number += 1