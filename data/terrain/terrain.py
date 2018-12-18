"""
Placeholder
"""


import os
import pygame


class Terrain():
    def __init__(self, type_name, path_to_image, def_adjustment, evasion_adjustment):
        self.type = type_name
        self.image = pygame.image.load(os.path.join(os.path.dirname(__file__), path_to_image)).convert()
        self.def_adjustment = def_adjustment
        self.evasion_adjustment = evasion_adjustment
        self.movement_cost = 1 # Hardcoded for inital use/testing
