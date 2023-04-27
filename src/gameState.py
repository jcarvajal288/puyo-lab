import event


class GameState:
    def __init__(self, pygame):
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.max_chain = 0
        self.isRunning = True

    def handle_event(self, evnt, board):
        if evnt == event.EVENT_QUIT:
            self.isRunning = False
        elif event.is_movement_event(evnt):
            if evnt == event.INPUT_UP:
                board.quick_drop()
                board.set_puyos()
            else:
                board.move_pair(evnt)
        elif evnt == event.ROTATE_CLOCKWISE:
            board.rotate_clockwise()
        elif evnt == event.ROTATE_COUNTER_CLOCKWISE:
            board.rotate_counter_clockwise()
        elif evnt == event.RESET_GAME:
            board.reset()
