#  I will try my best to comment this code as profusely as I can
#  so you will be able to follow along.

import sys
import pygame

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

        # README: temporarily messing around with moving characters
        self.test_img = pygame.image.load("data\\images\\Main Characters\\Mask Dude\\Idle (32x32).png").convert_alpha()
        self.test_img_pos = pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2)
        self.movement = [False, False]

        # Testing getting a frame from a sprite sheet
        self.frame_0 = self.get_sprite(self.test_img, 32, 32)

    def run(self):
        # We are going to use one loop for physics, rendering, etc. 
        while True:
            # Reset frames
            self.screen.fill((14, 219, 248))

            # Setting a means of moving the character, booleans are converted to integers
            # implicitly. So False = 0 and True = 1. We use this to see how much position should be changed by
            self.test_img_pos[1] += self.movement[1] - self.movement[0]

            # Adding character to the screen
            self.screen.blit(self.frame_0, self.test_img_pos)

            # Loop for input handling. Application will not respond without this loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                # When key is being pressed down, start moving
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.movement[0] = True
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = True

                # When key is being lifted up, stop moving   
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.movement[0] = False
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = False

            # This line refreshes the screen. Failing to include this line will leave the screen black
            pygame.display.update()

            # Setting loop to 60 fps
            self.clock.tick(60)

    def get_sprite(self, sheet, width, height):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(sheet, (0, 0), (0, 0, width, height))
        return image


Game().run()

# TODO: Finish adding movement functionality. Adding events functionality
# I was thinking we use wasd for movement and x and c for events
# Collision detection and overall physics implementation