
#http://kidscancode.org/blog/2016/08/pygame_shmup_part_1/

import pygame
import os

# Initialize pygame and create window
pygame.init()

# For sound
pygame.mixer.init()

WINDOW_WIDTH = 480 #width of our game window
WINDOW_HEIGHT = 600#height of our game window
WINDOW_TITLE = 'Pygame - Shmup! part 1'
FRAMES_PER_SECOND = 60

# set up asset folders
GAME_FOLDER = os.path.dirname(__file__)
SPRITES_FOLDER = os.path.join(GAME_FOLDER, 'sprites')

SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption(WINDOW_TITLE)
CLOCK = pygame.time.Clock()

class Colors:
  '''Colors (R, G, B)'''
  BLACK = (0, 0, 0)
  BLUE = (0, 0, 255)
  GREEN = (0, 255, 0)
  RED = (255, 0, 0)
  WHITE = (255, 255, 255)

class Player(pygame.sprite.Sprite):
  def __init__(self, width, height, position, color=Colors.BLUE):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.Surface((width, height))
    self.image.fill(color)
    self.rect = self.image.get_rect()
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

ALL_SPRITES = pygame.sprite.Group()

PLAYER = Player(50, 40, (WINDOW_WIDTH // 2, WINDOW_HEIGHT - 10))
ALL_SPRITES.add(PLAYER)

# Game Loop
IS_RUNNING = True

while IS_RUNNING:
  # Process input (events)
  for event in pygame.event.get():
    # Check for closing window
    if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key ==pygame.K_q:
      IS_RUNNING = False

  # Update
  ALL_SPRITES.update()

  SCREEN.fill(Colors.GREEN) # Render (draw)
  ALL_SPRITES.draw(SCREEN)

  # *After* drawing everything, flip the display
  pygame.display.flip()

  # Keep loop running at the right speed
  CLOCK.tick(FRAMES_PER_SECOND)

pygame.quit()
