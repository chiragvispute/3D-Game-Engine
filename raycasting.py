import pygame as py
import math
from settings import *
from map import *

class Raycasting:
    def __init__(self, game):
        self.game = game

    def ray_cast(self):
        ox, oy = self.game.player.pos()  # Player's current position
        map_x, map_y = self.game.player.map_pos()  # Player's grid position
        ray_angle = self.game.player.angle - HALF_FOV + 0.0001

        for ray in range(NUM_RAYS):
            sin_a = math.sin(ray_angle)
            cos_a = math.cos(ray_angle)

            # Horizontal ray casting
            if sin_a > 0:
                y_hor = map_y + 1
                dy = 1
            else:
                y_hor = map_y - 0.0001
                dy = -1

            depth_hor = (y_hor - oy) / sin_a
            x_hor = ox + depth_hor * cos_a
            delta_depth = dy / sin_a
            dx = delta_depth * cos_a

            for i in range(MAX_DEPTH):
                tile_hor = (int(x_hor), int(y_hor))
                if tile_hor in self.game.map.world_map:  # Check if tile is a wall
                    depth_hor = depth_hor  # The depth is already calculated
                    break
                x_hor += dx
                y_hor += dy
                depth_hor += delta_depth

            # Vertical ray casting
            if cos_a > 0:
                x_vert = map_x + 1
                dx = 1
            else:
                x_vert = map_x - 0.0001
                dx = -1

            depth_vert = (x_vert - ox) / cos_a
            y_vert = oy + depth_vert * sin_a
            delta_depth = dx / cos_a
            dy = delta_depth * sin_a

            for i in range(MAX_DEPTH):
                tile_vert = (int(x_vert), int(y_vert))
                if tile_vert in self.game.map.world_map:
                    break
                x_vert += dx
                y_vert += dy
                depth_vert += delta_depth

            if depth_vert < depth_hor:
                depth = depth_vert
            else:
                depth = depth_hor


            depth*=math.cos(self.game.player.angle-ray_angle)

           #projection height
            projection_height = SCREEN_DIST/ (depth +0.0001)
            normalized_depth = min(depth, MAX_DEPTH) / MAX_DEPTH
            color_intensity = int((1 - normalized_depth) * 255)
            color = (color_intensity, color_intensity, color_intensity)

            py.draw.rect(self.game.screen, color,
                         (ray *SCALE, HALF_HEIGHT-projection_height//2, SCALE, projection_height))

            ray_angle += DELTA_ANGLE

    def update(self):
        self.ray_cast()
