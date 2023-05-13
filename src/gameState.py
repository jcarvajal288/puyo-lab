from collections import deque
import event
from puyoPair import PuyoPair


class GameState:
    def __init__(self, pygame):
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.puyo_queue = deque([PuyoPair() for _ in range(3)])
        self.max_chain = 0
        self.num_moves = 0
        self.isRunning = True

    def reset(self, board):
        self.max_chain = 0
        self.num_moves = 0
        board.reset()
        self.puyo_queue = deque([PuyoPair() for _ in range(3)])

    def current_pair(self):
        return self.puyo_queue[0]

    def next_pair(self):
        self.puyo_queue.append(PuyoPair())
        self.puyo_queue.popleft()

    def handle_event(self, evnt, board):
        if evnt == event.EVENT_QUIT:
            self.isRunning = False
        elif event.is_movement_event(evnt):
            if evnt == event.INPUT_UP:
                self.current_pair().quick_drop(board)
                board.set_puyos(self.current_pair().colors, self.current_pair().locations)
                self.next_pair()
                self.num_moves += 1
            else:
                puyos_placed = self.current_pair().move(board, evnt)
                if puyos_placed:
                    self.num_moves += 1
        elif evnt == event.ROTATE_CLOCKWISE:
            self.current_pair().rotate_clockwise(board)
        elif evnt == event.ROTATE_COUNTER_CLOCKWISE:
            self.current_pair().rotate_counter_clockwise(board)
        elif evnt == event.RESET_GAME:
            self.reset(board)
