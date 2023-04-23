import gameboard


class Playfield:
    _background_image_filename = "../img/chalkboard_800x600.jpg"
    _chalk_font_filename = "../font/EraserRegular.ttf"
    _chalk_font_size = 16
    white = (255, 255, 255)

    def __init__(self, pygame, board):
        self.background_image = pygame.image.load(self._background_image_filename)
        self.gameboard_origin = board.origin
        self.chalk_font = pygame.font.Font(self._chalk_font_filename, 16)

        self.horizontal_bar = self.chalk_font.render('-----------------------', True, self.white)
        self.vertical_brackets = self.chalk_font.render('I                                 I', True, self.white)

    def draw(self, screen):
        top_left = (self.gameboard_origin[0] - self._chalk_font_size / 2,
                    self.gameboard_origin[1] - self._chalk_font_size)
        bottom_right = (self.gameboard_origin[0] + gameboard.BOARD_PIXEL_WIDTH,
                        self.gameboard_origin[1] + gameboard.BOARD_PIXEL_HEIGHT - self._chalk_font_size / 2)
        screen.fill("black")
        screen.blit(self.background_image, (0, 0))
        screen.blit(self.horizontal_bar, top_left)
        screen.blit(self.horizontal_bar, (top_left[0], bottom_right[1]))
        for i in range(1, 33):
            bracket_top_left = (top_left[0], top_left[1] + gameboard.BOARD_TILE_HEIGHT * i)
            screen.blit(self.vertical_brackets, bracket_top_left)
