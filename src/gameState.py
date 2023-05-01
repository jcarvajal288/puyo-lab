import event
from puyoPair import PuyoPair


class GameState:
    def __init__(self, pygame):
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.puyo_pair = PuyoPair()
        self.max_chain = 0
        self.num_moves = 0
        self.isRunning = True

    def reset(self, board):
        self.max_chain = 0
        self.num_moves = 0
        board.reset()
        self.puyo_pair = PuyoPair()

    def handle_event(self, evnt, board):
        if evnt == event.EVENT_QUIT:
            self.isRunning = False
        elif event.is_movement_event(evnt):
            if evnt == event.INPUT_UP:
                self.puyo_pair.quick_drop(board)
                board.set_puyos(self.puyo_pair.colors, self.puyo_pair.locations)
                self.puyo_pair = PuyoPair()
                self.num_moves += 1
            else:
                puyos_placed = self.puyo_pair.move(board, evnt)
                if puyos_placed:
                    self.num_moves += 1
        elif evnt == event.ROTATE_CLOCKWISE:
            self.puyo_pair.rotate_clockwise(board)
        elif evnt == event.ROTATE_COUNTER_CLOCKWISE:
            self.puyo_pair.rotate_counter_clockwise(board)
        elif evnt == event.RESET_GAME:
            self.reset(board)

