import sys
import copy
sys.path.append('..')
from Clairvoyant.AI import AI
import random
import pygame
from Rule import Rule
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
    clock.tick(FPS)
    screen.fill(Color(0,0,0))
    screen.blit(rule.get_board().draw(screen_size[1]-(2*space)), (space, space))
    pygame.display.update()

def exit_listener():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

def event_listener():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if rule.get_player() == 1 and player_type[0] == 'p' and event.type == KEYDOWN:
            if event.key == K_w:
                rule.change_changing(0,1,-1)
            elif event.key == K_s:
                rule.change_changing(0,1,1)
            elif event.key == K_a:
                rule.change_changing(0,0,-1)
            elif event.key == K_d:
                rule.change_changing(0,0,1)
            if event.key == K_SPACE:
                rule.player_play_piece(rule.get_player())
        elif rule.get_player() == -1 and player_type[1] == 'p' and event.type == KEYDOWN:
            if event.key == K_UP:
                rule.change_changing(1,1,-1)
            elif event.key == K_DOWN:
                rule.change_changing(1,1,1)
            elif event.key == K_LEFT:
                rule.change_changing(1,0,-1)
            elif event.key == K_RIGHT:
                rule.change_changing(1,0,1)
            if event.key == K_RETURN:
                rule.player_play_piece(rule.get_player())

def main():
    while True:
        while rule.main() == 0:
            if gamemod == 0 or gamemod == 1 or show_process:
                event_listener()
                draw()
            if gamemod == 1 or gamemod == 2:
                #print ai.simulation(rule.get_board(),rule.get_player(),rule.get_player_move())
                if player_type[int((-0.5*rule.get_player())+0.5)] == 'c':
                    rule.c_decision(ai.make_decision(copy.deepcopy(rule.get_board()),copy.deepcopy(rule.get_player()),copy.deepcopy(rule.get_player_move())))
            #print '******'
            #print "check" + str(rule.get_board().get_board())
        print "Winner is "+str(rule.get_board().check_win())
        if gamemod == 2:
            rule.start_new_game(None,None,None)
        else:
            restart_input = raw_input("Again?(y/n)")
            if restart_input == "y":
                print "Restarting!"
                rule.start_new_game(None,None,None)
            elif restart_input == "n":
                print "Fine"
                pygame.quit()
                sys.exit()

board_size = 19
win_length = 6
first_player = 1
piece_pre_player = 2
first_player_piece = 1
sim_num = 50
player_type = ['p','p']
show_process = True
gamemod = None

if gamemod == None:
    gamemod_info = ("0:PVP","1:PVC","2:CVC")
    info = ""
    for txt in gamemod_info:
        info += txt + "\n"
    gamemod = select_index((0,len(gamemod_info)-1),info)
if gamemod == 0 or gamemod == 1 or show_process:
    screen_width = 1000
    screen_height = 1000
    space = 30
    FPS = 30
    screen_size = (screen_width,screen_height)
    pygame.init()
    screen = pygame.display.set_mode(screen_size, 0, 32)
    pygame.display.set_caption("Connect6")
    clock = pygame.time.Clock()
if gamemod == 1:
    player_type[1] = 'c'
    ai = AI(Rule(None,board_size,win_length,first_player,piece_pre_player,first_player_piece,player_type),sim_num)
elif gamemod == 2:
    player_type = ['c','c']
    ai = AI(Rule(None,board_size,win_length,first_player,piece_pre_player,first_player_piece,player_type),sim_num)
rule = Rule(None,board_size,win_length,first_player,piece_pre_player,first_player_piece,player_type)
main()
