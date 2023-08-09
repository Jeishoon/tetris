import pygame

from tetrominos import *
from resources import *

################################## STANDARD TETRIS ##################################

class TetrisGrid:

    current_piece = None
    scale = 30
    #constructor with x,y co-ordinates in preparation for positioning of grid in 2 player mode
    def __init__(self,height,width,x,y,screen):
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        self.field = []
        self.counter = 0
        self.fast_down = False
        self.fast_left = False
        self.fast_right = False
        self.left_counter = 0
        self.right_counter = 0
        self.fps = 60
        self.state = "playing"
        self.lines_cleared = 0
        self.lock_delay = 0
        self.screen = screen

        #generates the field on initialisation
        for i in range(height):
            new_line = []
            for j in range(width):
                new_line.append(0)
            self.field.append(new_line)

    #creating a new piece for the tetris grid
    def new_piece(self):
        self.current_piece = TetrominoClassic(3,0)

    #moving the piece down
    def move_down(self):
        self.current_piece.y += 1
        if self.overlap():
            #small delay before locking the piece
            self.lock_delay += 1
            self.current_piece.y -= 1
            #seperate case for the player pressing down
            #since the method is called more often
            if self.fast_down == False:
                if self.lock_delay >= 1:
                    self.lock()
                    self.lock_delay = 0
            else:
                if self.lock_delay >= 4:
                    self.lock()
                    self.lock_delay = 0

    #moving the piece left or right
    def move_lr(self,direction):
        self.current_piece.x += direction
        if self.overlap():
            self.current_piece.x -= direction

    #rotating the piece
    def rotate(self,angle):
        if angle == 1:
            self.current_piece.rotate_cw()
            #revert rotation if invalid
            if self.overlap():
                self.current_piece.rotate_acw()
        else:
            self.current_piece.rotate_acw()
            if self.overlap():
                self.current_piece.rotate_cw()

    #detects whether piece will overlap another if it moves further down
    def overlap(self):
        #cycles through the spaces around the currently falling piece
        for i in range(4):
            for j in range(4):
                #only checks spaces around the piece which contain the piece
                if i * 4 + j in self.current_piece.get_state():
                    #should the piece meet the conditions of:
                    # 1. meeting the floor
                    # 2. meeting the left wall
                    # 3. meeting the right wall
                    # 4. meeting another piece in some way
                    if i + self.current_piece.y > self.height - 1 or \
                        j + self.current_piece.x > self.width - 1 or \
                        j + self.current_piece.x < 0 or \
                            self.field[i +self.current_piece.y][j + self.current_piece.x] > 0:
                        # piece would overlap and so return true
                        return True
        #returns false if not
        return False

    #clears lines if a full row is detected
    def clear_lines(self):
        #keep track of number of lines cleared in a clearing for scoring purposes
        lines = 0
        #checks through all lines
        for i in range(1, self.height):
            spaces = 0
            #counts number of empty spaces on a row
            for j in range(self.width):
                if self.field[i][j] == 0:
                    spaces += 1
                #clears row if there are no spaces
            if spaces == 0:
                lines += 1
                #moves all lines above the cleared line downwards
                for below_row in range(i, -1, -1):
                    above_row = below_row -1
                    if above_row != -1:
                        for j in range(self.width):
                            self.field[below_row][j] = self.field[above_row][j]
                    else:
                        for j in range(self.width):
                            self.field[below_row][j] = 0
        
        if lines > 0:
            self.lines_cleared += lines

    #locks the piece in place
    def lock(self):
        #finds all spaces around the piece containing the piece's type colour
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.current_piece.get_state():
                    #replaces the blank spaces in the grid with that color
                    self.field[i + self.current_piece.y][j + self.current_piece.x] = self.current_piece.colour
        #clears lines if applicable after locking
        self.clear_lines()
        #spwns a new piece
        self.new_piece()
        #if the piece overlaps with another on spawn
        if self.overlap():
            self.state = "over"

    #draws the currently falling piece
    def draw_piece(self):
        #checks for a falling piece present on the board
        if self.current_piece is not None:
            for i in range(4):
                for j in range(4):
                    p = i *4 + j
                    if p in self.current_piece.get_state():
                    #finds all spaces that the piece occupies 
                    #draws a rectangle for each space that the piece occupies
                        pygame.draw.rect(self.screen, colours[self.current_piece.colour],
                                        [self.x + self.scale * (j + self.current_piece.x),
                                        self.y + self.scale * (i + self.current_piece.y),
                                        self.scale, self.scale])    
 