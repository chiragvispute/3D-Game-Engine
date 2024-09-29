
from settings import *
import pygame as py
import math
from map import *

class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE

    def check_collision(self, new_x, new_y):

        tile_x = int(new_x)
        tile_y = int(new_y)

        if tile_x < 0 or tile_x >= MAP_WIDTH or tile_y < 0 or tile_y >= MAP_HEIGHT:
            return True
        if map[tile_y][tile_x] == 1:
            return True

        return False

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = PLAYER_SPEED * self.game.delta_time

        keys = py.key.get_pressed()
        if keys[py.K_w]:
            dx += speed * cos_a
            dy += speed * sin_a
        if keys[py.K_a]:
            dx += speed * -sin_a
            dy += speed * cos_a
        if keys[py.K_s]:
            dx += speed * -cos_a
            dy += speed * -sin_a
        if keys[py.K_d]:
            dx += speed * sin_a
            dy += speed * -cos_a

        new_x = self.x+ dx
        new_y = self.y+ dy

        if not self.check_collision(new_x, new_y):
            self.x = new_x
            self.y = new_y

        if keys[py.K_LEFT]:
            self.angle -= PLAYER_ROT * self.game.delta_time
        if keys[py.K_RIGHT]:
            self.angle += PLAYER_ROT * self.game.delta_time

        self.angle %= 2 * math.pi

    def draw(self):
        # Draw the direction line
        # py.draw.line(self.game.screen, 'yellow', (self.x * 100, self.y * 100),
        #              (self.x * 100 + WIDTH * math.cos(self.angle),
        #               self.y * 100 + WIDTH * math.sin(self.angle)), 2)
        # Draw the player position
        py.draw.circle(self.game.screen, 'green', (int(self.x * 100), int(self.y * 100)), 15)

    def update(self):
        self.movement()

    def pos(self):
        return self.x, self.y

    def map_pos(self):
        return int(self.x), int(self.y)
