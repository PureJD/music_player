from linked_list_class import *
import pygame
import time

WIDTH, HEIGHT = 950,830

'''The functionality of this will initially be completed in terminal.
Following this, a pygame window will be added with music playing and images.
Following this, investigations into alternative GUI will take place followed by
the addition of things such as the play bar and other elements'''

def change_track(current_track, track_length):
    '''This function will retrieve the required track information from the node'''
    current_node = music_library.get(current_track)
    current_track = pygame.image.load(current_node.image_location)
    screen.blit(current_track, (WIDTH / 2 - 200, HEIGHT / 2 - 200))
    pygame.display.flip()
    current_track = pygame.mixer.Sound(current_node.music_location)
    current_track.play()
    time.sleep(track_length + 1)
    return True
    
    
# Initial linked list nodes for test purposes
music_library = Doublylinkedlist('The Hopeless', 'Love song', 'track_images/hopeless.jpg', 'music_tracks/hopeless.wav', 11)
music_library.append('The shovel knights', 'shovel rock', 'track_images/shovel_rockers.jpg', 'music_tracks/shovel_rockers.wav', 8)
music_library.append('Shorties', 'Im small but you are tall', 'track_images/small_tall.jpg', 'music_tracks/small_tall.wav', 7)

#pygame setup 
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Music Player')
player_background_image = pygame.image.load('track_images/player_image.jpg')
screen.blit(player_background_image, (0, 0))
pygame.display.flip()

#pygame audio mixer setup 
pygame.mixer.init()
pygame.mixer.init(44100, -16, 2, 2048)
pygame.mixer.set_num_channels(2)



current_track = 0
current_node = music_library.get(current_track)



main_loop = True
while main_loop:
    
    

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main_loop = False
    
    #test code for chaing track image   CURRENTLY BROKEN. FIX REQUIRED
    time.sleep(3)
    change_track(current_track, current_node.track_length)
    
    current_track += 1
    change_track(current_track, current_node.track_length)
   
    current_track += 1
    change_track(current_track, current_node.track_length)
  
    
    

    # Displaying terminal-based input menu and handling user input
    try:
        user_input = int(input('''Please select from the list which task you wish to perform:
                            1. See all available tracks
                            2. Add a new track
                            3. Delete a track
                            4. Shuffle tracks
                                '''))
    except ValueError:
        print('Please select a valid number')
        continue

    if user_input == 1:
        music_library.print_list()
    elif user_input == 2:
        try:  # In a real system this data would be read from the audio files opened in the player, not input by the user
            user_artist_selection = str(input('What is the name of the artist? '))
            user_track_selection = str(input('What is the name of the track? '))
            user_image_location = str(input('What is the location of the image? '))
            user_song_location = str(input('What is the location of the song? '))
            user_input_track_length = int(input('How long is the track? '))
        except ValueError:
            print('Please enter a valid value')
            continue
        music_library.append(user_artist_selection, user_track_selection, user_image_location, user_song_location, user_input_track_length)
    elif user_input == 3:
        try:
            music_library.print_list()
            user_delete_selection = int(input('Which track number would you like to delete from the list? '))
            music_library.remove(user_delete_selection - 1)
        except ValueError:
            print('Please input a track number')
    elif user_input == 4:
        try:
            music_library.shuffle()
        except ValueError:
            print('Error attempting to shuffle tracks. Minimum 2 tracks required to shuffle')

    pygame.display.flip()

pygame.quit()
