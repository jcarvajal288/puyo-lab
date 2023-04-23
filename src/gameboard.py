TILE_SIZE = 32
BOARD_TILE_WIDTH = 6
BOARD_TILE_HEIGHT = 12
BOARD_PIXEL_WIDTH = BOARD_TILE_WIDTH * TILE_SIZE
BOARD_PIXEL_HEIGHT = BOARD_TILE_HEIGHT * TILE_SIZE
STARTING_POINTS = ((2, 0), (2, -1))


class Gameboard:
    """
    Abstraction of the PuyoPuyo gameboard: a 6x12 grid where each cell is $tile_size
    pixels wide and tall.  The origin is the top left corner.  This class handles
    the conversion from grid coordinates (e.g. [2,4]) to pixel coordinates (e.g. [64, 128])
    """

    def __init__(self, origin):
        self.origin = origin
        self.board = [[None for _ in range(0, BOARD_TILE_WIDTH)] for _ in range(0, BOARD_TILE_HEIGHT)]
        self.coord_list = [(x, y) for x in range(len(self.board[0]))
                                  for y in range(len(self.board))]

    def draw(self, screen, sprites, frame):
        filled_spaces = [(x, y) for (x, y) in self.coord_list if self.board[y][x] is not None]
        for (x, y) in filled_spaces:
            puyo_type = sprites.char_to_puyo(self.board[y][x])
            pixel_coord = self.grid_to_pixel((x, y))
            screen.blit(puyo_type[frame], pixel_coord)

    def grid_to_pixel(self, coord):
        """
        Converts from grid coordinates (0,1 or 2,4) to pixel coordinates (0,32) or (64, 128)
        """
        x, y = coord
        origin_x, origin_y = self.origin
        return origin_x + (x * TILE_SIZE), origin_y + (y * TILE_SIZE)

    def add_puyo(self, coord, puyo_type):
        x, y = coord
        self.board[y][x] = puyo_type
