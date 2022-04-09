import os
import random
import pygame

def Music():
    path = "E:\HEP\Music"
    file = os.path.join(path,random.choice(os.listdir(path)))
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    
    