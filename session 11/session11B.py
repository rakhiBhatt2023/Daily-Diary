class Playlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, song):

        self.size += 1       #     increment will be there in if and else also

        if self.head == None:          # Having only 1 song
            self.head = song
            self.tail = song

        else:
           self.tail.next = song
           song.previous = self.tail
           song.next = self.head

           self.tail = song
           self.head.previous = song

    # def iterate_forward(self):
    #     song = self.head
    #     song.show()
    #     while song.next != self.head:
    #         song = song.next
    #         song.show()

    # def iterate_backward(self):
    #     song = self.tail
    #     song.show()
    #     while song.previous != self.tail:
    #         song = song.previous
    #         song.show()
        

    def iterat(self,directoin = 0):
        if directoin == 0:
            song = self.head
            song.show()
            while song.next != self.head:
                song = song.next
                song.show()

        else:
            song = self.tail
            song.show()
            while song.previous != self.head:
                song = song.previous
                song.show()





           