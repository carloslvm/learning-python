#!/usr/bin/python3

def make_album(artist_name, album_title):
    album = {artist_name.title():album_title.title()}
    return album

make_album('chill carrier', 'sundays')
make_album('pod', 'testify')
make_album('stefano targa', 'bushido')

music_album1 = make_album('chill carrier', 'sundays')
music_album2 = make_album('pod', 'testify')
music_album3 = make_album('stefano targa', 'bushido')

print(music_album1)
print(music_album2)
print(music_album3)
