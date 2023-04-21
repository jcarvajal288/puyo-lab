class Gameboard():
    """
    Abstraction of the PuyoPuyo gameboard: a 6x12 grid where each cell is $tile_size
    pixels wide and tall.  The origin is the top left corner.  This class handles
    the conversion from grid coordinates (e.g. [2,4]) to pixel coordinates (e.g. [64, 128])
    """
    def __init__(self, origin, tile_size):
        self.origin_x, self.origin_y = origin
        self.tile_size = tile_size
        self.width = 6
        self.height = 12

    def grid(self, coord):
        """
        Converts from grid coordinates (0,1 or 2,4) to pixel coordinates (0,32) or (64, 128)
        """
        x, y = coord
        return (self.origin_x + (x * self.tile_size), self.origin_y + (y * self.tile_size))
