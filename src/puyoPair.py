import event
import gameboard


class PuyoPair:
    def __init__(self):
        self.colors = gameboard.random_puyo_pair()
        self.locations = gameboard.STARTING_POINTS

    def draw(self, screen, board, puyo_sprites, animation_frame):
        puyos = puyo_sprites.get_image_pair(self.colors)
        pair_grid_locations = [board.grid_to_pixel(x) for x in self.locations]
        for puyo, grid in zip(puyos, pair_grid_locations):
            screen.blit(puyo[animation_frame], grid)

    def move(self, board, evnt):
        (x, y), (a, b) = self.locations

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

        if evnt == event.INPUT_DOWN and not is_move_legal(board, x, y, a, b):
            board.set_puyos()
            return True

        if is_move_legal(board, x, y, a, b):
            self.locations = ((x, y), (a, b))
        return False

    def quick_drop(self, board):
        (x, y), (a, b) = self.locations
        lowest_point = max(y, b)
        distance_to_drop = -1
        for i in range(lowest_point, gameboard.BOARD_TILE_HEIGHT):
            if board.get_puyo((x, i)) is None and board.get_puyo((a, i)) is None:
                distance_to_drop += 1
            else:
                break
        self.locations = ((x, y + distance_to_drop), (a, b + distance_to_drop))

    def rotate_clockwise(self, board):
        (x, y), (a, b) = self.locations
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
        if is_move_legal(board, x, y, a, b):
            self.locations = ((x, y), (a, b))

    def rotate_counter_clockwise(self, board):
        (x, y), (a, b) = self.locations
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
        if is_move_legal(board, x, y, a, b):
            self.locations = ((x, y), (a, b))


def is_move_legal(board, x, y, a, b):
    return min(x, a) >= 0 \
           and max(x, a) < gameboard.BOARD_TILE_WIDTH \
           and min(y, b) >= 0 \
           and max(y, b) < gameboard.BOARD_TILE_HEIGHT \
           and board[y][x] is None \
           and board[b][a] is None
