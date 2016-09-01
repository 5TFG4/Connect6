from Board import Board
import sys
import pygame
from pygame.locals import *

def select_index(info):
    correct_input = False
    while correct_input == False:
        try:
            input_idx = int(input(info))
            correct_input = True
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
    global player,board,changing,player_move
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if player == 1 and event.type == KEYDOWN:
            pressed_keys = pygame.key.get_pressed()
            if event.key == K_w:
                changing[0][1] -= 1
            elif event.key == K_s:
                changing[0][1] += 1
            elif event.key == K_a:
                changing[0][0] -= 1
            elif event.key == K_d:
                changing[0][0] += 1
            if event.key == K_SPACE and player == 1:
                changing = board.selecting(changing)
                if board.play_piece(1):
                    player_move += 1
                    player_switch()
        elif player == -1 and event.type == KEYDOWN:
            if event.key == K_UP:
                changing[1][1] -= 1
            elif event.key == K_DOWN:
                changing[1][1] += 1
            elif event.key == K_LEFT:
                changing[1][0] -= 1
            elif event.key == K_RIGHT:
                changing[1][0] += 1
            if event.key == K_RETURN and player == -1:
                changing = board.selecting(changing)
                if board.play_piece(-1):
                    player_move += 1
                    player_switch()

def player_switch():
    global player_move,player
    if player_move >= piece_pre_player:
        player_move = 0
        player = -player
    print "Moves: " + str(piece_pre_player - player_move)


def main():
    global board
    while board.check_win() == 0:
        event_listener()
        draw()
    print "Winner is "+str(board.check_win())
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
    main()


if __name__ == "__main__":
    board_size = 19
    screen_width = 1000
    screen_height = 1000
    win_length = 6
    first_player = 1
    space = 30
    FPS = 30
    piece_pre_player = 2
    first_player_piece = 1
    screen_size = (screen_width,screen_height)
    pygame.init()
    screen = pygame.display.set_mode(screen_size, 0, 32)
    pygame.display.set_caption("Connect6")
    start_new_game()
