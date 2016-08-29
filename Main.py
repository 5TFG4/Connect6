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
    global screen,player,board,clock,FPS,changing
    time_passed = clock.tick(FPS)
    changing = board.selecting(changing)
    screen.fill(Color(0,0,0))
    screen.blit(board.draw(screen_size[1]-(2*space)), (space, space))
    pygame.display.update()

def main():
    global screen,player,board,space,x_loc,y_loc,changing
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[K_w]:
                changing[0][1] -= 1
            elif pressed_keys[K_s]:
                changing[0][1] += 1
            elif pressed_keys[K_a]:
                changing[0][0] -= 1
            elif pressed_keys[K_d]:
                changing[0][0] += 1
            if pressed_keys[K_SPACE] and player == 1:
                changing = board.selecting(changing)
                if board.play_piece(1):
                    player = -player
            if pressed_keys[K_UP]:
                changing[1][1] -= 1
            elif pressed_keys[K_DOWN]:
                changing[1][1] += 1
            elif pressed_keys[K_LEFT]:
                changing[1][0] -= 1
            elif pressed_keys[K_RIGHT]:
                changing[1][0] += 1
            if pressed_keys[K_RETURN] and player == -1:
                changing = board.selecting(changing)
                if board.play_piece(-1):
                    player = -player
                #if event.key == K_enter and player == -1:
                #    changing = board.selecting(changing)
                #    if board.play_piece(-1):
                #        player = -player

#        while board.play_piece([x_loc,y_loc],player) == False:
#            x_loc = select_index("x location")
#            y_loc = select_index("y location")
        #print "winner" + str(board.check_board())
#        player = -player
        #print "\n"
#        time_passed += clock.tick()
#        if
        draw()


if __name__ == "__main__":
    board_size = 19
    screen_width = 640
    win_length = 3
    player = 1
    space = 30
    FPS = 30
    screen_size = (screen_width,screen_width)
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(screen_size, 0, 32)
    pygame.display.set_caption("Connect6")
    board = board(board_size,win_length)
    board.print_board()
    changing = [[0,0],[0,0]]
    x_loc = 0
    y_loc = 0
    #x_loc = select_index("x location")
    #y_loc = select_index("y location")
    main()
