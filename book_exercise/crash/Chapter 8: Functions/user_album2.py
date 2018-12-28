#!/usr/bin/python3

def make_album(artist_name, album_title):
    album = {artist_name:album_title}
    return album

while True:
    print("Press 'q' anytime to quit the program.")
    name = input('Enter the name of the artist: ')
    if name == 'q':
        break
    title = input("Enter the artist's album: ")
    if title == 'q':
        break
    make_album(name, title)
    for artist, artist_album in make_album(name, title).items():
        name_artist = artist.title()
        art_album = artist_album.title()
        print('\nArtist: ' + name_artist)
        print('Album: ' + art_album + '\n')
