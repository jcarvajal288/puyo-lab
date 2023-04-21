import pygame
import event
from event import EventHandler
from gameboard import Gameboard
from sprites import Sprites

class GameState():
    def __init__(self, pygame):
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.isRunning = True
        self.falling_pair_location = (2, 0)

    def movePair(self, evnt):
        x, y = self.falling_pair_location
        if   evnt == event.INPUT_UP:    y -= 1
        elif evnt == event.INPUT_DOWN:  y += 1
        elif evnt == event.INPUT_LEFT:  x -= 1
        elif evnt == event.INPUT_RIGHT: x += 1
        self.falling_pair_location = (x, y)


def gameLoop(pygame, gameState, eventHandler):
    background_image = pygame.image.load("../img/chalkboard_800x600.jpg")
    puyoSprites = Sprites(pygame)
    gameboard = Gameboard((0,0), 32)

    while gameState.isRunning:
        eventHandler.handle_input(gameState)

        # fill the screen with a color to wipe away anything from last frame
        gameState.screen.fill("black")
        gameState.screen.blit(background_image, (0, 0))

        # RENDER YOUR GAME HERE
        gameState.screen.blit(puyoSprites.redPuyo, gameboard.grid(gameState.falling_pair_location))

        # flip() the display to put your work on screen
        pygame.display.flip()

        gameState.clock.tick(60)  # limits FPS to 60

def main():
    pygame.init()
    gameState = GameState(pygame)
    eventHandler = EventHandler(pygame)
    gameLoop(pygame, gameState, eventHandler)
    pygame.quit()


if __name__ == '__main__':
    main()
