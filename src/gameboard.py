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
        self.falling_puyos = []  # pairs of (puyo type, pixel coordinates)
        self.falling_speed = 8
        self.resolving_groups = set()
        self.num_chains = 0

    def is_resolving(self):
        return len(self.falling_puyos) > 0 \
               or len(self.resolving_groups) > 0

    def _is_puyo_supported(self, x, y):
        if y + 1 >= BOARD_TILE_HEIGHT:
            return True
        else:
            return self.board[y + 1][x] is not None

    def reset(self):
        self.__init__(self.origin)

    def draw(self, screen, sprites, frame):
        self._draw_settled_puyos(frame, screen, sprites)
        self._draw_falling_puyos(frame, screen, sprites)

    def _draw_settled_puyos(self, frame, screen, sprites):
        filled_spaces = [(x, y) for (x, y) in self.coord_list if self.board[y][x] is not None]
        for (x, y) in filled_spaces:
            puyo = sprites.char_to_puyo(self.board[y][x])
            pixel_coord = self.grid_to_pixel((x, y))
            screen.blit(puyo[frame], pixel_coord)

    def _draw_falling_puyos(self, frame, screen, sprites):
        for falling_puyo in self.falling_puyos:
            (puyo_color, pixel_coord) = falling_puyo
            puyo = sprites.char_to_puyo(puyo_color)
            screen.blit(puyo[frame], pixel_coord)
            x, y = self.pixel_to_grid(pixel_coord)
            if self._is_puyo_supported(x, y):
                self.board[y][x] = puyo_color
                self.falling_puyos.remove(falling_puyo)

    def grid_to_pixel(self, grid):
        """
        Converts from grid coordinates (0,1 or 2,4) to pixel coordinates (0,32) or (64, 128)
        """
        x, y = grid
        origin_x, origin_y = self.origin
        return origin_x + (x * TILE_SIZE), origin_y + (y * TILE_SIZE)

    def pixel_to_grid(self, pixel):
        x, y = pixel
        origin_x, origin_y = self.origin
        return (x - origin_x) // TILE_SIZE, (y - origin_y) // TILE_SIZE

    def get_grid(self, x, y):
        return self.board[y][x]

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

    def set_puyos(self, puyo_colors, coords):
        self.add_puyo(coords[0], puyo_colors[0])
        self.add_puyo(coords[1], puyo_colors[1])
        self.resolve()

    def remove_puyo(self, coord):
        self.board[coord[1]][coord[0]] = None

    def _detach_hanging_puyos(self):
        puyos_in_board = [(x, y) for (x, y) in self.coord_list if self.board[y][x] is not None]
        for x, y in reversed(puyos_in_board):
            if not self._is_puyo_supported(x, y):
                self.falling_puyos.append((self.board[y][x], self.grid_to_pixel((x, y))))
                self.remove_puyo((x, y))

    def _update_falling_puyo_locations(self):
        self.falling_puyos = [(p, (x, y + self.falling_speed)) for (p, (x, y)) in self.falling_puyos]

    def _get_group_for_coord(self, coord, puyo_type, group):
        group.add(coord)
        x, y = coord
        neighbors = ((x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1))
        new_group_members = [(x, y) for (x, y) in neighbors
                             if 0 <= x < BOARD_TILE_WIDTH
                             and 0 <= y < BOARD_TILE_HEIGHT
                             and self.board[y][x] == puyo_type
                             and (x, y) not in group]
        for neighbor in new_group_members:
            self._get_group_for_coord(neighbor, puyo_type, group)
        return group

    def _find_groups(self):
        for coord in self.coord_list:
            puyo_type = self.get_grid(coord[0], coord[1])
            if puyo_type is not None \
                    and coord not in self.resolving_groups:
                group = self._get_group_for_coord(coord, puyo_type, set())
                if len(group) >= 4:
                    self.resolving_groups.update(group)

    def _resolve_groups(self):
        self._find_groups()
        if len(self.resolving_groups) > 0:
            self.num_chains += 1
            for (x, y) in self.resolving_groups:
                self.remove_puyo((x, y))
            self.resolving_groups.clear()
            self.current_pair_locations = STARTING_POINTS

    def resolve(self):
        if len(self.falling_puyos) == 0:
            self._resolve_groups()
        self._detach_hanging_puyos()
        self._update_falling_puyo_locations()


