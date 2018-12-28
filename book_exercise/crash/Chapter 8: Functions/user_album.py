#!/usr/bin/python3

def make_album(artist_name, album_title, tracks=''):
    album = {artist_name.title(): album_title.title()}
    if tracks:
        album['Tracks'] = int(tracks)
    return album

print("Press 'q' anytime to quit the program")

while True:
    name = input('Type the name of the artist: ')
    if name == 'q':
        break
    title = input('Type the name of the album\'s artist: ')
    if title == 'q':
       break
    print('Do you want to specify the number of tracks?')
    confirm = input('yes/no: ')
    if confirm == 'yes':
        number_tracks = int(input('Enter the number of tracks: '))
        disc = make_album(name, title,tracks=number_tracks)
        print(disc)
    elif confirm == 'no':
        disc = make_album(name, title)
        print(disc)
    elif confirm == 'q':
        active = False
