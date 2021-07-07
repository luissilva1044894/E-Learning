
#http://kidscancode.org/blog/2016/08/pygame_1-2_working-with-sprites/

import pygame
import random

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
  def __init__(self, width, height, position, color=Colors.GREEN, *args, **kwargs):
    self.image = pygame.Surface((width, height))
    self.image.fill(color)
    self.rect = self.image.get_rect()
    self.rect.center = position
    pygame.sprite.Sprite.__init__(self, *args, **kwargs)

  def update(self):
    #if self.rect.right < WINDOW_WIDTH:
    #  self.rect.x += 5
    #self.rect.x += 25 * (random.random() - 0.5)
    #self.rect.y += 25 * (random.random() - 0.5)
    self.rect.x += 5
    if self.rect.left >= WINDOW_WIDTH:
      self.rect.x = -player.rect.width

player = Player(50, 50, (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
ALL_SPRITES.add(player)

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
  SCREEN.fill(Colors.BLACK)

  ALL_SPRITES.draw(SCREEN)

  # *After* drawing everything, flip the display
  pygame.display.flip()

  # Keep loop running at the right speed
  CLOCK.tick(FRAMES_PER_SECOND)

pygame.quit()
