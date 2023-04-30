import event
from random import choice


class GameState:
    def __init__(self, pygame):
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.next_puyo_pair = generate_random_puyo_pair()
        self.max_chain = 0
        self.num_moves = 0
        self.isRunning = True

    def reset(self, board):
        self.max_chain = 0
        self.num_moves = 0
        board.reset()

    def handle_event(self, evnt, board):
        if evnt == event.EVENT_QUIT:
            self.isRunning = False
        elif event.is_movement_event(evnt):
            if evnt == event.INPUT_UP:
                board.quick_drop()
                board.set_puyos()
                self.num_moves += 1
            else:
                puyos_placed = board.move_pair(evnt)
                if puyos_placed:
                    self.num_moves += 1
        elif evnt == event.ROTATE_CLOCKWISE:
            board.rotate_clockwise()
        elif evnt == event.ROTATE_COUNTER_CLOCKWISE:
            board.rotate_counter_clockwise()
        elif evnt == event.RESET_GAME:
            self.reset(board)


def generate_random_puyo_pair():
    yield choice('rgbyp') + choice('rgbyp')