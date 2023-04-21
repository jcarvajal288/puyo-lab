INPUT_UP = 0
INPUT_DOWN = 1
INPUT_LEFT = 2
INPUT_RIGHT = 3

class EventHandler():
    def __init__(self, pygame):
        REPEAT_DELAY_MS = 400
        REPEAT_INTERVAL_MS = 100
        self._pygame = pygame
        self._pygame.key.set_repeat(REPEAT_DELAY_MS, REPEAT_INTERVAL_MS)

    def is_movement_event(self, event):
        return event in {INPUT_UP, INPUT_DOWN, INPUT_LEFT, INPUT_RIGHT}

    def poll_for_input(self, gameState):
        for event in self._pygame.event.get():
            if event.type == self._pygame.QUIT: # pygame.QUIT event means the user clicked X to close your window
                gameState.isRunning = False
            elif event.type == self._pygame.KEYDOWN:
                if   event.key == self._pygame.K_UP:    return INPUT_UP
                elif event.key == self._pygame.K_DOWN:  return INPUT_DOWN
                elif event.key == self._pygame.K_LEFT:  return INPUT_LEFT
                elif event.key == self._pygame.K_RIGHT: return INPUT_RIGHT

    def handle_input(self, gameState):
        event = self.poll_for_input(gameState)
        if self.is_movement_event(event):
            gameState.movePair(event)
