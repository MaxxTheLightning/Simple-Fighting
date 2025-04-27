from pygame import *
from random import randint

#   GameSprite - main class for all sprites

class GameSprite(sprite.Sprite):

    def __init__(self, sprite_image, x, y, speed, scale):

        super().__init__()

        self.image = transform.scale(image.load(sprite_image), (scale, scale))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):

        window.blit(self.image, (self.rect.x, self.rect.y))

window = display.set_mode((700, 500))
display.set_caption("Space Shooter Beta")
bg = image.load("Media/bg.jpg")
background = transform.scale(bg, (700, 500))
player = GameSprite('Media/player.png', 100, 100, 2, 60)

#   Game

game = True

while game:

    #   Show background

    window.blit(background, (0, 0))
    player.reset()
    clock = time.Clock()
    FPS = 60
    clock.tick(FPS)

    #   Application closing

    for e in event.get():

        if e.type == QUIT:

            game = False
        
    keys_pressed = key.get_pressed()

    if keys_pressed[K_LEFT] and player.rect.x > 5:
       player.rect.x -= player.speed
    if keys_pressed[K_RIGHT] and player.rect.x < 595:
        player.rect.x += player.speed
    if keys_pressed[K_UP] and player.rect.y > 5:
        player.rect.y -= player.speed
    if keys_pressed[K_DOWN] and player.rect.y < 395:
        player.rect.y += player.speed




    display.update()