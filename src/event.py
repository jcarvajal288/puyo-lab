INPUT_UP = 0
INPUT_DOWN = 1
INPUT_LEFT = 2
INPUT_RIGHT = 3

class EventHandler():
    def __init__(self):
        self.is_held = False
        self.is_repeating = False

    def is_movement_event(self, event):
        return event in {INPUT_UP, INPUT_DOWN, INPUT_LEFT, INPUT_RIGHT}

    def poll_for_input(self, pygame, gameState):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # pygame.QUIT event means the user clicked X to close your window
                gameState.isRunning = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            return INPUT_UP
        if keys[pygame.K_DOWN]:
            return INPUT_DOWN
        if keys[pygame.K_LEFT]:
            return INPUT_LEFT
        if keys[pygame.K_RIGHT]:
            return INPUT_RIGHT

    def handle_input(self, pygame, gameState):
        event = self.poll_for_input(pygame, gameState)
        if self.is_movement_event(event):
            gameState.movePair(event)
