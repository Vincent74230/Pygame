'''class Rand_items:
-Method rand_items which generates coordinates of n items randomly in the maze,
according to the list 'level'.
-Method find_items : takes the character position as parameter,
and compares it to random items.
-Method disp_items which displays items according weather they are found or not.'''
import pygame
import settings
import random
from collections import namedtuple

class Rand_items:
    ''' Class that generates n rand items on the maze'''
    def __init__(self,level):
        self.level = level
        self.item_coordinates = []
        self.item_coordinates_pixel = []
        self.sprite = 0
        self.pixel = 0
        self.needle_found = False
        self.ether_found = False
        self.tube_found = False
        self.all_items_found = False

    def rand_items(self):
        ''' Method that generates n random items, and updates class attributes'''
        for i in range(0, 3):
            self.item_coordinates.append([0, 0])
            self.item_coordinates_pixel.append([0, 0])

        while self.level[self.item_coordinates[0][0]][self.item_coordinates[0][1]] != 0:
        # We generate the first couple X,Y of coordinates in the random list (initialisation)
            self.item_coordinates[0][0] = random.randint(0, 14)
            self.item_coordinates[0][1] = random.randint(0, 14)

        for i in range(1, 3):
        # Generation of 2 other couples of coordinates :
            while self.level[self.item_coordinates[i][0]][self.item_coordinates[i][1]] != 0\
            and self.item_coordinates[i] != self.item_coordinates[i-1]:
                self.item_coordinates[i][0] = random.randint(0, 14)
                self.item_coordinates[i][1] = random.randint(0, 14)

        for i in range(0, 3):
        # Generation of an equivalent of the previous list, but in pixels (edible by blit..)
            self.item_coordinates_pixel[i][0] = self.item_coordinates[i][0] * settings.SPRITE_SIZE
            self.item_coordinates_pixel[i][1] = self.item_coordinates[i][1] * settings.SPRITE_SIZE

        for i in range(0, 3):
         #Coordinates to give to blit must be : [y, x], not [x, y]
            self.item_coordinates[i].reverse()
            self.item_coordinates_pixel[i].reverse()

    def find_items(self ,y, x):
        '''Method which compares character position to item position, update a bool in attibutes'''
        if y == self.item_coordinates[0][0] and x == self.item_coordinates[0][1]:
            self.needle_found = True
        if y == self.item_coordinates[1][0] and x == self.item_coordinates[1][1]:
            self.ether_found = True
        if y == self.item_coordinates[2][0] and x == self.item_coordinates[2][1]:
            self.tube_found = True

    def disp_items(self, screen):
        '''Method that displays random items on the screen, according weather 
        they are found or not'''
        needle = pygame.image.load(settings.NEEDLE).convert_alpha()
        ether = pygame.image.load(settings.ETHER).convert_alpha()
        tube = pygame.image.load(settings.TUBE).convert_alpha()

        if self.needle_found == False:
            screen.blit(needle, (self.item_coordinates_pixel[0]))
        else:
            screen.blit(needle, (13*settings.SPRITE_SIZE, 0))

        if self.ether_found == False:
            screen.blit(ether, (self.item_coordinates_pixel[1]))
        else:
            screen.blit(ether, (12*settings.SPRITE_SIZE, 0))

        if self.tube_found == False:
            screen.blit(tube, (self.item_coordinates_pixel[2]))
        else:
            screen.blit(tube, (11*settings.SPRITE_SIZE, 0))

        if self.needle_found == True and self.ether_found == True and self.tube_found == True: 
            self.all_items_found = True





"""
class Rand_items:
    ''' Class that generates n rand items on the maze'''
    def __init__(self,level):
        self.level = level
        self.item_coordinates = []
        self.item_coordinates_pixel = []
        self.sprite = 0
        self.pixel = 0
        self.needle_found = False
        self.ether_found = False
        self.tube_found = False
        self.all_items_found = False

    def rand_items(self):
        ''' Method that generates n random items, and updates class attributes'''
        for i in range(0, 3):
            self.item_coordinates.append([0, 0])
            self.item_coordinates_pixel.append([0, 0])

        while self.level[self.item_coordinates[0][0]][self.item_coordinates[0][1]] != 0:
        # We generate the first couple X,Y of coordinates in the random list (initialisation)
            self.item_coordinates[0][0] = random.randint(0, 14)
            self.item_coordinates[0][1] = random.randint(0, 14)

        for i in range(1, 3):
        # Generation of 3 other couples of coordinates :
            while self.level[self.item_coordinates[i][0]][self.item_coordinates[i][1]] != 0\
            and self.item_coordinates[i] != self.item_coordinates[i-1]:
                self.item_coordinates[i][0] = random.randint(0, 14)
                self.item_coordinates[i][1] = random.randint(0, 14)

        for i in range(0, 3):
        # Generation of an equivalent of the previous list, but in pixels (edible by blit..)
            self.item_coordinates_pixel[i][0] = self.item_coordinates[i][0] * settings.SPRITE_SIZE
            self.item_coordinates_pixel[i][1] = self.item_coordinates[i][1] * settings.SPRITE_SIZE

        for i in range(0, 3):
        # Coordinates to give to blit must be : [y, x], not [x, y]
            self.item_coordinates[i].reverse()
            self.item_coordinates_pixel[i].reverse()

        Sprite = namedtuple('Sprite', ['needle', 'ether', 'tube'])
        sprite = Sprite(self.item_coordinates[0], self.item_coordinates[1], self.item_coordinates[2])
        Pixel = namedtuple('Pixel', ['needle', 'ether', 'tube'])
        pixel = Pixel(self.item_coordinates_pixel[0], self.item_coordinates_pixel[1], \
            self.item_coordinates_pixel[2])

        self.sprite = sprite
        self.pixel = pixel

    def find_items(self ,y, x):
        '''Method which compares character position to item position, update a bool in attibutes'''
        if y == self.sprite.needle[0] and x == self.sprite.needle[1]:
            self.needle_found = True
        if y == self.sprite.ether[0] and x == self.sprite.ether[1]:
            self.ether_found = True
        if y == self.sprite.tube[0] and x == self.sprite.tube[1]:
            self.tube_found = True

    def disp_items(self, screen):
        '''Method that displays random items on the screen, according weather 
        they are found or not'''
        needle = pygame.image.load(settings.NEEDLE).convert_alpha()
        ether = pygame.image.load(settings.ETHER).convert_alpha()
        tube = pygame.image.load(settings.TUBE).convert_alpha()

        if self.needle_found == False:
            screen.blit(needle, (self.pixel.needle))
        else:
            screen.blit(needle, (13*settings.SPRITE_SIZE, 0))

        if self.ether_found == False:
            screen.blit(ether, (self.pixel.ether))
        else:
            screen.blit(ether, (12*settings.SPRITE_SIZE, 0))

        if self.tube_found == False:
            screen.blit(tube, (self.pixel.tube))
        else:
            screen.blit(tube, (11*settings.SPRITE_SIZE, 0))

        if self.needle_found == True and self.ether_found == True and self.tube_found == True: 
            self.all_items_found = True
"""