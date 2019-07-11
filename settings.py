from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


SCREEN_SIZE = (645,645)

MACIMG = str(BASE_DIR / 'images' / 'MacGyver.png' )
BACKGROUND = str(BASE_DIR / 'images' / 'fond.png')
WALL = str(BASE_DIR / 'images' / 'wall.png')
BONES = str(BASE_DIR / 'images' / 'os.png')
GUARD = str(BASE_DIR / 'images' / 'Gardien.png')
NEEDLE = str(BASE_DIR / 'images' / 'needle.png')

SPRITE_SIZE = 43

LEVEL = [[4,0,1,4,4,4,4,4,4,4,4,4,4,4,1],
         [1,0,1,1,1,1,1,1,1,1,1,1,1,1,0],
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
