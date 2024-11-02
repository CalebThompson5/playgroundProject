import pygame

class PhysicsEtity:
    def __init__(self, game: object, entity_type: str, pos: tuple, size: tuple) -> None:
        """ Class constructor args:
        game: Game class instance
        entity_type: Type of entity being spawned
        pos: Position of character being spawned (x, y)
        size: Size of character being spawned (width, height)

        Initial velocity being set to 0, collisions dictionary being initialized to all False.
        """
        self.game = game 
        self.type = entity_type 
        self.pos = list(pos) 
        self.size = size
        self.velocity = [0,0]
        self.collisions = {'up': False, 'down': False, 'left': False, 'right': False}

    def rect(self) -> pygame.Rect:
        """
        Returns the hitbox rectangle of the entity.
        """
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def update (self, tilemap: object, movement: tuple = (0,0)) -> None:
        """ Args:
        tilemap: Tilemap object representing the current map layout
        movement: Current frame movement of the entity (x, y)

        This method will be infinitely updating the location, velocity, and acceleration of the
        entity.
        """
        # At the beginning of every frame, set collisions to false
        self.collisions = {'up': False, 'down': False, 'left': False, 'right': False}

        # Here we are updating how much the entity will move in the current frame based on
        # their current desired movement and their sustained velocity
        frame_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])

        # Updating x position based on the frame movement
        self.pos[0] += frame_movement[0]

        # Pulling the hitbox rectangle for the entity
        entity_rect = self.rect()

        # Loop through the entities surroundings, if the entity
        # collides with a surrounding rectangle we handle the collision
        # and set the collision value in the dictionary to true, finally
        # we update the entity position
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[0] > 0:
                       entity_rect.right = rect.left
                       self.collisions['right'] = True
                if frame_movement[0] < 0:
                       entity_rect.left = rect.right
                       self.collisions['left'] = True
                self.pos[0] = entity_rect.x
                
        # Updating y position based on the frame movement
        self.pos[1] += frame_movement[1]

        # Pulling the hitbox rectangle for the entity
        entity_rect = self.rect()

        # Loop through the entities surroundings, if the entity
        # collides with a surrounding rectangle we handle the collision
        # and set the collision value in the dictionary to true, finally
        # we update the entity position
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[1] > 0:
                       entity_rect.bottom = rect.top
                       self.collisions['down'] = True
                if frame_movement[1] < 0:
                       entity_rect.top = rect.bottom
                       self.collisions['up'] = True
                self.pos[1] = entity_rect.y

        # Set a terminal velocity for the y velocity, and acceleration
        # of .1 
        self.velocity[1] = min(5, self.velocity[1] + 0.1)

        # Make sure we stop moving on an upward or downward collision
        if self.collisions['down'] or self.collisions['up']:
             self.velocity[1] = 0

    def render(self, surf: object) -> None:
        """ Args:
        surf: Surface to render the entity on
        """
        # :oading the player image and the position
        surf.blit(self.game.assets['player'], self.pos)