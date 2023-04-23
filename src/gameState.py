import event
import gameboard
from random import choice


class GameState:
    def __init__(self, pygame):
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.isRunning = True
        self.falling_pair_type = 'ry'
        self.falling_pair_locations = gameboard.STARTING_POINTS

    def set_puyos(self, board):
        puyo_types = self.falling_pair_type
        coords = self.falling_pair_locations
        board.add_puyo(coords[0], puyo_types[0])
        board.add_puyo(coords[1], puyo_types[1])
        self.falling_pair_type = choice('rgbyp') + choice('rgbyp')
        self.falling_pair_locations = gameboard.STARTING_POINTS

    def move_pair(self, evnt, board):
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

        if evnt == event.INPUT_DOWN and not board.is_move_legal(x, y, a, b):
            self.set_puyos(board)

        if board.is_move_legal(x, y, a, b):
            self.falling_pair_locations = ((x, y), (a, b))

    def rotate_clockwise(self, board):
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
        if board.is_move_legal(x, y, a, b):
            self.falling_pair_locations = ((x, y), (a, b))

    def rotate_counter_clockwise(self, board):
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
        if board.is_move_legal(x, y, a, b):
            self.falling_pair_locations = ((x, y), (a, b))

    def handle_event(self, evnt, board):
        if evnt == event.EVENT_QUIT:
            self.isRunning = False
        elif event.is_movement_event(evnt):
            self.move_pair(evnt, board)
        elif evnt == event.ROTATE_CLOCKWISE:
            self.rotate_clockwise(board)
        elif evnt == event.ROTATE_COUNTER_CLOCKWISE:
            self.rotate_counter_clockwise(board)

