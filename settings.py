from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
SPRITE_SIZE = 43
SCREEN_SIZE = (15*SPRITE_SIZE,15*SPRITE_SIZE)

WHITE = (255,255,255)

MACIMG = str(BASE_DIR / 'images' / 'MacGyver.png' )
BACKGROUND = str(BASE_DIR / 'images' / 'fond.png')
WALL = str(BASE_DIR / 'images' / 'wall.png')
BONES = str(BASE_DIR / 'images' / 'os.png')
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
"""
LEVEL = [[4,0,1,4,4,4,4,4,4,4,4,4,4,4,1],
         [1,0,1,1,1,1,1,1,1,1,1,1,1,1,4],
         [1,0,0,1,0,1,0,0,1,0,0,0,0,0,1],
         [1,0,0,1,0,0,0,1,0,0,0,1,0,0,1],
         [1,0,1,1,0,1,0,1,0,0,0,1,0,0,1],
         [1,0,0,0,0,1,0,0,1,0,0,1,1,0,1],
         [1,0,1,0,0,1,0,0,1,0,1,0,0,0,1],
         [1,0,1,1,1,1,0,1,0,0,1,1,0,0,1],
         [1,0,0,1,0,0,0,0,1,0,1,0,0,0,1],
         [1,1,1,0,0,1,1,1,0,0,1,0,1,0,1],
         [1,0,0,0,0,1,0,1,0,1,4,1,0,0,0],
         [1,0,1,0,0,0,0,0,0,1,1,0,0,0,1],
         [1,0,0,1,1,1,1,1,1,0,1,0,1,0,1],
         [1,0,0,0,0,0,0,0,0,0,1,0,0,1,1],
         [1,1,1,1,1,1,1,1,1,1,2,1,0,0,3]]




'''
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
SPRITE_SIZE = 43
SCREEN_SIZE = (15*SPRITE_SIZE,15*SPRITE_SIZE)

MACIMG = str(BASE_DIR / 'images' / 'MacGyver.png' )
BACKGROUND = str(BASE_DIR / 'images' / 'fond.png')
WALL = str(BASE_DIR / 'images' / 'wall.png')
BONES = str(BASE_DIR / 'images' / 'os.png')
GUARD = str(BASE_DIR / 'images' / 'Gardien.png')
NEEDLE = str(BASE_DIR / 'images' / 'needle.png')
TUBE = str(BASE_DIR / 'images' / 'tube.png')
ETHER = str(BASE_DIR / 'images' / 'ether.png')

""" About 'LEVEL' : 0 == free square, and reachable by the character.
                    1 == a wall
                    2 == decoration (character can go over it)
                    3 == the guard
                    4 == free zone but not reachable (text zone)
"""
LEVEL = [[4,0,1,4,4,4,4,4,4,4,4,4,4,4,1],
         [1,0,1,1,1,1,1,1,1,1,1,1,1,1,4],
         [1,0,0,1,0,1,0,0,1,0,0,0,0,0,1],
         [1,0,0,1,0,0,0,1,0,0,0,1,0,0,1],
         [1,0,1,1,0,1,0,1,0,0,0,1,0,0,1],
         [1,0,0,0,0,1,0,0,1,0,0,1,1,0,1],
         [1,0,1,0,0,1,0,0,1,0,1,0,0,0,1],
         [1,0,1,1,1,1,0,1,0,0,1,1,0,0,1],
         [1,0,0,1,0,0,0,0,1,0,1,0,0,0,1],
         [1,1,1,0,0,1,1,1,0,0,1,0,1,0,1],
         [1,0,0,0,0,1,0,1,0,1,0,1,0,0,0],
         [1,0,1,0,0,0,0,0,0,1,1,0,0,0,1],
         [1,0,0,1,1,1,1,1,1,0,1,0,1,0,1],
         [1,0,0,0,0,0,0,0,0,0,1,0,0,1,1],
         [1,1,1,1,1,1,1,1,1,1,2,1,0,0,3]]

'''