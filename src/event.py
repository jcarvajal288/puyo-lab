EVENT_QUIT = 0
INPUT_UP = 1
INPUT_DOWN = 2
INPUT_LEFT = 3
INPUT_RIGHT = 4
ROTATE_CLOCKWISE = 5
ROTATE_COUNTER_CLOCKWISE = 6


class EventHandler:
    def __init__(self, pygame):
        REPEAT_DELAY_MS = 400
        REPEAT_INTERVAL_MS = 100
        self._pygame = pygame
        self._pygame.key.set_repeat(REPEAT_DELAY_MS, REPEAT_INTERVAL_MS)

    def get_input(self):
        for event in self._pygame.event.get():
            if event.type == self._pygame.QUIT:  # pygame.QUIT event means the user clicked X to close your window
                return EVENT_QUIT
            elif event.type == self._pygame.KEYDOWN:
                if event.key == self._pygame.K_UP:
                    return INPUT_UP
                elif event.key == self._pygame.K_DOWN:
                    return INPUT_DOWN
                elif event.key == self._pygame.K_LEFT:
                    return INPUT_LEFT
                elif event.key == self._pygame.K_RIGHT:
                    return INPUT_RIGHT
                elif event.key == self._pygame.K_z:
                    return ROTATE_CLOCKWISE
                elif event.key == self._pygame.K_x:
                    return ROTATE_COUNTER_CLOCKWISE


def is_movement_event(event):
    return event in {INPUT_UP, INPUT_DOWN, INPUT_LEFT, INPUT_RIGHT}
