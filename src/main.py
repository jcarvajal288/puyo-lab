import pygame

# pygame setup
pygame.init()

background_image = pygame.image.load("../img/chalkboard_800x600.jpg")

class GameState():
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.isRunning = True

def gameLoop(gameState):
    while gameState.isRunning:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameState.isRunning = False

        # fill the screen with a color to wipe away anything from last frame
        gameState.screen.fill("black")
        gameState.screen.blit(background_image, (0, 0))

        # RENDER YOUR GAME HERE

        # flip() the display to put your work on screen
        pygame.display.flip()

        gameState.clock.tick(60)  # limits FPS to 60


def main():
    gameState = GameState()
    gameLoop(gameState)
    pygame.quit()


if __name__ == '__main__':
    main()
