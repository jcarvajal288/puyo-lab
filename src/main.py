import pygame
from event import EventHandler
from gameState import GameState
from gameboard import Gameboard
from playfield import Playfield
import sprites
from sprites import Sprites


def render_current_pair(screen, board, puyo_sprites, puyo_frame):
    puyos = puyo_sprites.get_image_pair(board.current_pair_type)
    pair_grid_locations = [board.grid_to_pixel(x) for x in board.current_pair_locations]
    for puyo, grid in zip(puyos, pair_grid_locations):
        screen.blit(puyo[puyo_frame], grid)


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

        playfield.draw(game_state.screen)

        # RENDER YOUR GAME HERE
        puyo_frame = pygame.time.get_ticks() // sprites.ANIMATION_SPEED_IN_MS % 4
        board.draw(game_state.screen, puyo_sprites, puyo_frame)
        if not board.is_resolving():
            render_current_pair(game_state.screen, board, puyo_sprites, puyo_frame)

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
