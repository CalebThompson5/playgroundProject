#  I will try my best to comment this code as profusely as I can
#  so you will be able to follow along.

import sys
import pygame

# Initializing pygame
pygame.init()

# Here we are setting the panel for the game. The resolution (in pixels) is being passed in as a tuple
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Platformer Game")

# Creating a clock so we can set a frame rate. We are gonna use a fixed frame rate (60fps) so the game doesn't eat CPU
clock = pygame.time.Clock()

# We are going to use one loop for physics, rendering, etc. 
while True:
    # Loop for input handling. Application will not respond without this loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # This line refreshes the screen. Failing to include this line will leave the screen black
    pygame.display.update()

    # Setting loop to 60 fps
    clock.tick(60)

    