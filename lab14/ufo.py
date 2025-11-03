import pygame
from dataclasses import dataclass

WIDTH, HEIGHT = 800, 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Alien Invasion')
clock = pygame.time.Clock()


SKY_COLOR = (0, 255, 255)
SUN_COLOR = (255, 255, 0)
SUN_RADIUS = 150
SUN_POSITION = (WIDTH, 0)
GRASS_HEIGHT = 100
GRASS_TOP = HEIGHT - GRASS_HEIGHT
GRASS_RECTANGLE = pygame.Rect(0, GRASS_TOP, WIDTH, GRASS_HEIGHT)
GRASS_COLOR = (0, 128, 0)


@dataclass
class UFO:
    x: int
    y: int
    width: int = 100
    height: int = 30
    color: tuple = (128, 128, 128)
    speed: int = 1

    def draw(self):
        pygame.draw.ellipse(
            screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))
        pygame.draw.ellipse(
            screen, self.color,
            pygame.Rect(self.x + self.width//4, self.y-self.height//3, self.width//2, self.height))

    def move(self):
        self.x += self.speed
        if self.x > WIDTH:
            self.x = -self.width


ufos = [
    UFO(x=0, y=50, speed=0.5),
    UFO(x=200, y=100, width=80, height=20),
    UFO(x=400, y=150, width=120, speed=2),
    UFO(x=600, y=200, speed=1.5),
    UFO(x=300, y=250, width=90, height=25, speed=4),
    UFO(x=500, y=300, width=110, height=35, speed=2.5),
    UFO(x=700, y=350, width=600, height=150, speed=3),]


def draw_scene():
    screen.fill(SKY_COLOR)  # Cyan background
    pygame.draw.circle(screen, SUN_COLOR, SUN_POSITION, SUN_RADIUS)  # Sun
    pygame.draw.rect(screen, GRASS_COLOR, GRASS_RECTANGLE)  # Grass
    for ufo in ufos:
        ufo.draw()
        ufo.move()
        clock.tick(1000)
    pygame.display.flip()  # Put the drawing on the screen


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            raise SystemExit
    draw_scene()
