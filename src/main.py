import pygame
import event
from event import EventHandler
import gameboard
from gameboard import Gameboard
from playfield import Playfield
from sprites import Sprites

class GameState():
    def __init__(self, pygame):
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.isRunning = True
        self.falling_pair_location = (0, 0)

    def movePair(self, evnt):
        x, y = self.falling_pair_location

        if   evnt == event.INPUT_UP:    y -= 1
        elif evnt == event.INPUT_DOWN:  y += 1
        elif evnt == event.INPUT_LEFT:  x -= 1
        elif evnt == event.INPUT_RIGHT: x += 1

        if x < 0: 
            x = 0
        elif x >= gameboard.BOARD_TILE_WIDTH: 
            x = gameboard.BOARD_TILE_WIDTH - 1
        if y < 0: 
            y = 0
        elif y >= gameboard.BOARD_TILE_HEIGHT: 
            y = gameboard.BOARD_TILE_HEIGHT - 1

        self.falling_pair_location = (x, y)

    def handle_event(self, evnt):
        if evnt == event.EVENT_QUIT:
            self.isRunning = False
        elif event.is_movement_event(evnt):
            self.movePair(evnt)


def gameLoop(pygame, gameState, eventHandler):
    puyoSprites = Sprites(pygame)
    gameboard = Gameboard((100,100))
    playfield = Playfield(pygame, gameboard)

    while gameState.isRunning:
        gameState.handle_event(eventHandler.get_input())

        playfield.draw(gameState.screen)

        # RENDER YOUR GAME HERE
        gameState.screen.blit(puyoSprites.red_puyo(), gameboard.grid(gameState.falling_pair_location))

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
