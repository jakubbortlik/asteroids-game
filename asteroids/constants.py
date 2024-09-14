import os

import pygame.freetype

dir_name = os.path.dirname(os.path.realpath(__file__))
FONT_PATH = os.path.join(dir_name, "../data/fonts/JetBrainsMonoNerdFont-Medium.ttf")

pygame.freetype.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# For debugging, set `scale` to a higher value to make asteroids move slower
scale = 1.0
ASTEROID_MIN_SPEED = int(40 / scale)
ASTEROID_MAX_SPEED = int(100 / scale)
ASTEROID_MIN_RADIUS = 20.0
ASTEROID_KINDS = 3
ASTEROID_LINE_WIDTH = 2
ASTEROID_SPAWN_RATE = 0.8  # seconds
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS

PLAYER_SIZE = 20.0
PLAYER_LINE_WIDTH = 2
PLAYER_TURN_SPEED = 300
PLAYER_SPEED = 200
PLAYER_MAX_SPEEDUP = 200
PLAYER_SHOOT_COOLDOWN = 0.3

SHOT_LINE_WIDTH = 0
SHOT_RADIUS = 5.0
SHOT_SPEED = 700

SCORE_BOX_FONT_SIZE = 12
FONT = pygame.freetype.Font(file=FONT_PATH, size=SCORE_BOX_FONT_SIZE)
SCORE_BOX_WIDTH = 150
SCORE_BOX_HEIGHT = 30
SCORE_BOX_X = SCREEN_WIDTH - SCORE_BOX_WIDTH - 10
SCORE_BOX_Y = 10
SCORE_BOX_BORDER_WIDTH = 1
SCORE_BOX_PADDING = 10

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GRAY = (100, 100, 100)
AZURE = (0, 127, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
