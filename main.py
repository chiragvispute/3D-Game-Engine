import pygame as py
import sys
from settings import *
from map import *
from player import *
from raycasting import *

class Game:
    def __init__(self):
        py.init()
        self.screen = py.display.set_mode((WIDTH, HEIGHT))
        self.clock = py.time.Clock()
        self.delta_time=1
        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.raycasting=Raycasting(self)

    def update(self):
        self.player.update()
        self.raycasting.update()
        py.display.update()
        self.delta_time= self.clock.tick(FPS)


    def draw(self):
        self.screen.fill('Black')
        # self.draw_map()
        # self.player.draw()


    def draw_map(self):
        for y in range(MAP_HEIGHT):
            for x in range(MAP_WIDTH):
                color = (200, 200, 200) if map[y][x] == 1 else (50, 50, 50)
                py.draw.rect(self.screen, color,
                             (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    def check_events(self):
        for event in py.event.get():
            if event.type == py.QUIT or event.type == py.K_F5:
                py.quit()
                sys.exit()


    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__':
    game = Game()
    game.run()