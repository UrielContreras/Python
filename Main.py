import pygame

from src.Menu import Menu
from src.main_game import MainGame

if __name__ == "__main__":
    menu = Menu()
    action = menu.run()

    if action == "play":
        game = MainGame()
        game.run()
    else:
        pygame.quit()