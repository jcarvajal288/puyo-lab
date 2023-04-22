import pygame
import event
from event import EventHandler
import gameboard
from gameboard import Gameboard
from playfield import Playfield
import sprites
from sprites import Sprites

class GameState():
    def __init__(self, pygame):
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.isRunning = True
        self.falling_pair_type = 'ry'
        self.falling_pair_location = ((2, 0), (2, -1))

    def movePair(self, evnt):
        (x, y), (a, b) = self.falling_pair_location

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

        self.falling_pair_location = ((x, y), (a, b))

    def handle_event(self, evnt):
        if evnt == event.EVENT_QUIT:
            self.isRunning = False
        elif event.is_movement_event(evnt):
            self.movePair(evnt)


def render_falling_pair(gameState, gameboard, puyoSprites):
    puyos = puyoSprites.get_image_pair(gameState.falling_pair_type)
    puyo_frame = pygame.time.get_ticks() // sprites.ANIMATION_SPEED_IN_MS % 4
    pair_grid_locations = [gameboard.grid(x) for x in gameState.falling_pair_location]
    for puyo, grid in zip(puyos, pair_grid_locations):
        gameState.screen.blit(puyo[puyo_frame], grid)

def gameLoop(pygame, gameState, eventHandler):
    puyoSprites = Sprites(pygame)
    gameboard = Gameboard((100,100))
    playfield = Playfield(pygame, gameboard)

    while gameState.isRunning:
        gameState.handle_event(eventHandler.get_input())

        playfield.draw(gameState.screen)

        # RENDER YOUR GAME HERE
        render_falling_pair(gameState, gameboard, puyoSprites)

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
