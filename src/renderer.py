import sprites


class Renderer:
    def __init__(self, _pygame):
        self._pygame = _pygame

    def render(self, puyo_sprites, playfield, board, game_state):
        playfield.draw(game_state.screen, game_state)
        animation_frame = self._pygame.time.get_ticks() // sprites.ANIMATION_SPEED_IN_MS % 4
        board.draw(game_state.screen, puyo_sprites, animation_frame)
        if not board.is_resolving():
            game_state.current_pair().draw(game_state.screen, board, puyo_sprites, animation_frame)

        self._pygame.display.flip()
