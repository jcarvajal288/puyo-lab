INPUT_UP = 0
INPUT_DOWN = 1
INPUT_LEFT = 2
INPUT_RIGHT = 3

def is_movement_event(event):
    return event in {INPUT_UP, INPUT_DOWN, INPUT_LEFT, INPUT_RIGHT}

def poll_for_input(pygame, gameState):
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

def handle_input(pygame, gameState):
    event = poll_for_input(pygame, gameState)
    if is_movement_event(event):
        gameState.movePair(event)
