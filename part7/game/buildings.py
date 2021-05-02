
import pygame as pg



class Lumbermill:

    def __init__(self, pos):
        image = pg.image.load("assets/graphics/building01.png")
        self.image = image
        self.name = "lumbermill"
        self.rect = self.image.get_rect(topleft=pos)
        self.counter = 0

    def update(self):
        self.counter += 1



class Stonemasonry:

    def __init__(self, pos):
        image = pg.image.load("assets/graphics/building02.png")
        self.image = image
        self.name = "stonemasonry"
        self.rect = self.image.get_rect(topleft=pos)
        self.counter = 0

    def update(self):
        self.counter += 1


