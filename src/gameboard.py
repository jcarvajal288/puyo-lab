import event
from random import choice

TILE_SIZE = 32
BOARD_TILE_WIDTH = 6
BOARD_TILE_HEIGHT = 13
BOARD_PIXEL_WIDTH = BOARD_TILE_WIDTH * TILE_SIZE
BOARD_PIXEL_HEIGHT = BOARD_TILE_HEIGHT * TILE_SIZE
STARTING_POINTS = ((2, 1), (2, 0))


class Gameboard:
    """
    Abstraction of the PuyoPuyo gameboard: a 6x12 grid (plus one ghost row) where each cell
    is $tile_size pixels wide and tall.  The origin is the top left corner.  This class handles
    the conversion from grid coordinates (e.g. [2,4]) to pixel coordinates (e.g. [64, 128])
    """

    def __init__(self, origin):
        self.origin = origin
        self.board = [[None for _ in range(0, BOARD_TILE_WIDTH)] for _ in range(0, BOARD_TILE_HEIGHT)]
        self.coord_list = [(x, y) for x in range(len(self.board[0]))
                                  for y in range(len(self.board))]
        self.falling_pair_type = 'ry'
        self.falling_pair_locations = STARTING_POINTS

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

    def is_move_legal(self, x, y, a, b):
        return min(x, a) >= 0 \
               and max(x, a) < BOARD_TILE_WIDTH \
               and min(y, b) >= 0 \
               and max(y, b) < BOARD_TILE_HEIGHT \
               and self.board[y][x] is None \
               and self.board[b][a] is None

    def set_puyos(self):
        puyo_types = self.falling_pair_type
        coords = self.falling_pair_locations
        self.add_puyo(coords[0], puyo_types[0])
        self.add_puyo(coords[1], puyo_types[1])
        self.falling_pair_type = choice('rgbyp') + choice('rgbyp')
        self.falling_pair_locations = STARTING_POINTS

    def move_pair(self, evnt):
        (x, y), (a, b) = self.falling_pair_locations

        if evnt == event.INPUT_UP:
            y -= 1
            b -= 1
        elif evnt == event.INPUT_DOWN:
            y += 1
            b += 1
        elif evnt == event.INPUT_LEFT:
            x -= 1
            a -= 1
        elif evnt == event.INPUT_RIGHT:
            x += 1
            a += 1

        if evnt == event.INPUT_DOWN and not self.is_move_legal(x, y, a, b):
            self.set_puyos()

        if self.is_move_legal(x, y, a, b):
            self.falling_pair_locations = ((x, y), (a, b))

    def rotate_clockwise(self):
        (x, y), (a, b) = self.falling_pair_locations
        if x == a:
            if b < y:
                a += 1
                b += 1
            else:
                a -= 1
                b -= 1
        elif y == b:
            if a < x:
                b -= 1
                a += 1
            else:
                b += 1
                a -= 1
        if self.is_move_legal(x, y, a, b):
            self.falling_pair_locations = ((x, y), (a, b))

    def rotate_counter_clockwise(self):
        (x, y), (a, b) = self.falling_pair_locations
        if x == a:
            if b < y:
                a -= 1
                b += 1
            else:
                a += 1
                b -= 1
        elif y == b:
            if a < x:
                a += 1
                b += 1
            else:
                a -= 1
                b -= 1
        if self.is_move_legal(x, y, a, b):
            self.falling_pair_locations = ((x, y), (a, b))
