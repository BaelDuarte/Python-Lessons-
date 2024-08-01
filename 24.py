import pygame
pygame.mixer.init()
start_program = input('welcome to ultimate metal pipe sound effect reproducer, want to start? (y/n): ')
if start_program == 'y':
    print('loading the sound...')
    pygame.mixer.music.load('Metal pipe.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()
elif start_program == 'n':
    print('ok, shutting down the program...')
else:
    print('invalid format, shutting down the program...')