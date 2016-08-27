from Board import board
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
    global screen,player,board
    screen.fill(background)
    board.draw(screen)
    pygame.display.update()

def main():
    global screen,player,board
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        #while board.play_piece([x_loc,y_loc],player) == False:
            #x_loc = select_index("x location")
            #y_loc = select_index("y location")
        #print "winner" + str(board.check_board())
        player = -player
        #print "\n"
        draw()


if __name__ == "__main__":
    board_size = 10
    screen_width = 640
    background = (26,153,0)
    win_length = 3
    player = -1
    screen_size = (screen_width,screen_width)
    pygame.init()
    screen = pygame.display.set_mode(screen_size, 0, 32)
    pygame.display.set_caption("Connect6")
    board = board(board_size,win_length)
    board.print_board()
    main()
    #x_loc = select_index("x location")
    #y_loc = select_index("y location")
