<<<<<<< HEAD
from Board import Board
import random

class Rule:
    def __init__(self,board,board_size,win_length,first_player,piece_pre_player,first_player_piece,player_type):
        self.player_type = player_type
        self.first_player = first_player
        self.player = self.first_player
        self.piece_pre_player = piece_pre_player
        self.first_player_piece = first_player_piece
        self.player_move = self.piece_pre_player-self.first_player_piece
        self.changing = [[0,0],[0,0]]
        self.c_last_move = None
        self.c_play_loc = None
        self.p_play_loc = None
        self.board_size = board_size
        self.win_length = win_length
        if board == None:
            print "None"
            self.board = Board(self.board_size,self.win_length)
        else:
            print "NOOOOOOOOOOOOOOOO"
            self.board = board
        self.save = []

    def save(self):
        self.save = []



    def change_changing(self,idx,jdx,value):
        self.changing[idx][jdx] += value

    def player_play_piece(self,player):
        if self.board.play_piece(player):
            self.player_move += 1
            self.player_switch()

    def player_switch(self):
        if self.player_move >= self.piece_pre_player:
            self.player_move = 0
            self.player = -self.player

    def c_decision(self,playernum):
        if self.c_play_loc != None and self.board.c_selecting(playernum,self.c_play_loc):
            self.c_last_move = self.c_play_loc
            self.c_play_loc = None
            return True
        return False

    def change_c_play_loc(self,loc):
        self.c_play_loc = loc

    def c_main(self,playernum):
        #print self.c_decision(playernum)
        #self.change_c_play_loc([random.randint(0,self.board_size-1),random.randint(0,self.board_size-1)])
        if self.c_decision(playernum):
            self.player_play_piece(playernum)
            self.player_switch()

    def p_main(self,playernum):
        self.changing = self.board.p_selecting(self.changing)
        self.player_switch()

    def main(self):
        if self.player_type[int((-0.5*self.player)+0.5)] == 'p':
            self.p_main(self.player)
        elif self.player_type[int((-0.5*self.player)+0.5)] == 'c':
            self.c_main(self.player)
        return self.board.check_win()

    def get_player(self):
        return self.player

    def get_player_move(self):
        return self.player_move

    def get_c_last_move(self):
        return self.c_last_move

    def get_board_size(self):
        return self.board_size

    def get_board(self):
        return self.board

    def start_new_game(self,board,player,player_move):
        if player != None:
            self.player = player
        else:
            self.player = self.first_player
        if player_move != None:
            self.player_move = player_move
        else:
            self.player_move = self.piece_pre_player-self.first_player_piece
        if board != None:
            self.board = board
        else:
            self.board = Board(self.board_size,self.win_length)
        self.changing = [[0,0],[0,0]]
        self.c_play_loc = None
=======
from Board import Board
import random

class Rule:
    def __init__(self,board,board_size,win_length,first_player,piece_pre_player,first_player_piece,player_type):
        self.player_type = player_type
        self.first_player = first_player
        self.player = self.first_player
        self.piece_pre_player = piece_pre_player
        self.first_player_piece = first_player_piece
        self.player_move = self.piece_pre_player-self.first_player_piece
        self.changing = [[0,0],[0,0]]
        self.c_last_move = None
        self.c_play_loc = None
        self.p_play_loc = None
        self.board_size = board_size
        self.win_length = win_length
        if board == None:
            self.board = Board(self.board_size,self.win_length)
        else:
            self.board = board


    def change_changing(self,idx,jdx,value):
        self.changing[idx][jdx] += value

    def player_play_piece(self,player):
        if self.board.play_piece(player):
            self.player_move += 1
            self.player_switch()

    def player_switch(self):
        if self.player_move >= self.piece_pre_player:
            self.player_move = 0
            self.player = -self.player

    def c_decision(self,playernum):
        if self.c_play_loc != None and self.board.c_selecting(playernum,self.c_play_loc):
            self.c_last_move = self.c_play_loc
            self.c_play_loc = None
            return True
        return False

    def change_c_play_loc(self,loc):
        self.c_play_loc = loc
        self.c_last_move = None

    def c_main(self,playernum):
        #print self.c_decision(playernum)
        #self.change_c_play_loc([random.randint(0,self.board_size-1),random.randint(0,self.board_size-1)])
        if self.c_decision(playernum):
            self.player_play_piece(playernum)
            self.player_switch()

    def p_main(self,playernum):
        self.changing = self.board.p_selecting(self.changing)
        self.player_switch()

    def mian(self):
        if self.player_type[int((-0.5*self.player)+0.5)] == 'p':
            self.p_main(self.player)
        elif self.player_type[int((-0.5*self.player)+0.5)] == 'c':
            self.c_main(self.player)
        return self.board.check_win()

    def get_player(self):
        return self.player

    def get_player_move(self):
        return self.player_move

    def get_c_last_move(self):
        return self.c_last_move

    def get_board_size(self):
        return self.board_size

    def get_board(self):
        return self.board

    def start_new_game(self,board,player,player_move):
        if player != None:
            self.player = player
        else:
            self.player = self.first_player
        if player_move != None:
            self.player_move = player_move
        else:
            self.player_move = self.piece_pre_player-self.first_player_piece
        if board != None:
            self.board = board
        else:
            self.board = Board(self.board_size,self.win_length)
        self.changing = [[0,0],[0,0]]
        self.c_play_loc = None
>>>>>>> origin/master
