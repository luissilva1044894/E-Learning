
#http://kidscancode.org/blog/2016/08/pygame_shmup_part_2/

import pygame
import random
import os

# Initialize pygame and create window
pygame.init()

# For sound
pygame.mixer.init()

# Width of our game window
WINDOW_WIDTH = 480
# Height of our game window
WINDOW_HEIGHT = 600
WINDOW_TITLE = 'Pygame - Shmup! part 1'
FRAMES_PER_SECOND = 60

# set up asset folders
GAME_FOLDER = os.path.dirname(__file__)
SPRITES_FOLDER = os.path.join(GAME_FOLDER, 'sprites')

SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption(WINDOW_TITLE)
CLOCK = pygame.time.Clock()

ALL_SPRITES, ENEMIES_SPRITES = pygame.sprite.Group(), pygame.sprite.Group()

class Colors:
  '''Colors (R, G, B)'''
  BLACK = (0, 0, 0)
  BLUE = (0, 0, 255)
  GREEN = (0, 255, 0)
  RED = (255, 0, 0)
  WHITE = (255, 255, 255)

  @staticmethod
  def rand():
    return random.choice([Colors.BLACK, Colors.GREEN, Colors.RED])

class BaseSprite(pygame.sprite.Sprite):
  def __init__(self, width, height, color=None, *args, **kw):
    pygame.sprite.Sprite.__init__(self, *args, **kw)
    self.image = pygame.Surface((width, height))
    self.image.fill(color or Colors.rand())
    self.rect = self.image.get_rect()
    ALL_SPRITES.add(self)

class Player(BaseSprite):
  def __init__(self, width, height, position, color=Colors.BLUE):
    BaseSprite.__init__(self, width, height, color)
    self.rect.centerx, self.rect.bottom = position
    self.speed = 2

  def update(self):
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_LEFT] and self.rect.x > 0:
      self.rect.x -= self.speed
    elif keystate[pygame.K_RIGHT] and self.rect.x + self.rect.width < WINDOW_WIDTH:
      self.rect.x += self.speed
    #if self.rect.right > WIDTH: self.rect.right = WIDTH
    #elif self.rect.left < 0: self.rect.left = 0

class Mob(BaseSprite):
  def __init__(self, width, height, color=None):
    BaseSprite.__init__(self, width, height, color)
    ENEMIES_SPRITES.add(self)
    self.random_pos_and_speed()

  def random_pos_and_speed(self):
    self.rect.x, self.rect.y = random.randrange(WINDOW_WIDTH - self.rect.width), random.randrange(-100, -40)
    self.speed = random.randrange(1, 8)

  def update(self):
    self.rect.y += self.speed
    if self.rect.top > WINDOW_HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WINDOW_WIDTH + 20:
      self.random_pos_and_speed()

PLAYER = Player(50, 40, (WINDOW_WIDTH // 2, WINDOW_HEIGHT - 10))
for i in range(8):
  mob = Mob(random.randrange(10, 30), random.randrange(10, 40))

# Game Loop
IS_RUNNING = True

while IS_RUNNING:
  # Process input (events)
  for event in pygame.event.get():
    # Check for closing window
    if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_q:
      IS_RUNNING = False

  # Update
  ALL_SPRITES.update()

  # Render (draw)
  SCREEN.fill(Colors.WHITE)
  ALL_SPRITES.draw(SCREEN)

  # *After* drawing everything, flip the display
  pygame.display.flip()

  # Keep loop running at the right speed
  CLOCK.tick(FRAMES_PER_SECOND)

pygame.quit()
