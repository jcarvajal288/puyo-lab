import pygame
from event import EventHandler
from gameState import GameState
from gameboard import Gameboard
from playfield import Playfield
from renderer import Renderer
from sprites import Sprites


def game_loop(game_state, event_handler):
    puyo_sprites = Sprites(pygame)
    board = Gameboard((100, 68))
    playfield = Playfield(pygame, board)
    renderer = Renderer(pygame)

    while game_state.isRunning:
        board.resolve()
        if board.is_resolving():
            pygame.event.clear()
        else:
            board.num_chains = 0
            game_state.handle_event(event_handler.get_input(), board)
        game_state.max_chain = max(game_state.max_chain, board.num_chains)

        # RENDER YOUR GAME HERE
        renderer.render(puyo_sprites, playfield, board, game_state)

        game_state.clock.tick(60)  # limits FPS to 60


def main():
    pygame.init()
    game_state = GameState(pygame)
    event_handler = EventHandler(pygame)
    game_loop(game_state, event_handler)
    pygame.quit()


if __name__ == '__main__':
    main()
