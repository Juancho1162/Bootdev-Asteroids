import pygame
import sys
from asteroidfield import AsteroidField
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_SHOOT_SPEED
from player import Player 
from asteroid import Asteroid
from shoot import Shoot


def main():
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    time = pygame.time.Clock()
    dt = 0
    

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    aster_grp = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Shoot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable) 
    Asteroid.containers = (aster_grp, updatable, drawable) 
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0, 0, 0)) 
        
        for items in updatable:
            items.update(dt)

        for items in aster_grp:
            if items.colide(player):
                print("Game over!")
                sys.exit()

        for items in drawable:
            items.draw(screen)

        for asteroid in aster_grp:
            for bullet in shots:
                if asteroid.colide(bullet):
                    bullet.kill()
                    asteroid.split()


        pygame.display.flip()





        time.tick(180)
        dt = time.tick(180)/1000




# The last lines ensures that main is only called by running this file.
# So it cannot be imported as a module.
if __name__ == "__main__":
    main()
