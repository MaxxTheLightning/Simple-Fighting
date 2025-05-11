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

class Line(sprite.Sprite):
    def __init__(self, sprite_image, x, y, scale_x, scale_y):
        super().__init__()

        self.image = transform.scale(image.load(sprite_image), (scale_x, scale_y))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def reset(self):

        window.blit(self.image, (self.rect.x, self.rect.y))


window = display.set_mode((700, 500))
display.set_caption("Space Shooter Beta")
bg = image.load("Media/bg.jpg")
background = transform.scale(bg, (700, 500))
first_player = GameSprite('Media/player.png', 400, 100, 2, 60)
second_player = GameSprite('Media/player2.png', 100, 100, 2, 60)
red_board = Line('Media/red_line.png', 340, 0, 20, 500)
green_board1 = Line('Media/green_line.png',0 , 0, 200, 500)
green_board2 = Line('Media/green_line.png',500, 0, 200, 500)
#   Game

game = True

while game:

    #   Show background

    window.blit(background, (0, 0))
    red_board.reset()
    green_board1.reset()
    green_board2.reset()
    first_player.reset()
    second_player.reset()
    clock = time.Clock()
    FPS = 60
    clock.tick(FPS)

    #   Application closing

    for e in event.get():

        if e.type == QUIT:

            game = False
        
    keys_pressed = key.get_pressed()

    if keys_pressed[K_LEFT] and  first_player.rect.x > 355:
        first_player.rect.x -=  first_player.speed
    if keys_pressed[K_RIGHT] and  first_player.rect.x < 635:
        first_player.rect.x +=  first_player.speed
    if keys_pressed[K_UP] and  first_player.rect.y > 5:
        first_player.rect.y -=  first_player.speed
    if keys_pressed[K_DOWN] and  first_player.rect.y < 395:
        first_player.rect.y +=  first_player.speed

 
    if keys_pressed[K_a] and second_player.rect.x > 5:
        second_player.rect.x -=  second_player.speed
    if keys_pressed[K_d] and  second_player.rect.x < 285:
        second_player.rect.x +=  second_player.speed
    if keys_pressed[K_w] and  second_player.rect.y > 5:
        second_player.rect.y -=  second_player.speed
    if keys_pressed[K_s] and  second_player.rect.y < 395:
        second_player.rect.y +=  second_player.speed





    display.update()