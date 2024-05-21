from linked_list_class import *
import pygame
import time

WIDTH, HEIGHT = 950, 830

def change_track(current_track_index):
    '''This function will retrieve the required track information from the node'''
    current_node = music_library.get(current_track_index)
    track_image = pygame.image.load(current_node.image_location)
    screen.blit(track_image, (WIDTH / 2 - 200, HEIGHT / 2 - 200))
    pygame.display.flip()
    track_sound = pygame.mixer.Sound(current_node.music_location)
    track_sound.play()
    return track_sound, current_node.track_length

def stop_track():
    pygame.mixer.stop()

# Initial linked list nodes for test purposes
music_library = Doublylinkedlist('The Hopeless', 'Love song', 'track_images/hopeless.jpg', 'music_tracks/hopeless.wav', 11)
music_library.append('The shovel knights', 'shovel rock', 'track_images/shovel_rockers.jpg', 'music_tracks/shovel_rockers.wav', 8)
music_library.append('Shorties', 'Im small but you are tall', 'track_images/small_tall.jpg', 'music_tracks/small_tall.wav', 7)

# Pygame setup 
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Music Player')
player_background_image = pygame.image.load('track_images/player_image.jpg')
screen.blit(player_background_image, (0, 0))
pygame.display.flip()

# Pygame audio mixer setup 
pygame.mixer.init(44100, -16, 2, 2048)
pygame.mixer.set_num_channels(2)

current_track_index = 0
current_track, current_track_length = change_track(current_track_index)


main_loop = True
while main_loop:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main_loop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                stop_track()

   

    

pygame.quit()
