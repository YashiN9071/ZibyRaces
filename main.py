import pygame


class PlayerCar(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100, 50))
        self.image.fill(pygame.Color('RED'))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def move(self, key):
        if key == pygame.K_w:
            a = 1
        if key == pygame.K_a:
            a = 1
        if key == pygame.K_s:
            a = 1
        if key == pygame.K_d:
            a = 1


# game
pygame.init()

size = WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode(size)

all_sprites = pygame.sprite.Group()
player_sprite = pygame.sprite.Group()

player = PlayerCar()
player_sprite.add(player)

fps = 30
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            player.move(event.key)
    screen.fill(pygame.Color("black"))
    player_sprite.update()
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
