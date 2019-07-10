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


class MacGyver:
    def __init__(self):
        self.mac = pygame.image.load(settings.MACIMG).convert_alpha()
        self.level = settings.LEVEL
        self.sprite_x = 0
        self.sprite_y = 0
        self.x = 0
        self.y = 0
        

    def moves(self,move):
        if move == 'right':
            if self.sprite_x<14:
                if self.level[self.sprite_y][self.sprite_x+1] != 1:
                    self.sprite_x +=1
                    self.x = self.sprite_x * settings.SPRITE_SIZE

        if move == 'left':
            if self.sprite_x>0:
                if self.level[self.sprite_y][self.sprite_x-1] != 1:
                    self.sprite_x -=1
                    self.x = self.sprite_x * settings.SPRITE_SIZE

        if move == 'up':
            if self.sprite_y>0:
                if self.level[self.sprite_y-1][self.sprite_x] != 1:
                    self.sprite_y -= 1
                    self.y = self.sprite_y * settings.SPRITE_SIZE

        if move == 'down':
            if self.sprite_y < 14:
                if self.level[self.sprite_y+1][self.sprite_x] !=1:
                    self.sprite_y +=1
                    self.y = self.sprite_y * settings.SPRITE_SIZE
