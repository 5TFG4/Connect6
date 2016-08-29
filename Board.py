import pygame,pygame.gfxdraw
from pygame.locals import *

class board:
    def __init__(self,size,win_length):
        self.background = Color(26,153,0)
        self.line_width = 3
        self.box_width = 5
        self.size = size
        self.win_length = win_length
        self.contain = [[0 for idx in xrange(self.size)] for jdx in xrange(self.size)]
        self.selected_list = [(0,0),(1,0)]
        self.surface_size = None
        self.piece_size = None
        self.gap = None
        self.surface = None

    def play_piece(self,player):
        if player == 1:
            selected = self.selected_list[0]
        elif player == -1:
            selected = self.selected_list[1]
        if self.contain[selected[1]][selected[0]] == 0:
            self.contain[selected[1]][selected[0]] = player
            return True
        else:
            return False

    def selecting(self,changing):
        self.selected_list = [[self.selected_list[0][0]+changing[0][0],self.selected_list[0][1]+changing[0][1]],
        [self.selected_list[1][0]+changing[1][0],self.selected_list[1][1]+changing[1][1]]]
        for idx in xrange(len(self.selected_list)):
            for jdx in xrange(len(self.selected_list[idx])):
                if self.selected_list[idx][jdx] < 0:
                    self.selected_list[idx][jdx] = 0
                elif self.selected_list[idx][jdx] > self.size-1:
                    self.selected_list[idx][jdx] = self.size-1
        return [[0,0],[0,0]]


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

    def draw(self,surface_size):
        if self.surface == None or self.surface != surface_size:
            self.surface_size = surface_size
            self.surface = pygame.Surface((self.surface_size, self.surface_size))
            self.piece_size = int(self.surface_size/(2.0*self.size))-2
            self.gap = (self.surface_size-(2.0*self.piece_size))/(self.size-1)
        self.surface.fill(self.background)
        for idx in xrange(self.size+1):
            pygame.draw.aaline(self.surface, Color(0,0,0), (self.piece_size + (idx*self.gap),self.piece_size), (self.piece_size + (idx*self.gap),self.surface_size - self.piece_size), self.line_width)
            pygame.draw.aaline(self.surface, Color(0,0,0), (self.piece_size,self.piece_size + (idx*self.gap)), (self.surface_size - self.piece_size,self.piece_size + (idx*self.gap)), self.line_width)
        piece_list = [(self.piece_size + (x*self.gap),self.piece_size + (y*self.gap),self.contain[x][y])for x in xrange(self.size) for y in xrange(self.size) if self.contain[x][y] != 0]
        for piece in piece_list:
            if piece[2] == 1:
                color = Color(0,0,0)
            elif piece[2] == -1:
                color = Color(255,255,255)
            pygame.gfxdraw.aacircle(self.surface, int(piece[1]), int(piece[0]), self.piece_size, color)
            pygame.gfxdraw.filled_circle(self.surface, int(piece[1]), int(piece[0]), self.piece_size, color)
        if self.selected_list[0] != self.selected_list[1]:
            for idx in xrange(len(self.selected_list)):
                pygame.draw.rect(self.surface,Color(idx*255,idx*255,idx*255),
                ((self.selected_list[idx][0]*self.gap,self.selected_list[idx][1]*self.gap),(self.piece_size*2,self.piece_size*2)),self.box_width)
        else:
            pygame.draw.rect(self.surface,Color(148,148,148),
            ((self.selected_list[0][0]*self.gap,self.selected_list[0][1]*self.gap),(self.piece_size*2,self.piece_size*2)),self.box_width)
        return self.surface

    def print_board(self):
        for idx in xrange(self.size):
            print self.contain[idx]
