import os
import pygame

BASE_IMG_PATH = "data/images/"

def load_image(path: str) -> object:
    """ Args:
    path: Path of image to be loaded

    Loading a single image.
    """
    img = pygame.image.load(BASE_IMG_PATH + path).convert()
    img.set_colorkey((0, 0, 0))
    return img

def load_images(path: str) -> list[object]:
    """ Args:
    path: Path of folder containing sprites to be loaded

    Loading images for each sprite into an array.
    """
    images = []
    for img_name in sorted(os.listdir(BASE_IMG_PATH + path)):
        images.append(load_image(path + '/' + img_name))
    return images

class Animation:
    def __init__(self, images, img_dur=5, loop=True) -> None:
        self.images = images
        self.img_duration = img_dur
        self.loop = loop
        self.done = False
        self.frame = 0

    def copy(self):
        return Animation(self.images, self.img_duration, self.loop)
    
    def update(self):
        if self.loop:
            self.frame = (self.frame + 1) % (self.img_duration * len(self.images))
        else:
            self.frame = min(self.frame + 1, self.img_duration * len(self.images))
    
    def img(self):
        return self.images[int(self.frame / self.img_duration)]
        