import pygame
import settings
import random
from collections import namedtuple


class Rand_items:
    def __init__(self,n):
        self.level = settings.LEVEL
        self.n = n
        self.item_coordinates = 0
        self.item_coordinates_pixel = 0
        self.needle = pygame.image.load(settings.NEEDLE).convert_alpha()
        self.ether = pygame.image.load(settings.ETHER).convert_alpha()
        self.tube = pygame.image.load(settings.TUBE).convert_alpha()
        self.sprite = 0
        self.pixel = 0
        self.needle_found = False
        self.ether_found = False
        self.tube_found = False
        self.all_items_found = False

    def rand_items(self):
        item_coordinates = []
        item_coordinates_pixel = []
        for i in range(0,self.n):
            item_coordinates.append([0,0])
            item_coordinates_pixel.append([0,0])

        while self.level[item_coordinates[0][0]][item_coordinates[0][1]] != 0:
        # We generate the first couple X,Y of coordinates in the random list (initialisation)
            item_coordinates[0][0] = random.randint(0,14)
            item_coordinates[0][1] = random.randint(0,14)

        for i in range(1,self.n):
        # Generation of n other couples of coordinates : according to the amount of random items we want to set up in the maze
            while self.level[item_coordinates[i][0]][item_coordinates[i][1]] != 0 and item_coordinates[i] != item_coordinates[i-1]:
                item_coordinates[i][0] = random.randint(0,14)
                item_coordinates[i][1] = random.randint(0,14)
        self.item_coordinates = item_coordinates
        
        for i in range (0,self.n):
        # Generation of an equivalent of the previous list, but in pixels (edible by blit..)
            item_coordinates_pixel[i][0] = item_coordinates[i][0] * settings.SPRITE_SIZE
            item_coordinates_pixel[i][1] = item_coordinates[i][1] * settings.SPRITE_SIZE

        for i in range (0,self.n):
        # Coordinates to give to blit must be : [y,x], not [x,y]
            item_coordinates[i].reverse()
            item_coordinates_pixel[i].reverse()

        self.item_coordinates_pixel = item_coordinates_pixel
        
        Sprite = namedtuple('Sprite',['needle','ether','tube'])
        sprite = Sprite(self.item_coordinates[0],self.item_coordinates[1],self.item_coordinates[2])
        #print (coords.needle)
        Pixel = namedtuple('Pixel',['needle','ether','tube'])
        pixel = Pixel(self.item_coordinates_pixel[0],self.item_coordinates_pixel[1],self.item_coordinates_pixel[2])
        
        self.sprite = sprite
        self.pixel = pixel

    def find_items(self,screen,y,x):

        if y == self.sprite.needle[0] and x == self.sprite.needle[1]:
            self.needle_found = True
        if y == self.sprite.ether[0] and x == self.sprite.ether[1]:
            self.ether_found = True
        if y == self.sprite.tube[0] and x == self.sprite.tube[1]:
            self.tube_found = True

    def disp_items(self,screen):
        if self.needle_found == False:
            screen.blit(self.needle,(self.pixel.needle))
        else:
            screen.blit(self.needle,(13*settings.SPRITE_SIZE,0))

        if self.ether_found == False:
            screen.blit(self.ether,(self.pixel.ether))
        else:
            screen.blit(self.ether,(12*settings.SPRITE_SIZE,0))

        if self.tube_found == False:
            screen.blit(self.tube,(self.pixel.tube))
        else:
            screen.blit(self.tube,(11*settings.SPRITE_SIZE,0))


        if self.needle_found == True and self.ether_found == True and self.tube_found == True : 
            self.all_items_found = True
            