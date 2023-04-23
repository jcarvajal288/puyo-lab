import pygame
from event import EventHandler
from gameState import GameState
from gameboard import Gameboard
from playfield import Playfield
import sprites
from sprites import Sprites


def game_loop(pygame, game_state, event_handler):
    puyo_sprites = Sprites(pygame)
    board = Gameboard((100, 68))
    playfield = Playfield(pygame, board)

    while game_state.isRunning:
        board.resolve()
        if board.is_resolving():
            pygame.event.clear()
        else:
            game_state.handle_event(event_handler.get_input(), board)

        # RENDER YOUR GAME HERE
        playfield.draw(game_state.screen)
        puyo_frame = pygame.time.get_ticks() // sprites.ANIMATION_SPEED_IN_MS % 4
        board.draw(game_state.screen, puyo_sprites, puyo_frame)

        # flip() the display to put your work on screen
        pygame.display.flip()

        game_state.clock.tick(60)  # limits FPS to 60


def main():
    pygame.init()
    game_state = GameState(pygame)
    event_handler = EventHandler(pygame)
    game_loop(pygame, game_state, event_handler)
    pygame.quit()


if __name__ == '__main__':
    main()
