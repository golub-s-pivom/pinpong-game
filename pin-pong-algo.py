from pygame import *

font.init()
font1 = font.Font(None, 36)
mixer.init()
win_width, win_height = 700, 500
display.set_caption('поньк')
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load("fon.gpj.webp"),(win_width,win_height ))

class GameSprite(sprite.Sprite):
    def __init__(self, sprite_image, sprite_x, sprite_y, sprite_speed,w,h):
        super().__init__()
        self.image = transform.scale(image.load(sprite_image), (w,h))
        self.speed = sprite_speed
        self.rect = self.image.get_rect()
        self.rect.x = sprite_x
        self.rect.y = sprite_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 65:
            self.rect.x += self.speed
class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 65:
            self.rect.x += self.speed
player1 = player1 = Player1("roketka.webp", 5, win_height - 80, 1,65,65)
player2 = player2 = Player2("roketka1.webp", 5, 100 - 80, 1,65,65)
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load("fon.gpj.webp"),(win_width,win_height ))

FPS = 60
game = True
while game:
    window.blit(background,(0,0))
    player1.reset()
    player2.reset()
    for e in event.get():
        if e.type == QUIT:
            game = False
    player1.update()
    player2.update()
    display.update()
