import pygame
import datetime
pygame.init()

W, H = 829, 800
WHITE = (255, 255, 255)
sc = pygame.display.set_mode((W, H), pygame.RESIZABLE)
pygame.display.set_caption('Mikey\'s Clock')
pygame.display.set_icon(pygame.image.load('Lab_7\mickeyclock.jpeg'))
body = pygame.image.load('Lab_7\main-clock.png')
r_hand = pygame.image.load('Lab_7\\right-hand.png')
l_hand = pygame.image.load('Lab_7\left-hand.png')
clock = pygame.time.Clock()

def rot_center(image, angle, w, h):
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_rect = rotated_image.get_rect(center = (w//2, h//2))
    return rotated_image, rotated_rect

flspace = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    NEW_WIDTH = pygame.display.get_window_size()[0]
    NEW_HEIGHT = pygame.display.get_window_size()[1]

    current_time = datetime.datetime.today().time()
    minutes_angle = -6 * current_time.minute + 90
    seconds_angle = -6 * current_time.second + 90
    l_hand_seconds_image, l_hand_new_rect = rot_center(l_hand, seconds_angle, NEW_WIDTH, NEW_HEIGHT)
    r_hand_minutes_image, r_hand_new_rect = rot_center(r_hand, minutes_angle, NEW_WIDTH, NEW_HEIGHT)

    body_rect = body.get_rect(center= (NEW_WIDTH//2, NEW_HEIGHT//2))
    r_hand_rect = r_hand.get_rect(center= (NEW_WIDTH//2, NEW_HEIGHT//2))
    l_hand_rect = l_hand.get_rect(center= (NEW_WIDTH//2, NEW_HEIGHT//2))

    sc.fill(WHITE)
    sc.blit(body, body_rect)
    sc.blit(r_hand_minutes_image, r_hand_new_rect)
    sc.blit(l_hand_seconds_image, l_hand_new_rect)
    pygame.display.flip()   # = update
    clock.tick(30)