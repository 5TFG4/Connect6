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
        self.p_play_loc = None
        self.board_size = board_size
        self.win_length = win_length
        self.c_played = False
        if board == None:
            self.board = Board(self.board_size,self.win_length)
        else:
            self.board = board

    def get_empty_loc_list(self):
        return self.board.get_empty_loc_list()

    def get_random_loc(self,piece_win_chance_list):
        maximum = sum([sum(x_raw)for x_raw in piece_win_chance_list])
        if maximum > 0:
            cumulative_probability = 0.0
            key = random.uniform(0,maximum)
            for loc in self.board.get_empty_loc_list():
                cumulative_probability += piece_win_chance_list[1][0]
                if cumulative_probability>key:
                    return loc
        loc = random.choice(self.board.get_empty_loc_list())
        return loc

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

    def c_decision(self,loc):
        if self.c_played == False:
            self.board.c_selecting(self.player,loc)
            self.c_played = True

    def c_main(self,playernum):
        if self.c_played:
            self.player_play_piece(playernum)
            self.player_switch()
            self.c_played = False

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
