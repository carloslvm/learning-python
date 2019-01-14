#!/usr/bin/python3

class Techno():
    def __init__(self, dj, song_name):
        self.dj = dj
        self.song_name = song_name

    def current_music(self):
        print("DJ: %s" % self.dj.upper())
        print("Song: %s" % self.song_name.title(), '\n')

first_set = Techno("somma & blu eyes", "drawn to you")
#print(first_set.dj)
first_set.current_music()

second_set = Techno("omnia", "cyberpunk")
#print(second_set.dj)
second_set.current_music()

third_set = Techno("antonio mareno", "we ain't ever coming down")
#print(third_set.dj)
third_set.current_music()

fourth_set = Techno("ferry corsten & saad ayub", "synchronicity")
#print(fourth_set.dj)
fourth_set.current_music()

fifth_set = Techno("sasha", "xpander")
#print(fifth_set.dj)
fifth_set.current_music()
