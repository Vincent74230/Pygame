import pygame
import settings


class Character:
    """ Class that generates the character and its movements with keyboard"""
    def __init__(self):
        self.image = pygame.image.load(settings.MACIMG).convert_alpha()
        self.level = settings.LEVEL
        self.sprite_x = 0
        self.sprite_y = 0
        self.x = 0
        self.y = 0
        
    def moves(self,move):
        """ Method that allows character to move with keyboard"""
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

    def disp_character(self,screen):
        screen.blit(self.image,(self.x,self.y))

    '''              

    def found(self,object_position_x,object_position_y):
        """ Tests if character is currently on a random object position"""
        if self.sprite_x == object_position_x and self.sprite_y == object_position_y:
            return True
    '''