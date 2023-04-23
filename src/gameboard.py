TILE_SIZE = 32
BOARD_TILE_WIDTH = 6
BOARD_TILE_HEIGHT = 12
BOARD_PIXEL_WIDTH = BOARD_TILE_WIDTH * TILE_SIZE
BOARD_PIXEL_HEIGHT = BOARD_TILE_HEIGHT * TILE_SIZE


class Gameboard:
    """
    Abstraction of the PuyoPuyo gameboard: a 6x12 grid where each cell is $tile_size
    pixels wide and tall.  The origin is the top left corner.  This class handles
    the conversion from grid coordinates (e.g. [2,4]) to pixel coordinates (e.g. [64, 128])
    """

    def __init__(self, origin):
        self.origin = origin

    def grid_to_pixel(self, coord):
        """
        Converts from grid coordinates (0,1 or 2,4) to pixel coordinates (0,32) or (64, 128)
        """
        x, y = coord
        origin_x, origin_y = self.origin
        return origin_x + (x * TILE_SIZE), origin_y + (y * TILE_SIZE)
