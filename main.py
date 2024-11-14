import pygame
from constants import *
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT



def main():
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    time = pygame.time.Clock()
    dt = 0



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0, 0, 0))
        pygame.display.flip()


        time.tick(60)
        dt = time.tick(60)/1000












# The last lines ensures that main is only called by running this file.
# So it cannot be imported as a module.
if __name__ == "__main__":
    main()
