import pygame
from constants import *
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT

def main():
    
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0, 0, 0))
        pygame.display.flip()












# The last lines ensures that main is only called by running this file.
# So it cannot be imported as a module.
if __name__ == "__main__":
    main()
