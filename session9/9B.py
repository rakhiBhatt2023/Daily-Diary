"""
   1.Think of an object
    Song : name,artists,album, duration

    Song is an object
    name,artists, album, duration are attributes or variables inside an object

"""
# 2. Create its class
class song:
    def init(self):
         print('constructor executed')
         print('self:', self, type(self), id(self)) 


# creation of object
# Johns song is not an object. It is a reference variable(STACK AREA)
# It will hold hashcode of the object in the memory.
# Song() is creating an object in RAM(Heap area)
johns_song = song()
print('johns_song:',johns_song, type(johns_song), id(johns_song))
print(vars(johns_song))


# Write data in object
# name, Artists, album, duration
johns_song.name = 'Laal Pari'
johns_song.artists = 'Yo yo Honey Singh, Simar kaur, Afl'
johns_song.album= 'Top 50'
johns_song.durattion = '4.16'