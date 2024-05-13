from linked_list_class import *


'''The functionality of this will initally be completed in terminal.
Following this a pygame window will be added with music playing and images
following this investigations into alternative GUI will take place followed by
the addition of things such as the play bar and other elements'''

music_library  = Doublylinkedlist('the butcher', 'Sausage', 'test', 'test')
music_library.append('workers', 'desks are for men', 'test', 'test')
music_library.append('horses', 'book worms read shoes', 'test', 'test')


main_loop = True
while main_loop:
    try:
        user_input = int(input('''Please select from the list which task you wish to perform:
                            1. See all available tracks
                            2. Add a new track
                            3. Delete a track
                            4. Shuffle tracks
                                '''))
    except:
        print('Please select a valid number')
    if user_input == 1:
        music_library.print_list()
    elif user_input == 2:
        try:
            user_artist_selection = str(input('What is the name of the artist? '))
            user_track_selection = str(input('What is the name of the track? '))
            user_image_location = str(input('What is the location of the image? '))
            user_song_location = str(input('What is the location of the song? '))
        except:
            print('Please enter a valid value')
        music_library.append(user_artist_selection, user_track_selection, user_image_location, user_song_location)
    elif user_input == 3:
        try:
            music_library.print_list()
            user_delete_selection = int(input('Which track number would you like to delete from the list? '))
            music_library.remove(user_delete_selection -1)
        except:
            print('Please input a track number')
                                       
    
    




