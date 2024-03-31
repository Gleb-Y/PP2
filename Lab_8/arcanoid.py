import pygame 
import random
from pygame.locals import*
pygame.init()

W, H = 1200, 800
FPS = 60

screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()
done = False
bg = (0, 0, 0)

#paddle
paddleW = 150
paddleH = 25
paddleSpeed = 20
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)


#Ball
ballRadius = 20
ballSpeed = 5
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1

#Game score
game_score = 0
game_score_fonts = pygame.font.SysFont('comicsansms', 40)
game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))
game_score_rect = game_score_text.get_rect()
game_score_rect.center = (210, 20)

#Ingame timer
game_time_sec = 0
game_time_min = 0
game_time_fonts = pygame.font.SysFont('comicsansms', 40)
game_time_text = game_time_fonts.render(f"Time: {game_time_min}:{game_time_sec}", True, (255, 255, 255))
game_time_rect = game_time_text.get_rect()
game_time_rect.center = (1010 , 20)

#Catching sound
collision_sound = pygame.mixer.Sound('catch.mp3')

def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    if delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy


#block settings
block_list = [pygame.Rect(10 + 120 * i, 50 + 70 * j,
        100, 50) for i in range(10) for j in range (4)]
color_list = [(random.randrange(0, 255), 
    random.randrange(0, 255),  random.randrange(0, 255))
              for i in range(10) for j in range(4)] 

# Unbreakable blocks
unbreakable_block_list = []
# Generate unbreakable blocks
while len(unbreakable_block_list) < 6:  
    x = 10 + 120 * random.randint(0, 10)  # Случайное положение по оси X
    y = 50 + 70 * random.randint(0, 4)  # Случайное положение по оси Y
    new_block = pygame.Rect(x, y, 100, 50)
    # Проверяем, не перекрывается ли новый блок с другими блоками
    overlapping = False
    for block in (block_list + unbreakable_block_list):
        if new_block.colliderect(block):
            overlapping = True
            break
    if not overlapping:
        unbreakable_block_list.append(new_block)

#Game over Screen
losefont = pygame.font.SysFont('comicsansms', 40)
losetext = losefont.render('Game Over', True, (255, 255, 255))
losetextRect = losetext.get_rect()
losetextRect.center = (W // 2, H // 2)

#Win Screen
winfont = pygame.font.SysFont('comicsansms', 40)
wintext = losefont.render('You win yay', True, (0, 0, 0))
wintextRect = wintext.get_rect()
wintextRect.center = (W // 2, H // 2)

#Increase ball speed over time
INCREASE_BALL_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INCREASE_BALL_SPEED, 10000)

#Time counter
TIME_COUNT_SEC = pygame.USEREVENT + 2
pygame.time.set_timer(TIME_COUNT_SEC, 1000)
TIME_COUNT_MIN = pygame.USEREVENT + 3
pygame.time.set_timer(TIME_COUNT_MIN, 60000)

while not done:
    for event in pygame.event.get():
        if event.type == INCREASE_BALL_SPEED:
            ballSpeed += 1
        if event.type == TIME_COUNT_SEC:
            game_time_sec += 1
            if game_time_sec == 60:
                game_time_sec=0
        if event.type == TIME_COUNT_MIN:
            game_time_min += 1
        if event.type == pygame.QUIT:
            done = True

    screen.fill(bg)
    
    # drawing blocks
    [pygame.draw.rect(screen, color_list[color], block)
     for color, block in enumerate(block_list)] 
    
    # drawing unbreakable blocks
    [pygame.draw.rect(screen, pygame.Color(255, 255, 255), block)
     for block in unbreakable_block_list] 
    
    pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)
    pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius)

    #Ball movement
    ball.x += ballSpeed * dx
    ball.y += ballSpeed * dy

    #Collision left 
    if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
        dx = -dx
    #Collision top
    if ball.centery < ballRadius + 50: 
        dy = -dy
    #Collision with paddle
    if ball.colliderect(paddle) and dy > 0:
        dx, dy = detect_collision(dx, dy, ball, paddle)

    #Collision blocks
    hitIndex = ball.collidelist(block_list + unbreakable_block_list)

    if hitIndex != -1:
        hitRect = (block_list + unbreakable_block_list)[hitIndex]
        if hitRect in unbreakable_block_list:
            dx, dy = detect_collision(dx, dy, ball, hitRect)
        else:
            block_list.pop(hitIndex)
            color_list.pop(hitIndex)
            dx, dy = detect_collision(dx, dy, ball, hitRect)
            game_score += 1
            collision_sound.play()
        
        # Game score
    game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
    screen.blit(game_score_text, game_score_rect)

    # Game timer
    game_time_text = game_time_fonts.render(f"Time: {game_time_min}:{game_time_sec}", True, (255, 255, 255))
    screen.blit(game_time_text, game_time_rect)
    
    # Win/lose screens
    if ball.bottom > H:
        screen.fill((0, 0, 0))
        screen.blit(losetext, losetextRect)
    elif not len(block_list):
        screen.fill((255, 255, 255))
        screen.blit(wintext, wintextRect)
        
    # Paddle Control
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddleSpeed
    if key[pygame.K_RIGHT] and paddle.right < W:
        paddle.right += paddleSpeed

    pygame.display.flip()
    clock.tick(FPS)

