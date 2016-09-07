from Board import Board
import sys
import random
import pygame
from pygame.locals import *

def select_index(input_range,info):
    correct_input = False
    while correct_input == False:
        try:
            input_idx = int(input(info))
            if input_idx >= input_range[0] and input_idx <= input_range[1]:
                correct_input = True
            else:
                print"Not in range, please try again"
        except:
            print"Incorrect input, only number is accepted, please try again"
            sys.exc_clear()
    return input_idx

def draw():
    global screen,player,board,clock,FPS,changing
    time_passed = clock.tick(FPS)
    changing = board.selecting(changing)
    screen.fill(Color(0,0,0))
    screen.blit(board.draw(screen_size[1]-(2*space)), (space, space))
    pygame.display.update()

def event_listener():
    global player,board,changing
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if player == 1 and player_type[0] == 'p' and event.type == KEYDOWN:
            pressed_keys = pygame.key.get_pressed()
            if event.key == K_w:
                changing[0][1] -= 1
            elif event.key == K_s:
                changing[0][1] += 1
            elif event.key == K_a:
                changing[0][0] -= 1
            elif event.key == K_d:
                changing[0][0] += 1
            if event.key == K_SPACE:
                changing = board.selecting(changing)
                player_play_piece(player)
        elif player == -1 and player_type[1] == 'p' and event.type == KEYDOWN:
            if event.key == K_UP:
                changing[1][1] -= 1
            elif event.key == K_DOWN:
                changing[1][1] += 1
            elif event.key == K_LEFT:
                changing[1][0] -= 1
            elif event.key == K_RIGHT:
                changing[1][0] += 1
            if event.key == K_RETURN:
                changing = board.selecting(changing)
                player_play_piece(player)

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

def change_c_play_loc(loc):
    global c_play_loc
    c_play_loc = loc

def c_decision(playernum):
    global c_play_loc
    if c_play_loc != None and board.c_selecting(playernum,c_play_loc):
        c_play_loc = None
        return True
    return False

def c_main(playernum):
    while player == playernum:
        change_c_play_loc([random.randint(0,board_size-1),random.randint(0,board_size-1)])
        if c_decision(playernum):
            player_play_piece(playernum)

def p_main(playernum):
    while player == playernum:
        event_listener()
        draw()


def mian():
    global board
    while True:
        num = 1
        while board.check_win() == 0:
            if player_type[int((-0.5*num) + 0.5)] == 'p':
                p_main(num)
            elif player_type[int((-0.5*num) + 0.5)] == 'c':
                c_main(num)
            num = -num
            if gamemod == 0 or gamemod == 1 or show_process == True:
                draw()
        print "Winner is "+str(board.check_win())
        if gamemod == 2:
            start_new_game()
        else:
            restart_input = raw_input("Again?(y/n)")
            if restart_input == "y":
                print "Restarting!"
                start_new_game()
            elif restart_input == "n":
                print "Fine"
                pygame.quit()
                sys.exit()


def start_new_game():
    global player_move,player,board,clock,changing
    player = first_player
    player_move = piece_pre_player-first_player_piece
    clock = pygame.time.Clock()
    board = Board(board_size,win_length)
    changing = [[0,0],[0,0]]
    c_play_loc = None


board_size = 19
win_length = 6
first_player = 1
piece_pre_player = 2
first_player_piece = 1
player_type = ['p','p']
show_process = True
gamemod = None
if gamemod == None:
    gamemod_info = ("0:PVP","1:PVC","2:CVC")
    info = ""
    for txt in gamemod_info:
        info += txt + '\n'
    gamemod = select_index((0,len(gamemod_info)-1),info)
if gamemod == 0 or gamemod == 1 or show_process == True:
    screen_width = 1000
    screen_height = 1000
    space = 30
    FPS = 30
    screen_size = (screen_width,screen_height)
    pygame.init()
    screen = pygame.display.set_mode(screen_size, 0, 32)
    pygame.display.set_caption("Connect6")
if gamemod == 1:
    player_type[1] = 'c'
elif gamemod == 2:
    player_type = ['c','c']

start_new_game()
mian()
