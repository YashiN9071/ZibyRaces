import pygame
from image_load import load_image

pygame.init()


# player
class PlayerCar(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100, 200))
        self.image.fill(pygame.Color('Red'))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, 880)

    def move(self, key):
        self.rect.move(10, 0)


# game
size = WIDTH, HEIGHT = 1920, 1080
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
        while event.type == pygame.KEYDOWN:
            player.move(event.key)
    screen.fill(pygame.Color("black"))
    player_sprite.update()
    player_sprite.draw(screen)
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
