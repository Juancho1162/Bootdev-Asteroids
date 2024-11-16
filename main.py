import pygame
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
from player import Player 


def main():
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    time = pygame.time.Clock()
    dt = 0
    

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0, 0, 0))
        
        for items in updatable:
            items.update(dt)

        for items in drawable:
            items.draw(screen)


        pygame.display.flip()





        time.tick(180)
        dt = time.tick(180)/1000




# The last lines ensures that main is only called by running this file.
# So it cannot be imported as a module.
if __name__ == "__main__":
    main()
