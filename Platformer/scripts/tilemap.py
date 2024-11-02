import pygame

# List of neighboring tiles... Order matters a lot here
NEIGHBOR_OFFSET = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (0, 0), (-1, 1), (0, 1), (1, 1)]
# Types of tiles we can collide with
PHYSICS_TILES = {'grass', 'stone'}

class Tilemap:
    def __init__(self, game: object, tile_size: int = 10) -> None:
        """ Class constructor args:
        game: Game class instance
        tile_size: Default tile size, should be overridden
        """
        self.game = game
        self.tile_size = tile_size
        self.tilemap = {}
        self.offgrid_tiles = []

        # Example tilemap for testing functionality to be replaced later
        for i in range(10):
            self.tilemap[str(3 + i) + ';10'] = {'type': 'grass', 'variant': 1, 'pos': (3 + i, 10)}
            self.tilemap['10;' + str(5 + i)] = {'type': 'stone', 'variant': 1, 'pos': (10, 5 + i)}

    def tiles_around(self, pos: tuple) -> list[dict]:
        """ Args:
        pos: position from which we will scan surrounding tiles

        Here we are checking if there are tiles in any of the 9 neighboring positions on the screen.
        """
        tiles = []
        tile_loc = (int(pos[0] // self.tile_size), int(pos[1] // self.tile_size))

        # Check neighboring locations
        for offset in NEIGHBOR_OFFSET:
            # Get location
            check_loc = str(tile_loc[0] + offset[0]) + ';' + str(tile_loc[1] + offset[1])
            # If location exists in tilemap, add to list of surrounding tiles
            if check_loc in self.tilemap:
                tiles.append(self.tilemap[check_loc])
        return tiles
    
    def physics_rects_around(self, pos: tuple) -> list[object]:
        """ Args:
        pos: position from which we will scan surrounding tiles

        Here we are checking if there are any tiles we can collide with in any of the neighboring tiles.
        """
        rects = []
        
        # Get the surrounding tiles, if their type is one of the physics tiles, we append to the list
        for tile in self.tiles_around(pos):
            if tile['type'] in PHYSICS_TILES:
                rects.append(pygame.Rect(tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size, self.tile_size, self.tile_size))
        return rects

    def render(self, surf: object) -> None:
        """ Args:
        surf: Surface to render the entity on

        we are loading offgrid tiles (tiles that we wont be colliding with) and physics tiles (tiles we can collide with)
        """ 
        for tile in self.offgrid_tiles:
            surf.blit(self.game.assets[tile['type']][tile['variant']], tile['pos'])
        
        for loc in self.tilemap:
            tile = self.tilemap[loc]
            surf.blit(self.game.assets[tile['type']][tile['variant']], (tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size))