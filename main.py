import pygame, sys
from settings import *
from level import Level


class Game:

    def __init__(self):
        pygame.init()
        # Create display
        self.screen = pygame.display.set_mode((Screen_Width, Screen_Height))
        # Changing the window name
        pygame.display.set_caption('The Land')
        # Creating the clock
        self.clock = pygame.time.Clock()
        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                # Checking if user closed the game
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            # Time keeping
            dt = self.clock.tick() / 1000
            self.level.run(dt)
            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()
