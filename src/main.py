import pygame
import sys
from game.game_logic import Game

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("贪吃蛇游戏")

    game = Game()
    game.start_game()

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.end_game()
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                game.change_direction(event.key)

        game.update()
        game.draw(screen)
        pygame.display.flip()
        clock.tick(15)

if __name__ == "__main__":
    main()