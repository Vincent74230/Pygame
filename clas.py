import pygame
import settings
import random



class Level:
    """ Generates a labyrinth from a list in settings file, and 3 objects randomly
    in reachable areas of the labyrinth (see manual in settings file) """
    def __init__(self):
        self.level = settings.LEVEL
        self.object_coordinates = 0
        self.needle_x=0
        self.needle_y=0
        self.needle_pixel_x=0
        self.needle_pixel_y=0
        self.needle = pygame.image.load(settings.NEEDLE).convert_alpha()
        self.object_found = False

    def disp_level(self,screen):
        """Method that generates a labyrinth automaticly from a list named
        'LEVEL' in settings"""
        wall = pygame.image.load(settings.WALL).convert()
        bones = pygame.image.load(settings.BONES).convert_alpha()
        guard = pygame.image.load(settings.GUARD).convert_alpha()
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
                elif sprite == 3:
                    screen.blit(guard,(x,y))
                square_number += 1
            line_number += 1

    def rand_objects(self):
        """ Method that generates the coordinates of 3 objects in reachable areas
        of the labyrinth"""
        object_coordinates = [[0,0],[0,0],[0,0]]

        while self.level[object_coordinates[0][0]][object_coordinates[0][1]] != 0:
            object_coordinates[0][0] = random.randint(0,14)
            object_coordinates[0][1] = random.randint(0,14)
        
        for i in range(1,3):
            while self.level[object_coordinates[i][0]][object_coordinates[i][1]] != 0 and object_coordinates[i] != object_coordinates[i-1]:
                object_coordinates[i][0] = random.randint(0,14)
                object_coordinates[i][1] = random.randint(0,14)
                
        self.object_coordinates = object_coordinates
        print(self.object_coordinates)
        while self.level[self.needle_y][self.needle_x] != 0:
            self.needle_x = random.randint (0,14)
            self.needle_y = random.randint (0,14)
        self.needle_pixel_x = self.needle_x * settings.SPRITE_SIZE
        self.needle_pixel_y = self.needle_y * settings.SPRITE_SIZE


class MacGyver:
    """ Class that generates the character and its movements with keyboard"""
    def __init__(self):
        self.macimg = pygame.image.load(settings.MACIMG).convert_alpha()
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

    def found(self,object_position_x,object_position_y):
        """ Tests if character is actually on a random object position"""
        if self.sprite_x == object_position_x and self.sprite_y == object_position_y:
            return True
        






'''
import pygame
import settings
import random



class Level:
    """ Generates a labyrinth from a list in settings file, and 3 objects randomly
    in reachable areas of the labyrinth"""
    def __init__(self):
        self.level = settings.LEVEL
        self.needle_x=0
        self.needle_y=0
        self.needle_pixel_x=0
        self.needle_pixel_y=0
        self.needle = pygame.image.load(settings.NEEDLE).convert_alpha()
        self.object_found = False

    def disp_level(self,screen):
        """method which generates a labyrinth automaticly from a list in settings"""
        wall = pygame.image.load(settings.WALL).convert()
        bones = pygame.image.load(settings.BONES).convert_alpha()
        guard = pygame.image.load(settings.GUARD).convert_alpha()
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
                elif sprite == 3:
                    screen.blit(guard,(x,y))
                square_number += 1
            line_number += 1

    def rand_objects(self):
        """ Method that generates 3 objects and set those in reachable areas
        of the labyrinth"""
        while self.level[self.needle_y][self.needle_x] != 0:
            self.needle_x = random.randint (0,14)
            self.needle_y = random.randint (0,14)
        self.needle_pixel_x = self.needle_x * settings.SPRITE_SIZE
        self.needle_pixel_y = self.needle_y * settings.SPRITE_SIZE


class MacGyver:
    """ Class that generates the character and its movements with keyboard"""
    def __init__(self):
        self.macimg = pygame.image.load(settings.MACIMG).convert_alpha()
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

    def found(self,object_position_x,object_position_y):
        """ Tests if character is actually on a random object position"""
        if self.sprite_x == object_position_x and self.sprite_y == object_position_y:
            return True

'''