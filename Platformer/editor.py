import sys
import pygame

from scripts.utils import load_images, Animation
from scripts.tilemap import Tilemap

RENDER_SCALE = 2.0

class Editor:
    def __init__(self) -> None:

        pygame.init()

        # Here we are setting the panel for the game. The resolution (in pixels) is being passed in as a tuple
        self.screen = pygame.display.set_mode((640, 480))
        self.display = pygame.Surface((320, 240))
        pygame.display.set_caption("Editor")

        # Creating a clock so we can set a frame rate. We are gonna use a fixed frame rate (60fps) so the game doesn't eat CPU
        self.clock = pygame.time.Clock()

        self.movement = [False, False]

        # Images to be loaded in
        self.assets = {
            'decor': load_images('tiles/decor'),
            'grass': load_images('tiles/grass'),
            'large_decor': load_images('tiles/large_decor'),
            'stone': load_images('tiles/stone'),
            'player': load_image('entities/player.png'),
            'background': load_image('background.png'),
            'clouds': load_images('clouds'),
            'player/idle': Animation(load_images('entities/player/idle'), img_dur = 6),
            'player/run': Animation(load_images('entities/player/run'), img_dur = 4),
            'player/jump': Animation(load_images('entities/player/jump'), img_dur = 5),
            'player/slide': Animation(load_images('entities/player/slide'), img_dur = 5),
            'player/wall_slide': Animation(load_images('entities/player/wall_slide'), img_dur = 5)
        }

        self.clouds = Clouds(self.assets['clouds'], count = 16)

        self.player = Player(self, (50, 50), (8, 15))

        self.tilemap = Tilemap(self, tile_size = 16)

        self.scroll = [0, 0]

    def run(self):
        # We are going to use one loop for physics, rendering, etc. 
        while True:
            # Reset frames
            self.display.blit(self.assets['background'], (0, 0))

            # Make camera follow player
            self.scroll[0] += (self.player.rect().centerx - self.display.get_width() / 2 - self.scroll[0]) / 30
            self.scroll[1] += (self.player.rect().centery - self.display.get_height() / 2 - self.scroll[1]) / 30
            render_scroll = (int(self.scroll[0]), int(self.scroll[1]))

            self.clouds.update()
            self.clouds.render(self.display, offset = render_scroll)

            self.tilemap.render(self.display, offset = render_scroll)

            # update location of player in the x direction
            self.player.update(self.tilemap, (self.movement[1] - self.movement[0], 0))
            self.player.render(self.display, offset = render_scroll)

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

            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))

            # This line refreshes the screen. Failing to include this line will leave the screen black
            pygame.display.update()

            # Setting loop to 60 fps
            self.clock.tick(60)


Game().run()

# TODO: Finish adding movement functionality. Adding events functionality
# I was thinking we use wasd for movement and x and c for events
# Collision detection and overall physics implementation