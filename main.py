import pygame
pygame.init()


WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
ROCKET_IMG = 'Rocket.png'
BALL_IMG = 'Ball.jpg'
BACKGROUND_COLOR = (224, 255, 255)


window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Ping-Pong')
window.fill(BACKGROUND_COLOR)
clock = pygame.time.Clock()


class Sprite(pygame.sprite.Sprite):
    def __init__(self, image, x=0, y=0, width=0, height=0):
        image = pygame.image.load(image)
        self.image = pygame.transform.scale(image, (width, height))
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(Sprite):
    def __init__(self, image, x=0, y=0, width=0, height=0, speed=5, k_up=pygame.K_UP, k_down=pygame.K_DOWN):
        super().__init__(image, x, y, width, height)
        self.speed = speed
        self.k_up = k_up
        self.k_down = k_down
    
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[self.k_up] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[self.k_down] and self.rect.y < (WINDOW_HEIGHT - self.rect.height):
            self.rect.y += self.speed


class Ball(Sprite):
    dx = 5
    dy = 5
    def update(self, player_1, player_2):
        if self.rect.y <= 0:
            dy *= -1
        if self.rect.y >= (WINDOW_HEIGHT - self.rect.height):
            dy *= -1
        if self.rect.colliderect(player_1.rect):
            dx *= -1
        if self.rect.colliderect(player_2.rect):
            dx *= -1
        self.rect.x += dx
        self.rect.y += dy


player_left = Player(ROCKET_IMG, 20, 5, 40, 150, 5, pygame.K_w, pygame.K_s)
player_right = Player(ROCKET_IMG, 740, WINDOW_HEIGHT-105, 40, 150, 5)
ball = Ball(BALL_IMG, 250, 250, 50, 50)


game_status = 'game'
while game_status != 'off':
    window.fill(BACKGROUND_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_status = 'off'
    
    ball.update(player_left, player_right)
    player_left.update()
    player_right.update()
    ball.draw()
    player_left.draw()
    player_right.draw()
    clock.tick(60)
    pygame.display.update()