import gameboard


class Playfield:
    _background_image_filename = "../img/chalkboard_800x600.jpg"
    _chalk_font_filename = "../font/VTCAllSkratchedUpOne.ttf"
    _board_border_font_size = gameboard.TILE_SIZE // 2
    _stats_font_size = gameboard.TILE_SIZE
    _max_chain_origin = (500, 100)
    _num_moves_origin = (500, 200)
    _preview_origin = (300, 200)
    white = (240, 240, 240)

    def __init__(self, pygame, board):
        self.background_image = pygame.image.load(self._background_image_filename)
        self.gameboard_origin = board.origin[0], board.origin[1] + gameboard.TILE_SIZE
        self.board_border_font = pygame.font.Font(self._chalk_font_filename, self._board_border_font_size)
        self.stats_font = pygame.font.Font(self._chalk_font_filename, self._stats_font_size)

        self.horizontal_bar = self.board_border_font.render('---------------------', True, self.white)
        self.vertical_brackets = self.board_border_font.render('|                                       |', True, self.white)

    def draw(self, screen, game_state, puyo_sprites, animation_frame):
        self._draw_board_border(screen)
        self._draw_preview(screen, game_state, puyo_sprites, animation_frame)
        self._draw_stats(screen, game_state)

    def _draw_board_border(self, screen):
        top_left = (self.gameboard_origin[0] - self._board_border_font_size // 2,
                    self.gameboard_origin[1] - self._board_border_font_size)
        bottom_right = (self.gameboard_origin[0] + gameboard.BOARD_PIXEL_WIDTH,
                        self.gameboard_origin[1] + gameboard.BOARD_PIXEL_HEIGHT
                        - gameboard.TILE_SIZE
                        - self._board_border_font_size / 2)
        screen.fill("black")
        screen.blit(self.background_image, (0, 0))
        screen.blit(self.horizontal_bar, top_left)
        screen.blit(self.horizontal_bar, (top_left[0], bottom_right[1]))
        vertical_bar_offset = 6
        for i in range(1, 31):
            bracket_top_left = (top_left[0], top_left[1] + gameboard.BOARD_TILE_HEIGHT * i - vertical_bar_offset)
            screen.blit(self.vertical_brackets, bracket_top_left)

    def _draw_preview(self, screen, game_state, puyo_sprites, animation_frame):
        top = self._preview_origin
        bottom = self._preview_origin[0], self._preview_origin[1] + gameboard.TILE_SIZE
        for puyo_color, coord in zip(game_state.puyo_queue[1].colors, (top, bottom)):
            puyo = puyo_sprites.char_to_puyo(puyo_color)
            screen.blit(puyo[animation_frame], coord)

    def _draw_stats(self, screen, game_state):
        max_chain = self.stats_font.render(f'Max Chain: {game_state.max_chain}', True, self.white)
        num_moves = self.stats_font.render(f'Number of Moves: {game_state.num_moves}', True, self.white)
        screen.blit(max_chain, self._max_chain_origin)
        screen.blit(num_moves, self._num_moves_origin)
