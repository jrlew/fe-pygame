import pygame as pg

from .tools.singleton import Singleton


@Singleton
class Store():
    def __init__(self):
        self.screen = None

        self.terrain = None
        self.units = None
        self.highlights = None

        self.current_highlights = None

        self.indicator = None

        self.players = None
        self.enemys = None
        self.all_units = pg.sprite.Group()

        self.paired_unit = None
