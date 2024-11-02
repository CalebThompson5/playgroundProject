#  I will try my best to comment this code as profusely as I can
#  so you will be able to follow along.

import sys
import pygame
from scripts.entities import PhysicsEtity 

# Here we are creating a class for the game. This will make things much easier to work with.
class Game:
    def __init__(self) -> None:
        # Initializing pygame
        pygame.init()

        # Here we are setting the panel for the game. The resolution (in pixels) is being passed in as a tuple
        self.screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Platformer Game")

        # Creating a clock so we can set a frame rate. We are gonna use a fixed frame rate (60fps) so the game doesn't eat CPU
        self.clock = pygame.time.Clock()

        self.movement = [False, False]

        self.player = PhysicsEtity(self, 'player', (50, 50), (32, 32))

    def run(self):
        # We are going to use one loop for physics, rendering, etc. 
        while True:
            # Reset frames
            self.screen.fill((14, 219, 248))

            self.player.update((self.movement[1] - self.movement[0], 0))
            self.player.render(self.screen)

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