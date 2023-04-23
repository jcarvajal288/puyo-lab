import event
import gameboard


class GameState:
    def __init__(self, pygame):
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.isRunning = True
        self.falling_pair_type = 'ry'
        self.falling_pair_location = ((2, 0), (2, -1))

    def move_pair(self, evnt):
        (x, y), (a, b) = self.falling_pair_location

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

        if is_move_legal(x, y, a, b):
            self.falling_pair_location = ((x, y), (a, b))

    def rotate_clockwise(self):
        (x, y), (a, b) = self.falling_pair_location
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
        if is_move_legal(x, y, a, b):
            self.falling_pair_location = ((x, y), (a, b))

    def rotate_counter_clockwise(self):
        (x, y), (a, b) = self.falling_pair_location
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
        if is_move_legal(x, y, a, b):
            self.falling_pair_location = ((x, y), (a, b))

    def handle_event(self, evnt):
        if evnt == event.EVENT_QUIT:
            self.isRunning = False
        elif event.is_movement_event(evnt):
            self.move_pair(evnt)
        elif evnt == event.ROTATE_CLOCKWISE:
            self.rotate_clockwise()
        elif evnt == event.ROTATE_COUNTER_CLOCKWISE:
            self.rotate_counter_clockwise()


def is_move_legal(x, y, a, b):
    return min(x, a) >= 0 \
           and max(x, a) < gameboard.BOARD_TILE_WIDTH \
           and min(y, b) >= 0 \
           and max(y, b) < gameboard.BOARD_TILE_HEIGHT