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