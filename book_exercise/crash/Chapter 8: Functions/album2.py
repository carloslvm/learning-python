#!/usr/bin/python3

def make_album(artist_name, album_title, tracks=''):
    album = {artist_name.title():album_title.title()}
    if tracks:
        album['Tracks'] = tracks
    return album

music1 = make_album('pod', 'testify')
music2 = make_album('stefano targa','bushido', 10)
music3 = make_album('chill carrier', 'sundays', 11)
print(music2)
print(music1)
print(music3)
