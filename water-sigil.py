"""
Placeholder
"""

import pygame

from data.enemy import Enemy
from data.player import Player
from data.indicator import Indicator
from data.state import State
from data.screen import Screen
from data.levels.intro import Intro
from data.event_handler import EventHandler

# Temp until Indicator separated from Unit
playerStats = {
    "name": "Indicator",
    "hp": 20,
    "strength": 8,
    "defense": 4,
    "accuracy": 120,
    "evasion": 25,
}

pygame.init()
state = State(Screen(), Intro(), Indicator((0, 0), playerStats))
event_handler = EventHandler()
clock = pygame.time.Clock()
FPS = 30

state.screen.init_screen(state.level.terrain)
state.screen.init_info_pane(state)
state.screen.init_context_menu()
state.screen.display_terrain_info(state)

state.screen.render_unit(state.indicator)

for _player in state.level.players:
    state.screen.render_unit(_player)

for _enemy in state.level.enemys:
    state.screen.render_unit(_enemy)

pygame.display.update()

while 1:
    clock.tick(FPS)

    if state.flags.player_won:
        state.level.end_game('You Win')

    state.flags.update = False

    if state.flags.player_turn:
        state.screen.display_context_message("Player Turn")
        pygame.display.update()
        
        for event in pygame.event.get():
            event_handler.handle(event, state)

        if state.flags.update:
            state.level.check_for_win(state)
            state.screen.clear_info_pane(state)
            state.screen.move_indicator(state)
            state.level.update_unit_info(state)
            state.screen.display_terrain_info(state)
            pygame.display.update()

            # TODO: this should check on movement not on every cyle...
            state.level.check_for_turn_end(state, state.level.players)


    else:
        state.screen.display_context_message("Enemy Turn")
        state.level.enemy_turn(state)
        pygame.display.update()
        state.level.check_for_turn_end(state, state.level.enemys)
