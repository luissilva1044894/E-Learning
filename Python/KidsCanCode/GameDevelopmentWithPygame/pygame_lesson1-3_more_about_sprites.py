
#http://kidscancode.org/blog/2016/08/pygame_1-3_more-about-sprites/

import pygame
import random
import os

# Initialize pygame and create window
pygame.init()

# For sound
pygame.mixer.init()

# Width of our game window
WINDOW_WIDTH = 360
# Height of our game window
WINDOW_HEIGHT = 480
WINDOW_TITLE = 'My Game'
FRAMES_PER_SECOND = 30

# Set up asset folders
GAME_FOLDER = os.path.dirname(__file__)
SPRITES_FOLDER = os.path.join(GAME_FOLDER, 'sprites')

SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption(WINDOW_TITLE)
CLOCK = pygame.time.Clock()
ALL_SPRITES = pygame.sprite.Group()

class Colors:
  '''Colors (R, G, B)'''
  BLACK = (0, 0, 0)
  BLUE = (0, 0, 255)
  GREEN = (0, 255, 0)
  RED = (255, 0, 0)
  WHITE = (255, 255, 255)

class Player(pygame.sprite.Sprite):
  def __init__(self, sprite, position):
    pygame.sprite.Sprite.__init__(self)
    self.image = sprite
    self.image.set_colorkey(Colors.BLACK)
    self.rect = self.image.get_rect()
    self.rect.center = position

  def update(self):
    #if self.rect.right < WINDOW_WIDTH:
    #  self.rect.x += 5
    self.rect.x += 25 * (random.random() - 0.5)
    self.rect.y += 25 * (random.random() - 0.5)
    #self.rect.x += 5
    #if self.rect.left >= WINDOW_WIDTH:
    #  self.rect.x = -self.rect.width

PLAYER_SPRITE = pygame.image.load(os.path.join(SPRITES_FOLDER, 'player.png')).convert()
PLAYER = Player(PLAYER_SPRITE, (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
ALL_SPRITES.add(PLAYER)

# Game Loop
IS_RUNNING = True

while IS_RUNNING:
  # Process input (events)
  for event in pygame.event.get():
    # Check for closing window
    if event.type == pygame.QUIT:
      IS_RUNNING = False

  # Update
  ALL_SPRITES.update()

  # Render (draw)
  SCREEN.fill(Colors.GREEN)
  ALL_SPRITES.draw(SCREEN)

  # *After* drawing everything, flip the display
  pygame.display.flip()

  # Keep loop running at the right speed
  CLOCK.tick(FRAMES_PER_SECOND)

pygame.quit()
