#import libraries
import pygame
import random

#create a window/constants for vertical
WIDTH = 480
HEIGHT = 600
FPS = 60 #how many times per sec sreen refreshed
#define colours so can Reuse
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255, 0, 0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)

pygame.init()#initialise pygame
#pygame.mixer.init()#initialise mixer for sound
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Shmup!")
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.Surface((50,40))
    self.image.fill(GREEN)
    self.rect = self.image.get_rect()
    self.rect.centerx = WIDTH/2
    self.rect.bottom = HEIGHT -10
    self.speedx = 0

  def update(self):
    #tell it to always be still
    self.speedx = 0
    #pygame.key_getpressed returns a list of keys pressed
    keystate = pygame.key.get_pressed()
    if  keystate[pygame.K_LEFT]:
      self.speedx = -5
    if keystate[pygame.K_RIGHT]:
      self.speedx = 5
    self.rect.x += self.speedx
    #set sides as walls
    if self.rect.right > WIDTH:
      self.rect.right = WIDTH
    if self.rect.left < 0:
      self.rect.left = 0

  def shoot(self):
    bullet = Bullet(self.rect.centerx, self.rect.top)
    all_sprites.add(bullet)
    bullets.add(bullet)
#set up enemies
class Mob(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.Surface((30,40))
    self.image.fill(RED) 
    self.rect = self.image.get_rect() 
    self.rect.x = random.randrange(WIDTH - self.rect.width)
    self.rect.y = random.randrange(-100,-40)
    self.speedy = random.randrange(1,8)
    self.speedx = random.randrange(-3,3)

  def update(self):
    self.rect.x +=self.speedx
    self.rect.y += self.speedy
    if self.rect.top > HEIGHT +10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
      self.rect.x = random.randrange(WIDTH - self.rect.width)
      self.rect.y = random.randrange(-100,-40)
      self.speedy = random.randrange(1,8)
      
class Bullet(pygame.sprite.Sprite):
  def __init__(self,x,y):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.Surface((10,20))
    self.image.fill(YELLOW)
    self.rect = self.image.get_rect()
    self.rect.bottom = y
    self.rect.centerx = x
    self.speedy = -10

  def update(self):
    self.rect.y +=self.speedy
    #kill if it gets to Top 
    if self.rect.bottom <0:
      self.kill()

all_sprites = pygame.sprite.Group()
all_mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
for i in range(8):
  m = Mob()
  all_sprites.add(m)
  all_mobs.add(m)
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
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        player.shoot() 

  #update
  all_sprites.update()
  #check if bullet hit Mob
  hits = pygame.sprite.groupcollide(all_mobs, bullets, True, True)
  for hit in hits:
    m = Mob()
    all_sprites.add(m)
    all_mobs.add(m)



  #check to see if mob hits player
  hits = pygame.sprite.spritecollide(player, all_mobs, False)
  if hits:
    running = False
  #draw/update
  screen.fill(BLACK)
  all_sprites.draw(screen)
  #always do last, draw then flip
  pygame.display.flip()
  
pygame.quit()
