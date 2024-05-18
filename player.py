from linked_list_class import *
import pygame

'''The functionality of this will initially be completed in terminal.
Following this, a pygame window will be added with music playing and images.
Following this, investigations into alternative GUI will take place followed by
the addition of things such as the play bar and other elements'''

# Initial linked list nodes for test purposes
music_library = Doublylinkedlist('the butcher', 'Sausage', 'test', 'test', 100)
music_library.append('workers', 'desks are for men', 'test', 'test', 100)
music_library.append('horses', 'book worms read shoes', 'test', 'test', 100)

#pygame setup 
pygame.init()
WIDTH, HEIGHT = 950,830
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Music Player')
player_background_image = pygame.image.load('track_images/player_image.jpg')
screen.blit(player_background_image, (0, 0))
pygame.display.flip()


main_loop = True
while main_loop:
    

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main_loop = False

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
