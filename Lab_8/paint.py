import pygame
from pygame.locals import *

#r for rectangle
#c for circle
#e for eraser
#стрелки вверх\вниз смена цвета
class SceneBase:
    def __init__(self):
        self.next = self
    
    def ProcessInput(self, events, pressed_keys):
        print("uh-oh, you didn't override this in the child class")

    def Update(self):
        print("uh-oh, you didn't override this in the child class")

    def Render(self, screen):
        print("uh-oh, you didn't override this in the child class")

    def SwitchToScene(self, next_scene):
        self.next = next_scene
    
    def Terminate(self):
        self.SwitchToScene(None)

class GameScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        self.drawing = False
        self.shapes = []
        self.current_shape = None
        self.current_color = (0, 0, 0)  # Default color is black

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    # Switch to rectangle drawing mode
                    self.current_shape = 'rectangle'
                elif event.key == pygame.K_c:
                    # Switch to circle drawing mode
                    self.current_shape = 'circle'
                elif event.key == pygame.K_e:
                    # Switch to eraser mode
                    self.current_shape = 'eraser'
                elif event.key == pygame.K_SPACE:
                    # Clear the screen
                    self.shapes = []
                elif event.key == pygame.K_UP:
                    # Cycle through colors (forwards)
                    self.current_color = (self.current_color[0] + 50) % 256, \
                                         (self.current_color[1] + 50) % 256, \
                                         (self.current_color[2] + 50) % 256
                elif event.key == pygame.K_DOWN:
                    # Cycle through colors (backwards)
                    self.current_color = (self.current_color[0] - 50) % 256, \
                                         (self.current_color[1] - 50) % 256, \
                                         (self.current_color[2] - 50) % 256
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    self.drawing = True
                    if self.current_shape == 'rectangle':
                        start_pos = event.pos
                        self.shapes.append({'type': 'rectangle', 'start': start_pos, 'end': start_pos, 'color': self.current_color})
                    elif self.current_shape == 'circle':
                        start_pos = event.pos
                        self.shapes.append({'type': 'circle', 'start': start_pos, 'end': start_pos, 'color': self.current_color})
                elif event.button == 3:  # Right mouse button
                    self.drawing = True
                    if self.current_shape == 'eraser':
                        start_pos = event.pos
                        self.shapes.append({'type': 'eraser', 'start': start_pos, 'end': start_pos})
            elif event.type == pygame.MOUSEMOTION:
                if self.drawing:
                    if self.current_shape == 'rectangle' or self.current_shape == 'circle':
                        self.shapes[-1]['end'] = event.pos
                    elif self.current_shape == 'eraser':
                        self.shapes.append({'type': 'eraser', 'start': event.pos, 'end': event.pos})
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 or event.button == 3:  # Left or Right mouse button
                    self.drawing = False

    def Update(self):
        pass
    
    def Render(self, screen):
        screen.fill((255, 255, 255))  # Fill screen with white background
        
        for shape in self.shapes:
            if shape['type'] == 'rectangle':
                pygame.draw.rect(screen, shape['color'], pygame.Rect(shape['start'], (shape['end'][0] - shape['start'][0], shape['end'][1] - shape['start'][1])))
            elif shape['type'] == 'circle':
                radius = max(abs(shape['end'][0] - shape['start'][0]), abs(shape['end'][1] - shape['start'][1]))
                pygame.draw.circle(screen, shape['color'], shape['start'], radius, 1)
            elif shape['type'] == 'eraser':
                pygame.draw.circle(screen, (255, 255, 255), shape['start'], 10)  # White circle as eraser
                
        pygame.display.flip()

def run_game(width, height, fps, starting_scene):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    active_scene = starting_scene

    while active_scene != None:
        pressed_keys = pygame.key.get_pressed()
        
        # Event filtering
        filtered_events = []
        for event in pygame.event.get():
            quit_attempt = False
            if event.type == pygame.QUIT:
                quit_attempt = True
            elif event.type == pygame.KEYDOWN:
                alt_pressed = pressed_keys[pygame.K_LALT] or \
                              pressed_keys[pygame.K_RALT]
                if event.key == pygame.K_ESCAPE:
                    quit_attempt = True
                elif event.key == pygame.K_F4 and alt_pressed:
                    quit_attempt = True
            
            if quit_attempt:
                active_scene.Terminate()
            else:
                filtered_events.append(event)
        
        active_scene.ProcessInput(filtered_events, pressed_keys)
        active_scene.Update()
        active_scene.Render(screen)
        
        active_scene = active_scene.next
        
        pygame.display.flip()
        clock.tick(fps)

run_game(400, 300, 60, GameScene())
