'''Module that contains the main loop of the game'''
import pygame
import LeveL
import settings
import rand_items
import character

def main():
    """ Main contains pygame init, screen init, main loop and manages end of game """
    pygame.init()

    screen = pygame.display.set_mode(settings.SCREEN_SIZE)
    pygame.display.set_caption("Projet 3 de Vincent NOWACZYK : MacGyver")
    level = LeveL.Level(settings.LEVEL)
    macgyver = character.Character(settings.LEVEL)
    items = rand_items.Rand_items(settings.LEVEL)
    items.rand_items()

    level.message(screen, settings.LIST_MESS)

    launched = True
    while launched:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                launched = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    macgyver.moves('right')
                if event.key == pygame.K_LEFT:
                    macgyver.moves('left')
                if event.key == pygame.K_UP:
                    macgyver.moves('up')
                if event.key == pygame.K_DOWN:
                    macgyver.moves('down')

        level.disp_level(screen)
        macgyver.disp_character(screen)
        items.find_items(macgyver.sprite_x, macgyver.sprite_y)
        items.disp_items(screen)
        if level.level[macgyver.sprite_x][macgyver.sprite_y] == 3:
            if items.all_items_found:
                level.message(screen, settings.YOU_WIN)
                launched = False
            else:
                level.message(screen, settings.YOU_LOOSE)
                launched = False

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
