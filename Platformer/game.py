import sys
import pygame

from scripts.utils import load_image, load_images
from scripts.entities import PhysicsEtity
from scripts.tilemap import Tilemap

class Game:
    def __init__(self) -> None:

        pygame.init()

        # Here we are setting the panel for the game. The resolution (in pixels) is being passed in as a tuple
        self.screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Platformer Game")

        # Creating a clock so we can set a frame rate. We are gonna use a fixed frame rate (60fps) so the game doesn't eat CPU
        self.clock = pygame.time.Clock()

        self.movement = [False, False]

        # Images to be loaded in
        self.assets = {
            'decor': load_images('tiles/decor'),
            'grass': load_images('tiles/grass'),
            'large_decor': load_images('tiles/large_decor'),
            'stone': load_images('tiles/stone'),
            'player': load_image('entities/player.png')
        }

        self.player = PhysicsEtity(self, 'player', (50, 50), (8, 15))

        self.tilemap = Tilemap(self, tile_size = 16)

    def run(self):
        # We are going to use one loop for physics, rendering, etc. 
        while True:
            # Reset frames
            self.screen.fill((14, 219, 248))

            self.tilemap.render(self.screen)

            # update location of player in the x direction
            self.player.update(self.tilemap, (self.movement[1] - self.movement[0], 0))
            self.player.render(self.screen)

            # print(self.tilemap.physics_rects_around(self.player.pos))
            # print(self.player.pos)

            # Loop for input handling. Application will not respond without this loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # When key is being pressed down, start moving   
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                    if event.key == pygame.K_UP:
                        self.player.velocity[1] = -3

                # When key is being lifted up, stop moving   
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False

            # This line refreshes the screen. Failing to include this line will leave the screen black
            pygame.display.update()

            # Setting loop to 60 fps
            self.clock.tick(60)


Game().run()

# TODO: Finish adding movement functionality. Adding events functionality
# I was thinking we use wasd for movement and x and c for events
# Collision detection and overall physics implementation