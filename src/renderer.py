import sprites


class Renderer:
    def __init__(self, _pygame):
        self._pygame = _pygame

    def render(self, puyo_sprites, playfield, board, game_state):
        playfield.draw(game_state.screen, game_state)
        puyo_frame = self._pygame.time.get_ticks() // sprites.ANIMATION_SPEED_IN_MS % 4
        board.draw(game_state.screen, puyo_sprites, puyo_frame)

        # flip() the display to put your work on screen
        self._pygame.display.flip()
