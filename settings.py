'''Module that contains the constants of the game, images and levels'''
from pathlib import Path
import pygame
pygame.init()


BASE_DIR = Path(__file__).resolve().parent
SPRITE_SIZE = 43
SCREEN_SIZE = (15*SPRITE_SIZE, 15*SPRITE_SIZE)

WHITE = (255, 255, 255)

ARIAL_FONT = pygame.font.SysFont("arial", 40)
ARIAL_FONT_B = pygame.font.SysFont("arial", 35)
MESSAGE_1 = ARIAL_FONT.render("MacGyver has been trapped !!!", False, WHITE)
MESSAGE_2 = ARIAL_FONT.render("The only way out is guarded..", False, WHITE)
MESSAGE_3 = ARIAL_FONT.render("Help MacGyver to escape", False, WHITE)
WIN = ARIAL_FONT.render("You win !!!", False, WHITE)
LOOSE = ARIAL_FONT.render("You loose...", False, WHITE)
LIST_MESS = [MESSAGE_1, MESSAGE_2, MESSAGE_3]
YOU_WIN = [WIN]
YOU_LOOSE = [LOOSE]
COUNTER_0 = ARIAL_FONT_B.render("Items found : 0/3", False, WHITE)
COUNTER_1 = ARIAL_FONT_B.render("Items found : 1/3", False, WHITE)
COUNTER_2 = ARIAL_FONT_B.render("Items found : 2/3", False, WHITE)
COUNTER_3 = ARIAL_FONT_B.render("Items found : 3/3", False, WHITE)

MACIMG = str(BASE_DIR / 'images' / 'MacGyver.png')
BACKGROUND = str(BASE_DIR / 'images' / 'fond.png')
WALL = str(BASE_DIR / 'images' / 'wall.png')
BONES = str(BASE_DIR / 'images' / 'os.png')
SKELETON = str(BASE_DIR / 'images' / 'skeleton.png')
SIGN = str(BASE_DIR / 'images'/ 'sign.png')
GUARD = str(BASE_DIR / 'images' / 'Gardien.png')

"""About lines that follow : those are random items to set up on the maze"""
NEEDLE = str(BASE_DIR / 'images' / 'needle.png')
TUBE = str(BASE_DIR / 'images' / 'tube.png')
ETHER = str(BASE_DIR / 'images' / 'ether.png')

""" About 'LEVEL' : 0 == free square, and reachable by the character.
                    1 == a wall
                    2 == decoration (character can go over it)
                    3 == the guard
                    4 == free zone but not reachable (text zone)
                    5 == decoration
                    6 == sign
"""
LEVEL = [[4, 0, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1],
         [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6],
         [1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
         [1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
         [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1],
         [1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1],
         [1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1],
         [1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
         [1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
         [1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 5, 1, 0, 0, 0],
         [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
         [1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 0, 0, 3]]
