
import pygame as pg
from game.game import Game
from game.menu import StartMenu, GameMenu


def main():

    running = True

    pg.init()
    pg.mixer.init()
    screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
    clock = pg.time.Clock()

    # implement menus
    start_menu = StartMenu(screen, clock)
    game_menu = GameMenu(screen, clock)

    # implement game
    game = Game(screen, clock)

    while running:

        # start menu goes here
        playing = start_menu.run()

        while playing:
            # game loop here
            game.run()
            # pause loop here
            playing = game_menu.run()

if __name__ == "__main__":
    main()

