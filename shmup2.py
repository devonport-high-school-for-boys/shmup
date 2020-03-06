#import libraries
import pygame
import random

#create a window/constants
WIDTH = 800
HEIGHT = 600
FPS = 30 #how many times per sec sreen refreshed
#define colours so can Reuse
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255, 0, 0)
GREEN = (0,255,0)
BLUE = (0,0,255)


class Player(pygame.sprite.Sprite):
  #sprite for player
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.Surface((50,50))
    self.image.fill(GREEN)
    self.rect = self.image.get_rect()
    self.rect.center=(WIDTH/2,HEIGHT/2)
  def update(self):
    self.rect.x += 5
    if self.rect.left > WIDTH:
      self.rect.right = 0

pygame.init()#initialise pygame
#pygame.mixer.init()#initialise mixer for sound
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
#game Loop
#while loop, that also needs to be able to stop
running = True
while running:
  #keep running at right speed
  clock.tick(FPS)
  #process input(events)
  for event in pygame.event.get():
  #close event 
    if event.type == pygame.QUIT:
      running = False 

  #update
  all_sprites.update()
  #draw/update
  screen.fill(BLACK)
  all_sprites.draw(screen)
  #always do last, draw then flip
  pygame.display.flip()
  
pygame.quit()