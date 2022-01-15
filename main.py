import sys
import pygame
import random

# from image_load import load_image

pygame.init()

size = WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode(size)

fps = 100
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
def menu_button(text, coords):
    pass


def obstacle_check(p_rect):
    for obstacle in obstacles_sprite:
        if p_rect.colliderect(obstacle.rect):
            obstacle.kill()
            return True


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


# game
font = pygame.font.SysFont('arial', 50)

player_sprite = pygame.sprite.Group()
obstacles_sprite = pygame.sprite.Group()
not_an_object_sprite = pygame.sprite.Group()
buttons_sprite = pygame.sprite.Group()


run = True
while run:
    # start game
    intro_text = ['Ziby Races', ' ', 'press any key to continue']

    fon = pygame.transform.scale(pygame.Surface(size), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    text_coord = 0
    f = pygame.font.SysFont('arial', 250)
    for line in intro_text:
        string_rendered = f.render(line, True, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        f = pygame.font.SysFont('arial', 30)
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.center = (WIDTH // 2, HEIGHT // 2 + text_coord)
        text_coord += 200
        screen.blit(string_rendered, intro_rect)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    run = False
                running = False
        pygame.display.flip()
        clock.tick(fps)

    if not run:
        break

    # environment
    for pos in range(510, 1411, 300):
        environment_image = pygame.Surface((10, HEIGHT))
        environment_image.fill(pygame.Color('White'))
        environment = pygame.sprite.Sprite(not_an_object_sprite)
        environment.image = environment_image
        environment.rect = environment_image.get_rect()
        environment.rect.left += pos

    f = pygame.font.SysFont('arial', 30)
    string_rendered = f.render("To move use keys: 'A' and 'D'", True, pygame.Color('white'))
    hint_rect = string_rendered.get_rect()
    hint_rect.center = (180, 1040)
    screen.blit(string_rendered, hint_rect)

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
                if event.key == pygame.K_ESCAPE:
                    running = False
                    run = False

        # create obstacles
        if tps >= 250:
            random_obstacle()
            tps = 0

        # check score
        if score >= 100000:
            running = False

        # check intersection
        player_rect = player.rect_check()
        a = obstacle_check(player_rect)
        if a:
            running = False

        # screen update
        screen.fill(pygame.Color("black"))
        score_text = font.render('Your score: ' + str(score), True, (255, 255, 255))
        screen.blit(score_text, (20, 10))
        screen.blit(string_rendered, hint_rect)
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

    if not run:
        break

    with open('score.txt') as file:
        b = file.readlines()
        k = b[-1].split()[0]
        print(k)
        k = int(k)
        k += 1
        print(k)

    with open('score.txt', 'w') as file:
        for i in b:
            print(i, file=file, end='')
        print(f'{k} game: {score}', file=file)

    # end game
    intro_text = ['Game Over', ' ', f'Your result: {score}', ' ', 'press any key to go back to start screen']

    fon = pygame.transform.scale(pygame.Surface(size), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    text_coord = 0
    f = pygame.font.SysFont('arial', 200)
    for line in intro_text:
        string_rendered = f.render(line, True, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        f = pygame.font.SysFont('arial', 30)
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.center = (WIDTH // 2, HEIGHT // 2 + text_coord)
        text_coord += 50
        screen.blit(string_rendered, intro_rect)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    run = False
                running = False
        pygame.display.flip()
        clock.tick(fps)

pygame.quit()
