class board:
    def __init__(self,size,win_length):
        self.size = size
        self.win_length = win_length
        self.contain = [[0 for idx in xrange(self.size)] for jdx in xrange(self.size)]

    def play_piece(self,loc,player):
        if self.contain[loc[1]][loc[0]] == 0:
            self.contain[loc[1]][loc[0]] = player
            return True
        else:
            return False

    def check_board(self):
        sum_list = [sum(self.contain[y][x:x+self.win_length]) for y in xrange(self.size) for x in xrange(self.size-self.win_length+1) if self.contain[y][x] != 0]
        sum_list += [sum([self.contain[y+idx][x] for idx in xrange(self.win_length)]) for y in xrange(self.size-self.win_length+1) for x in xrange(self.size) if self.contain[y][x] != 0]
        sum_list += [sum([self.contain[y+idx][x+idx] for idx in xrange(self.win_length)]) for y in xrange(self.size-self.win_length+1) for x in xrange(self.size-self.win_length+1) if self.contain[y][x] != 0]
        sum_list += [sum([self.contain[y+idx][x-idx] for idx in xrange(self.win_length)]) for y in xrange(self.size-self.win_length+1) for x in xrange(self.win_length-1,self.size) if self.contain[y][x] != 0]
        print "sum_list" + str(sum_list)
        if self.win_length in sum_list:
            return 1
        elif -self.win_length in sum_list:
            return -1
        else:
            return 0

    def draw(self,screen,loc):
        pass

    def print_board(self):
        for idx in xrange(self.size):
            print self.contain[idx]
