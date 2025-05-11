from pygame import *

bullets = []

#   Classes

class GameSprite(sprite.Sprite):

    def __init__(self, sprite_image, x, y, scale):

        super().__init__()

        self.image = transform.scale(image.load(sprite_image), (scale, scale))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):

        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):

    def __init__(self, sprite_image, x, y, speed, scale):

        super().__init__(sprite_image, x, y, scale)

        self.shoot_counter = 0
        self.speed = speed
        self.health = 3

    def update(self):

        if keys_pressed[K_LEFT] and player.rect.x > 5:
            
            player.rect.x -= player.speed

        if keys_pressed[K_RIGHT] and player.rect.x < 595:

            player.rect.x += player.speed

        if keys_pressed[K_UP] and player.rect.y > 5:

            player.rect.y -= player.speed

        if keys_pressed[K_DOWN] and player.rect.y < 395:

            player.rect.y += player.speed

        if keys_pressed[K_SPACE]:
            
            if self.shoot_counter == 0:

                self.fire("right")

            self.shoot_counter += 1

            if self.shoot_counter > 20:

                self.shoot_counter = 0
        
        else:

            self.shoot_counter = 0

    def fire(self, direction):

        if direction == "right":

            dir = 10
            x = self.rect.x + 30

        elif direction == "left":

            dir = -10
            x = self.rect.x - 30

        bullet = Bullet('Media/Bullet.png', x, self.rect.y + 10, dir, 40)

        if direction == "left":

            bullet.image = transform.flip(bullet.image, True, False)

        bullets.append(bullet)

        fire.play()

    def damage(self):

        self.health -= 1

class Bullet(GameSprite):

    def __init__(self, sprite_image, x, y, speed, scale):

        super().__init__(sprite_image, x, y, scale)

        self.speed = speed

    def update(self):

        self.rect.x += self.speed

#   Setup the scene

window = display.set_mode((700, 500))
display.set_caption("Space Shooter Beta")
bg = image.load("Media/bg.jpg")
background = transform.scale(bg, (700, 500))

#   Audioeffects setup

mixer.init()
fire = mixer.Sound('Media/new_fire.wav')

#   Setup sprites

player = Player('Media/player.png', 100, 100, 5, 60)

hearts = []

heart_x = 0

for i in range(player.health):

    heart = GameSprite('Media/Heart.png', heart_x, 5, 50)

    hearts.append(heart)

    heart_x += 50

#   Game

game = True

while game:

    #   Show background

    window.blit(background, (0, 0))
    player.reset()
    clock = time.Clock()
    FPS = 60
    clock.tick(FPS)

    #   Managing bullets

    if len(bullets) > 0:

        for this_bullet in bullets:

            this_bullet.reset()
            this_bullet.update()

            if this_bullet.rect.x < -50 or this_bullet.rect.x > 750:

                del bullets[bullets.index(this_bullet)]

    if len(hearts) > 0:

        for h in hearts:

            h.reset()

    #   Application closing

    for e in event.get():

        if e.type == QUIT:

            game = False
        
    keys_pressed = key.get_pressed()

    player.update()

    display.update()