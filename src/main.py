import pygame

class GameState():
    def __init__(self, pygame):
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.isRunning = True


class PuyoSprites():
    _spritesheet_filename = "../img/chalkpuyo_sprites.png"
    _redPuyoRect = (192, 319, 64, 64)

    def __init__(self, pygame):
        try:
            self._spritesheet = pygame.image.load(self._spritesheet_filename).convert_alpha()
        except pygame.error as e:
            print(f"Unable to load spritesheet image: {self._spritesheet_filename}")
            raise SystemExit(e)
        self.redPuyo = self.image_at(self._redPuyoRect)
    
    def image_at(self, rectangle, colorkey=None):
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size, pygame.SRCALPHA)
        image.blit(self._spritesheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey == -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image


def gameLoop(pygame, gameState):
    background_image = pygame.image.load("../img/chalkboard_800x600.jpg")
    puyoSprites = PuyoSprites(pygame)

    while gameState.isRunning:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameState.isRunning = False

        # fill the screen with a color to wipe away anything from last frame
        gameState.screen.fill("purple")
        gameState.screen.blit(background_image, (0, 0))

        # RENDER YOUR GAME HERE
        gameState.screen.blit(puyoSprites.redPuyo, (0, 0))

        # flip() the display to put your work on screen
        pygame.display.flip()

        gameState.clock.tick(60)  # limits FPS to 60

def main():
    pygame.init()
    gameState = GameState(pygame)
    gameLoop(pygame, gameState)
    pygame.quit()


if __name__ == '__main__':
    main()
