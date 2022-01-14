import sys
import pygame
import pygame_menu
import random

from image_load import load_image

pygame.init()

size = WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode(size)

fps = 60
clock = pygame.time.Clock()


# menu class
class Menu:
    def __init__(self):
        pass


# player
class PlayerCar(pygame.sprite.Sprite):
    def __init__(self):
        self.for_move = 2
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100, 200))
        self.image.fill(pygame.Color('White'))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, 780)

    def move(self, key):
        if key == pygame.K_a and self.for_move - 1 > 0:
            self.rect.left -= 300
            self.for_move -= 1
        elif key == pygame.K_d and self.for_move + 1 < 4:
            self.rect.left += 300
            self.for_move += 1

    def rect_check(self):
        return self.rect

    def game_over(self):
        self.kill()


# obstacles
class ObstacleCar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(obstacles_sprite)
        self.image = pygame.Surface((100, 200))
        self.image.fill(pygame.Color('White'))
        self.rect = self.image.get_rect()
        place = random.randrange(660, 1261, 300)
        self.rect.center = (place, -100)

    def update(self):
        self.rect.top += 3
        if self.rect.y > 1100:
            self.kill()


class ObstacleCarFromYou(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(obstacles_sprite)
        self.image = pygame.Surface((100, 200))
        self.image.fill(pygame.Color('White'))
        self.rect = self.image.get_rect()
        place = random.randrange(660, 1261, 300)
        self.rect.center = (place, -100)

    def update(self):
        self.rect.top += 2
        if self.rect.y > 1100:
            self.kill()


class ObstacleCarOnYou(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(obstacles_sprite)
        self.image = pygame.Surface((100, 200))
        self.image.fill(pygame.Color('White'))
        self.rect = self.image.get_rect()
        place = random.randrange(660, 1261, 300)
        self.rect.center = (place, -100)

    def update(self):
        self.rect.top += 5
        if self.rect.y > 1100:
            self.kill()


class BigObstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(obstacles_sprite)
        self.image = pygame.Surface((300, 300))
        self.image.fill(pygame.Color('White'))
        self.rect = self.image.get_rect()
        place = random.randrange(660, 1261, 300)
        self.rect.center = (place, -100)

    def update(self):
        self.rect.top += 3
        if self.rect.y > 1100:
            self.kill()


class SmallObstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(obstacles_sprite)
        self.image = pygame.Surface((300, 50))
        self.image.fill(pygame.Color('White'))
        self.rect = self.image.get_rect()
        place = random.randrange(660, 1261, 300)
        self.rect.center = (place, -100)

    def update(self):
        self.rect.top += 3
        if self.rect.y > 1100:
            self.kill()


# functions
def obstacle_check(p_rect):
    for obstacle in obstacles_sprite:
        if p_rect.colliderect(obstacle.rect):
            obstacle.kill()
            pygame.quit()
            sys.exit()


def random_obstacle():
    obst = random.randrange(1, 6, 1)
    if obst == 1:
        ObstacleCar()
    elif obst == 2:
        ObstacleCarOnYou()
    elif obst == 3:
        ObstacleCarFromYou()
    elif obst == 4:
        BigObstacle()
    elif obst == 5:
        SmallObstacle()


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = ['Ziby Races', ' ', 'press any key to continue']

    fon = pygame.transform.scale(pygame.Surface(size), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    text_coord = 0
    f = pygame.font.SysFont('arial', 250)
    for line in intro_text:
        string_rendered = f.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        f = pygame.font.SysFont('arial', 30)
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.center = (WIDTH // 2, HEIGHT // 2 + text_coord)
        text_coord += 200
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(fps)


def set_difficulty(value, difficulty):
    pass


def start_the_game():
    return False


# game
font = pygame.font.SysFont('arial', 50)

player_sprite = pygame.sprite.Group()
obstacles_sprite = pygame.sprite.Group()
not_an_object_sprite = pygame.sprite.Group()

start_screen()

run = True
while run:
    # menu
    running = True
    while running:
        menu = pygame_menu.Menu('Welcome', 400, 300, theme=pygame_menu.themes.THEME_BLUE)

        menu.add.text_input('Name :', default='John Doe')
        menu.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
        menu.add.button('Play', start_the_game)
        menu.add.button('Quit', pygame_menu.events.EXIT)

    # environment
    for pos in range(510, 1411, 300):
        environment_image = pygame.Surface((10, HEIGHT))
        environment_image.fill(pygame.Color('White'))
        environment = pygame.sprite.Sprite(not_an_object_sprite)
        environment.image = environment_image
        environment.rect = environment_image.get_rect()
        environment.rect.left += pos

    player = PlayerCar()
    player_sprite.add(player)

    score = 0
    tps = 200

    running = True
    while running:
        # buttons
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                player.move(event.key)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    score += 100000

        # create obstacles
        if tps >= 250:
            random_obstacle()
            tps = 0

        # check score
        if score >= 100000:
            running = False
            run = False

        # check intersection
        player_rect = player.rect_check()
        obstacle_check(player_rect)

        # screen update
        screen.fill(pygame.Color("black"))
        score_text = font.render('Your score: ' + str(score), 5, (255, 255, 255))
        screen.blit(score_text, (20, 10))
        not_an_object_sprite.update()
        obstacles_sprite.update()
        player_sprite.update()
        not_an_object_sprite.draw(screen)
        obstacles_sprite.draw(screen)
        player_sprite.draw(screen)

        # ticks and points
        pygame.display.flip()
        clock.tick(fps)
        score += 1
        tps += 1

pygame.quit()
