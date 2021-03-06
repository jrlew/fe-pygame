import sys
import pygame as pg
from .store import Store

from .customevents import CustomEvents

class Game(object):
    """
    A single instance of this class is responsible for 
    managing which individual game state is active
    and keeping it updated. It also handles many of
    pygame's nuts and bolts (managing the event 
    queue, framerate, updating the display, etc.). 
    and its run method serves as the "game loop".
    """

    def __init__(self, screen, states, start_state):
        """
        Initialize the Game object.

        screen: the pygame display surface
        states: a dict mapping state-names to GameState objects
        start_state: name of the first active game state 
        """
        print('Is Game used?')
        self.done = False
        self.clock = pg.time.Clock()
        self.fps = 60
        self.states = states
        self.state_name = start_state
        self.state = self.states[self.state_name]()
        self.custom_events = CustomEvents()
        self.store = Store.instance()
        self.store.screen = screen

        self.state = self.states[self.state_name]()
        self.state.startup()

    def event_loop(self):
        """Events are passed for handling to the current state."""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit = True
                sys.exit()
            elif event.type == self.custom_events.UPDATE_ANIMATION:
                self.store.all_units.update()
            else:
                self.state.get_event(event)

    def flip_state(self):
        """Switch to the next game state."""
        current_state = self.state_name
        next_state = self.state.next_state
        self.state.done = False
        self.state_name = next_state
        self.state = self.states[self.state_name]()
        self.state.startup()

    def update(self, dt):
        """
        Check for state flip and update active state.
        dt: milliseconds since last frame
        """
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.flip_state()
        self.state.update(dt)

    def draw(self):
        """Pass display surface to active state for drawing."""
        self.state.draw()

    def run(self):
        """
        Pretty much the entirety of the game's runtime will be
        spent inside this while loop.
        """
        pg.time.set_timer(self.custom_events.UPDATE_ANIMATION, 650)

        while not self.done:
            dt = self.clock.tick(self.fps)
            self.event_loop()
            self.update(dt)
            self.draw()
            pg.display.update()
