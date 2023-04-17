import pygame
from random import randint
pygame.init()

fx = pygame.mixer.Sound(r"assets/mp3/blip.mp3")
fx.set_volume(0.5)
f = r"assets/students/"
students = [[f"{f}a1.png", f"{f}a2.png", f"{f}a3.png"],
            [f"{f}b1.png", f"{f}b2.png", f"{f}b3.png"],
            [f"{f}c1.png", f"{f}c2.png", f"{f}c3.png"],
            [f"{f}j1.png", f"{f}j2.png", f"{f}j3.png"],
            [f"{f}k1.png", f"{f}k2.png", f"{f}k3.png"]]

class Student(pygame.sprite.Sprite):
    def __init__(self, x, y, id, a, b):
        # all necessary properties
        super().__init__()
        self.status = 'awake'
        self.id = id
        self.i = randint(0, len(students)-1) # we get ranom sprite from list
        self.image = pygame.image.load(students[self.i][0])
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.x = x
        self.y = y
        self.w = 32
        self.h = 32

        self.a = a
        self.b = b
        self.energy_speed = randint(self.a, self.b) # each student has random speed of energy drain
        self.energy = 125 # max energy
        self.next_time = pygame.time.get_ticks()
        
    
    def energy_drain(self):
        current_time = pygame.time.get_ticks()
        if current_time > self.next_time and self.energy > 0:
            self.next_time += self.energy_speed
            self.energy -= 25 # everyone looses 25 energy according to energy_speed
        
        if self.energy > 50: # changes student's sprite and status according to how many energy left
            self.set_awake()
            self.status = 'awake'
        elif self.energy > 0:
            self.set_half_sleepy()
            self.status = 'half_sleepy'
        else:
            self.set_asleep()
            self.status = 'asleep'

    def click_event(self, m_x, m_y):
        # reset student's energy when clicked at 'asleep' status. make sure user clicked on top of sprite
        if (m_x <= (self.x + self.w) and m_y <= (self.y + self.h) and m_x >= (self.x - self.w) and m_y >= (self.y - self.h)) and self.status == 'asleep':
            self.energy = 125
            fx.play()
        
        
    def get_status(self):
        return self.status
    def get_id(self):
        return self.id
    
    # for userevent
    def change_speed(self):
        if self.a > 0 and self.b > 0:
            self.a -= 3000
            self.b -= 3000
        self.energy_speed = randint(self.a, self.b)
    
    def set_awake(self):
        self.image = pygame.image.load(students[self.i][0]) # [0] - awake, [1] - half-sleepy, [2] - asleep
    
    def set_half_sleepy(self):
        self.image = pygame.image.load(students[self.i][1])
    
    def set_asleep(self):
        self.image = pygame.image.load(students[self.i][2])