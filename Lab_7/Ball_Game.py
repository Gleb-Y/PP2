import pygame
pygame.init()

WIDTH, HEIGHT = 600, 400
COLOUR_WHITE = (255, 255, 255)
COLOUR_RED = (255, 0, 0)
SPEED = 20
BALL_RADIUS = 25
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Ball Game")
clock = pygame.time.Clock()
FPS = 60

x_coordinate = WIDTH/2 
y_coordinate = HEIGHT/2 

fldown = flleft = flup = flright = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                flleft = True
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                flright = True
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                fldown = True
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                flup = True
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_a, pygame.K_d]:
                flleft = flright = False
            elif event.key in [pygame.K_DOWN, pygame.K_UP, pygame.K_w, pygame.K_s]:
                flup = fldown = False

    NEW_WIDTH = pygame.display.get_window_size()[0]
    NEW_HEIGHT = pygame.display.get_window_size()[1]

    if flleft and x_coordinate >= 0 + BALL_RADIUS:
        x_coordinate -= SPEED
    elif flright and x_coordinate <= NEW_WIDTH - BALL_RADIUS:
        x_coordinate += SPEED
    if fldown and y_coordinate <= NEW_HEIGHT - BALL_RADIUS:
        y_coordinate += SPEED
    elif flup and y_coordinate >= 0 + BALL_RADIUS:
        y_coordinate -= SPEED

    screen.fill(COLOUR_WHITE)
    pygame.draw.circle(screen, COLOUR_RED, (x_coordinate, y_coordinate), BALL_RADIUS)
    pygame.display.update()

    clock.tick(FPS)