
#http://kidscancode.org/blog/2016/08/pygame_1-1_getting-started/

import pygame

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

class Colors:
  '''Colors (R, G, B)'''
  BLACK = (0, 0, 0)
  BLUE = (0, 0, 255)
  GREEN = (0, 255, 0)
  RED = (255, 0, 0)
  WHITE = (255, 255, 255)

# Game Loop
IS_RUNNING = True

while IS_RUNNING:
  # Process input (events)
  for event in pygame.event.get():
    # Check for closing window
    if event.type == pygame.QUIT:
      IS_RUNNING = False

  # Update

  # Render (draw)
  SCREEN.fill(Colors.BLACK)

  # *After* drawing everything, flip the display
  pygame.display.flip()

  # Keep loop running at the right speed
  CLOCK.tick(FRAMES_PER_SECOND)

pygame.quit()
