import pygame

class PhysicsEtity: 
        
    # defining class constructor
    def __init__(self, game, entity_type, pos, size ):
            self.game = game 
            self.type = entity_type 
            self.pos = list(pos) 
            self.size = size
            self.velocity = [0,0]

    def update (self, movement =(0,0)):
        """
        defining how much the entity will move within the frame based on it current velocity
        and desired movement withing frame; using this value to update the position within
        the entity
        """
        frame_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])

        # updating x position based on the frame movement
        self.pos[0] += frame_movement [0]

        # updating y position based on the frame movement
        self.pos[1] += frame_movement[1]

    def render(self, surf):
         """

         """
         surf.blit(self.game.assets['player'], self.pos)