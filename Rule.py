class Rule:
    def __init__(board,board_size,win_length,first_player,piece_pre_player,first_player_piece,player_type):
        self.player_type = player_type
        self.first_player = first_player
        self.player = self.first_player
        self.piece_pre_player = piece_pre_player
        self.first_player_piece = first_player_piece
        self.player_move = self.piece_pre_player-self.first_player_piece
        self.changing = [[0,0],[0,0]]
        self.c_play_loc = None
        self.board_size = board_size
        self.win_length = win_length
        if board == None:
            self.board = Board(self.board_size,self.win_length)
        else:
            self.board = board



    def player_play_piece(player):
        global board,player_move
        if board.play_piece(player):
            player_move += 1
            player_switch()

    def player_switch():
        global player_move,player
        if player_move >= piece_pre_player:
            player_move = 0
            player = -player

    def c_decision(playernum):
        global c_play_loc
        if c_play_loc != None and board.c_selecting(playernum,c_play_loc):
            c_play_loc = None
            return True
        return False

    def change_c_play_loc(loc):
        global c_play_loc
        c_play_loc = loc

    def c_main(playernum):
        if player == playernum:
            change_c_play_loc([random.randint(0,board_size-1),random.randint(0,board_size-1)])
            if c_decision(playernum):
                player_play_piece(playernum)

    def p_main(playernum):
        if player == playernum:
            self.changing = self.board.selecting(changing)

    def mian():
        for num in xrange(len(self.player_type)):
            if self.player_type[num] == 'p':
                self.p_main((-2*num)+1)
            elif self.player_type[num] == 'c':
                self.c_main((-2*num)+1)
            if self.board.check_win() != 0:
                return self.board.check_win()
        return 0

        num = 1
        while self.board.check_win() == 0:
            if self.player_type[int((-0.5*num) + 0.5)] == 'p':
                self.p_main(num)
            elif self.player_type[int((-0.5*num) + 0.5)] == 'c':
                c_main(num)
            num = -num
            if gamemod == 0 or gamemod == 1 or show_process:
                draw()
                exit_listener()

    def get_board():
        return board


    def start_new_game():
        self.player = self.first_player
        self.player_move = self.piece_pre_player-self.first_player_piece
        self.changing = [[0,0],[0,0]]
        self.c_play_loc = None
        self.board = Board(self.board_size,self.win_length)
