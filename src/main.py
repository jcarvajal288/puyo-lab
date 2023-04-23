import pygame
from event import EventHandler
from gameState import GameState
from gameboard import Gameboard
from playfield import Playfield
import sprites
from sprites import Sprites


def render_falling_pair(game_state, gameboard, puyo_sprites, puyo_frame):
    puyos = puyo_sprites.get_image_pair(game_state.falling_pair_type)
    pair_grid_locations = [gameboard.grid_to_pixel(x) for x in game_state.falling_pair_location]
    for puyo, grid in zip(puyos, pair_grid_locations):
        game_state.screen.blit(puyo[puyo_frame], grid)


def game_loop(pygame, gameState, eventHandler):
    puyo_sprites = Sprites(pygame)
    gameboard = Gameboard((100, 100))
    playfield = Playfield(pygame, gameboard)

    while gameState.isRunning:
        gameState.handle_event(eventHandler.get_input())

        playfield.draw(gameState.screen)

        # RENDER YOUR GAME HERE
        puyo_frame = pygame.time.get_ticks() // sprites.ANIMATION_SPEED_IN_MS % 4
        gameboard.draw(gameState.screen, puyo_sprites, puyo_frame)
        render_falling_pair(gameState, gameboard, puyo_sprites, puyo_frame)

        # flip() the display to put your work on screen
        pygame.display.flip()

        gameState.clock.tick(60)  # limits FPS to 60


def main():
    pygame.init()
    game_state = GameState(pygame)
    event_handler = EventHandler(pygame)
    game_loop(pygame, game_state, event_handler)
    pygame.quit()


if __name__ == '__main__':
    main()
