import pygame
import os
pygame.init()

W, H = 600, 200
WHITE = (255, 255, 255)
sc = pygame.display.set_mode((W, H), pygame.RESIZABLE)
pygame.display.set_caption('music player')
next = pygame.image.load('Lab_7\\next_song.jpg')
prev = pygame.image.load('Lab_7\\prevsong.jpg')
pause = pygame.image.load('Lab_7\pause_icon.jpg')
play = pygame.image.load('Lab_7\play_icon.jpg')


music_dir = "Lab_7"
music_files = [f for f in os.listdir(music_dir) if f.endswith(".mp3")]
current_track = 0

pygame.mixer.music.load(os.path.join(music_dir, music_files[current_track]))

def play_current_track():
    global current_track
    current_track = current_track % len(music_files)
    pygame.mixer.music.load(os.path.join(music_dir, music_files[current_track]))
    pygame.mixer.music.play()

def play_next_track():
    global current_track
    current_track = (current_track + 1) % len(music_files)
    pygame.mixer.music.load(os.path.join(music_dir, music_files[current_track]))
    pygame.mixer.music.play()

def play_previous_track():
    global current_track
    current_track = (current_track - 1) % len(music_files)
    pygame.mixer.music.load(os.path.join(music_dir, music_files[current_track]))
    pygame.mixer.music.play()

flpaused = flright = flleft = action = False

play_current_track()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if flpaused:
                    pygame.mixer.music.unpause()
                    flpaused = False
                    action = False 
                else:
                    pygame.mixer.music.pause()
                    flpaused = True
                    action = True
                    
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                play_next_track()
            
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                play_previous_track()


    NEW_WIDTH = pygame.display.get_window_size()[0]
    NEW_HEIGHT = pygame.display.get_window_size()[1]

    next_rect = next.get_rect(center= (NEW_WIDTH// 1.5, NEW_HEIGHT//2))
    prev_rect = prev.get_rect(center= (NEW_WIDTH// 3.5 , NEW_HEIGHT//2))
    pause_rect = pause.get_rect(center= (NEW_WIDTH//2 - 10, NEW_HEIGHT//2))
    play_rect = play.get_rect(center= (NEW_WIDTH//2 - 7, NEW_HEIGHT//2))

    sc.fill(WHITE)
    sc.blit(next, next_rect)
    sc.blit(prev, prev_rect)
    if action:
        sc.blit(play, play_rect)
        
    else:
        sc.blit(pause, pause_rect)
    pygame.display.flip()