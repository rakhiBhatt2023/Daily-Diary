# this is the driver file for both 11A and 11B

from seesion11A import Song
from session11B import Playlist

song1 = Song(
                track='1. Laal Pari', 
                artists='john, jennie', 
                album='Album1', 
                duration=4.5
            )

song2 = Song(track='2. Zamaana Lage', artists='harry, jennie',album='Album1',duration=3.5)
song3 = Song(
                track='3. Chor Bazaari', 
                artists='george, ben', 
                album='Album2', 
                duration=6.2
            )

# print('[main] song1:', song)
songs_play_list = Playlist()

songs_play_list.add(song=song1)
songs_play_list.add(song=song2)
songs_play_list.add(song=song3)


songs_play_list.iterat()

