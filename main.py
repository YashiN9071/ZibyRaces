import pygame
# from image_load import load_image

pygame.init()


# player
class PlayerCar(pygame.sprite.Sprite):
    def __init__(self):
        self.for_move = 2
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100, 200))
        self.image.fill(pygame.Color('Red'))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, 880)

    def move(self, key):
        if key == pygame.K_a and self.for_move - 1 > 0:
            self.rect.left -= 300
            self.for_move -= 1
        elif key == pygame.K_d and self.for_move + 1 < 4:
            self.rect.left += 300
            self.for_move += 1

    def game_over(self):
        pass


# obstacles
class Obstacle:
    def __init__(self):
        pass

    def move(self):
        pass


# game
size = WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode(size)

all_sprites = pygame.sprite.Group()
player_sprite = pygame.sprite.Group()
obstacle_sprite = pygame.sprite.Group()
not_an_object_sprite = pygame.sprite.Group()

# environment
for pos in range(505, 1406, 300):
    environment_image = pygame.Surface((10, HEIGHT))
    environment_image.fill(pygame.Color('White'))
    environment = pygame.sprite.Sprite(not_an_object_sprite)
    environment.image = environment_image
    environment.rect = environment_image.get_rect()
    environment.rect.left += pos

player = PlayerCar()
player_sprite.add(player)

fps = 60
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            player.move(event.key)
    screen.fill(pygame.Color("black"))
    not_an_object_sprite.update()
    player_sprite.update()
    not_an_object_sprite.draw(screen)
    player_sprite.draw(screen)
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
