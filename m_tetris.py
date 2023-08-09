import copy
import random

from tetris_grid import *

class Modern_Tetris(TetrisGrid):

    #inherits from TetrisGrid class, and has own attributes
    def __init__(self,height,width,x,y,screen):
        super().__init__(height,width,x,y,screen)

        #bag of required pieces
        self.held_piece = None
        self.held_state = False
        self.bag = [0, 1, 2, 3, 4, 5, 6]
        self.queue = []
        self.ghost_piece = None
        self.lock_delay = 0

        #fills the queue with a randomised bag at the start of the game
        for i in range(0,2):
            random.shuffle(self.bag)
            for piece in self.bag:
                self.queue.append(piece)
        #sets the current piece to be the first piece in the queue
        self.current_piece = TetrominoModern(3,0,self.queue[0])
        #makes a copy of the current piece with no references to the original
        self.ghost_piece = copy.deepcopy(self.current_piece)

    #acts more as a "next piece function"
    def new_piece(self):
        #dequeues first item and sets current piece to that piece
        self.queue = self.queue[1:]
        self.current_piece = TetrominoModern(3,0,self.queue[0])
        #if the queue is running low on pieces, refill it
        if len(self.queue) < 7:
            random.shuffle(self.bag)
            for piece in self.bag:
                self.queue.append(piece)

    #moves the piece downwards
    def move_down(self):
        self.current_piece.y += 1
        if self.overlap():
            self.lock_delay += 1
            self.current_piece.y -= 1
            #separate case for soft dropping added
            #to compensate for more frequent method calls
            if self.fast_down == False:
                if self.lock_delay >= 2:
                    self.lock()
                    self.lock_delay = 0
            else:
                if self.lock_delay >= 14:
                    self.lock()
                    self.lock_delay = 0

    #instantly drops
    def hard_drop(self):

        #keeps moving the piece down until it would overlap
        while not self.overlap():
            self.current_piece.y += 1
        self.current_piece.y -= 1
        self.lock()

    #function for holding the pieces
    def hold(self):

        #used at the start of the game where there is no held piece
        #moves current piece into held and generates new piece
        #resets rotations/position of pieces
        if self.held_piece == None:
            self.held_piece = self.current_piece
            self.held_piece.rotation = 0
            self.held_state = True
            self.new_piece()

        #used when a held peice exists, and if a hold hasn't been used before a lock function
        elif self.held_piece != None and self.held_state == False:
            self.held_piece, self.current_piece = self.current_piece, self.held_piece
            self.held_piece.rotation = 0
            self.current_piece.y = 0
            self.current_piece.x = 3
            #held state set to true to indicate held has been used
            self.held_state = True

        else:
            pass

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
        self.held_state = False
        #if the piece overlaps with another on spawn
        if self.overlap():
            self.state = "over"

    #draws the hel piece
    def draw_held(self,held_x,held_y):
        if self.held_piece == None:
            pass
        else:
            for i in range(4):
                for j in range(4):
                    p = i *4 +j
                    if p in self.held_piece.get_state():
                        #recalculates x/y coordinates of pieces
                        #to center them correctly
                        if self.held_piece.type == 0:
                            xpos = (self.x-80) + self.scale * (j + held_x)
                            ypos = (self.y-65) + self.scale * (i + held_y)
                        if self.held_piece.type == 1:
                            xpos = (self.x-65) + self.scale * (j + held_x)
                            ypos = (self.y-50) + self.scale * (i + held_y)
                        if self.held_piece.type == 2:  
                            xpos = (self.x-65) + self.scale * (j + held_x)
                            ypos = (self.y-50) + self.scale * (i + held_y)
                        if self.held_piece.type == 3:
                            xpos = (self.x-95) + self.scale * (j + held_x)
                            ypos = (self.y-50) + self.scale * (i + held_y)
                        if self.held_piece.type == 4:
                            xpos = (self.x-95) + self.scale * (j + held_x)
                            ypos = (self.y-50) + self.scale * (i + held_y)
                        if self.held_piece.type == 5:  
                            xpos = (self.x-65) + self.scale * (j + held_x)
                            ypos = (self.y-50) + self.scale * (i + held_y)
                        if self.held_piece.type == 6:
                            xpos = (self.x-80) + self.scale * (j + held_x)
                            ypos = (self.y-50) + self.scale * (i + held_y)
                        #draws the piece onto the screen
                        self.screen.blit(colours_mt[self.held_piece.colour], [xpos, ypos])

    #draws the preview piece
    def draw_preview(self,x,y,piece):

        #creates preview piece local to function
        #since there will be multiple preview pieces
        preview_piece = TetrominoModern(x,y,piece)
        #draws the piece in that queue
        for i in range(4):
            for j in range(4):
                p = i *4 +j
                if p in preview_piece.get_state():
                    #recalculates x/y coordinates of pieces
                    #based on piece for better alignment
                    if piece == 0:
                        xpos = (self.x-80) + self.scale * (j + preview_piece.x)
                        ypos = (self.y-65) + self.scale * (i + preview_piece.y)
                    if piece == 1:
                        xpos = (self.x-65) + self.scale * (j + preview_piece.x)
                        ypos = (self.y-50) + self.scale * (i + preview_piece.y)
                    if piece == 2:  
                        xpos = (self.x-65) + self.scale * (j + preview_piece.x)
                        ypos = (self.y-50) + self.scale * (i + preview_piece.y)
                    if piece == 3:
                        xpos = (self.x-95) + self.scale * (j + preview_piece.x)
                        ypos = (self.y-50) + self.scale * (i + preview_piece.y)
                    if piece == 4:
                        xpos = (self.x-95) + self.scale * (j + preview_piece.x)
                        ypos = (self.y-50) + self.scale * (i + preview_piece.y)
                    if piece == 5:  
                        xpos = (self.x-65) + self.scale * (j + preview_piece.x)
                        ypos = (self.y-50) + self.scale * (i + preview_piece.y)
                    if piece == 6:
                        xpos = (self.x-80) + self.scale * (j + preview_piece.x)
                        ypos = (self.y-50) + self.scale * (i + preview_piece.y)

                    #drwas the piece onto the self.screen
                    self.screen.blit(colours_mt[preview_piece.colour], [xpos, ypos+20])

    #draws the grid for modern tetris
    def draw_grid(self):
         #cycles through each cell
        for i in range(self.height):
            for j in range(self.width):
                #default draws as black cells
                pygame.draw.rect(self.screen,BLACK,[self.x + self.scale *j, 
                                self.y +self.scale*i, 
                                self.scale, self.scale])

                #if the cell contains a coloured piece placed by the user
                if self.field[i][j] > 0:
                    self.screen.blit(colours_mt[self.field[i][j]], [self.x + self.scale * (j),
                                          self.y + self.scale * (i)])

                #draws gridlines in gray around each black cell
                else:
                    pygame.draw.rect(self.screen,DARK_GRAY,[self.x + self.scale *j, 
                        self.y +self.scale*i, 
                        self.scale, self.scale],1)

    #draws the piece that is currently falling
    def draw_piece(self):
        #checks for a falling piece present on the board
        if self.current_piece is not None:
            for i in range(4):
                for j in range(4):
                    p = i *4 + j
                    #finds all spaces that the piece occupies 
                    #draws a rectangle for each space that the piece occupies
                    if p in self.current_piece.get_state():
                        self.screen.blit(colours_mt[self.current_piece.colour], [self.x + self.scale * (j + self.current_piece.x), self.y + self.scale * (i + self.current_piece.y)])

    #draws dynamic UI elements
    def draw_ui(self):
        
        #initialises texts
        next_text = mt_font.render("Next", True, BLACK)
        hold_text = mt_font.render("Hold", True, BLACK)

        #creating black backgrounds for preview, hold and garbage queue elements
        pygame.draw.rect(self.screen,BLACK,[self.x + 11*self.scale, self.y + 1*self.scale, 140,480])
        pygame.draw.rect(self.screen,BLACK,[self.x - 150, self.y + 1*self.scale, 140,80])

        #adds elements to screen
        self.screen.blit(next_text, [self.x + 330, self.y])
        self.screen.blit(hold_text, [self.x - 150, self.y])

    #method for the checking of wall kicks
    def wall_kick(self,angle):
        
        #cases for all pieces except for O and I pieces
        case_1 = [[-1,0],[0,-1],[1,3],[-1,0]]
        case_2 = [[1,0],[0,1],[-1,-3],[1,0]]
        case_3 = [[1,0],[0,-1],[-1,3],[1,0]]
        case_4 = [[-1,0],[0,1],[1,-3],[-1,0]]

        #cases for I piece
        case_5 = [[-2,0],[3,0],[-3,1],[3,-3]]
        case_6 = [[-1,0],[3,0],[-3,-2],[3,3]]
        case_7 = [[2,0],[-3,0],[3,-1],[-3,3]]
        case_8 = [[1,0],[-3,0],[3,2],[-3,-3]]

        #checks if the piece is any piece other than I piece
        if self.current_piece.type in [1,2,3,4,5,6]:
            #checks the angle of rotation
            if angle == 1:
                #checks which rotation the piece is currently in
                if self.current_piece.rotation == 1:
                    #moves the piece by the vector given by the case
                    #repeating for all cases
                    for case in case_1:
                        self.current_piece.x += case[0]
                        self.current_piece.y += case[1]
                        #returns true if the wall kick is successful (no overlap)
                        if self.overlap() == False:
                            return True
                    #returns false if not
                    return False
            
            #does check for all pieces
                if self.current_piece.rotation == 2:
                    for case in case_2:
                        self.current_piece.x += case[0]
                        self.current_piece.y += case[1]
                        if self.overlap() == False:
                            return True
                    return False

                if self.current_piece.rotation == 3:
                    for case in case_3:
                        self.current_piece.x += case[0]
                        self.current_piece.y += case[1]
                        if self.overlap() == False:
                            return True
                    return False

                if self.current_piece.rotation == 0:
                    for case in case_4:
                        self.current_piece.x += case[0]
                        self.current_piece.y += case[1]
                        if self.overlap() == False:
                            return True
                    return False

            #cases for a rotation in the other direction
            else:
                if self.current_piece.rotation == 1:
                    for case in case_1:
                        self.current_piece.x += case[0]
                        self.current_piece.y += case[1]
                        if self.overlap() == False:
                            return True
                    return False
                
                if self.current_piece.rotation == 2:
                    for case in case_4:
                        self.current_piece.x += case[0]
                        self.current_piece.y += case[1]
                        if self.overlap() == False:
                            return True
                    return False

                if self.current_piece.rotation == 3:
                    for case in case_3:
                        self.current_piece.x += case[0]
                        self.current_piece.y += case[1]
                        if self.overlap() == False:
                            return True
                    return False

                if self.current_piece.rotation == 0:
                    for case in case_2:
                        self.current_piece.x += case[0]
                        self.current_piece.y += case[1]
                        if self.overlap() == False:
                            return True
                    return False

        #if the piece is an I piece, checks the cases for the I piece
        else:
            if angle == 1:
                if self.current_piece.rotation == 1:
                    for case in case_5:
                        self.current_piece.x += case[0]
                        self.current_piece.y += case[1]
                        if self.overlap() == False:
                            return True
                    return False

                if self.current_piece.rotation == 2:
                    for case in case_6:
                        self.current_piece.x += case[0]
                        self.current_piece.y += case[1]
                        if self.overlap() == False:
                            return True
                    return False
                
                if self.current_piece.rotation == 3:
                    for case in case_7:
                        self.current_piece.x += case[0]
                        self.current_piece.y += case[1]
                        if self.overlap() == False:
                            return True
                    return False

                if self.current_piece.rotation == 0:
                    for case in case_8:
                        self.current_piece.x += case[0]
                        self.current_piece.y += case[1]
                        if self.overlap() == False:
                            return True
                    return False
            else:
                if self.current_piece.rotation == 1:
                    for case in case_8:
                        self.current_piece.x += case[0]
                        self.current_piece.y += case[1]
                        if self.overlap() == False:
                            return True
                    return False

                if self.current_piece.rotation == 2:
                    for case in case_5:
                        self.current_piece.x += case[0]
                        self.current_piece.y += case[1]
                        if self.overlap() == False:
                            return True
                    return False
                
                if self.current_piece.rotation == 3:
                    for case in case_6:
                        self.current_piece.x += case[0]
                        self.current_piece.y += case[1]
                        if self.overlap() == False:
                            return True
                    return False

                if self.current_piece.rotation == 0:
                    for case in case_7:
                        self.current_piece.x += case[0]
                        self.current_piece.y += case[1]
                        if self.overlap() == False:
                            return True
                    return False

    #new rotate method to take into account the wall kick checks
    def rotate(self,angle):            
        old_x, old_y = self.current_piece.x, self.current_piece.y
        if angle == 1:
            self.current_piece.rotate_cw()
            #if normal rotation would cause overlap, try wall kick method
            if self.overlap():
                wall_kicked = self.wall_kick(angle)
                #if wall kick function fails, revert to original position (fail rotation)
                if wall_kicked == False:
                    self.current_piece.rotate_acw()
                    self.current_piece.x, self.current_piece.y = old_x, old_y

        #same for other angle rotation
        else:
            self.current_piece.rotate_acw()
            if self.overlap():
                wall_kicked = self.wall_kick(angle)
                if wall_kicked == False:
                    self.current_piece.rotate_cw()
                    self.current_piece.x, self.current_piece.y = old_x, old_y

    #checks if a ghost piece would overlap from moving down
    def overlap_ghost(self):
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.ghost_piece.get_state():
                    if i + self.ghost_piece.y > self.height - 1 or \
                        j + self.ghost_piece.x > self.width - 1 or \
                        j + self.ghost_piece.x < 0 or \
                            self.field[i +self.ghost_piece.y][j + self.ghost_piece.x] > 0:
                        return True
        return False

    #ghost piece will need to be drawn at lowest possible drop position
    #position will be same as hard drop position
    def drop_ghost(self):
        while not self.overlap_ghost():
            self.ghost_piece.y += 1
        self.ghost_piece.y -= 1
        
    #draws the ghost piece in its dropped position
    def draw_ghost(self):
        #deep copy used to make the variable its own object
        #with same attributes but not shared via reference with the original
        self.ghost_piece = copy.deepcopy(self.current_piece)
        self.drop_ghost()
        for i in range(4):
            for j in range(4):
                p = i *4 +j
                if p in self.ghost_piece.get_state():
                    xpos = self.x + self.scale * (j + self.ghost_piece.x)
                    ypos = self.y + self.scale * (i + self.ghost_piece.y)

                    #new drawing method for the ghost piece
                    s = pygame.Surface((self.scale,self.scale))
                    s.set_alpha(128)
                    s.blit(colours_mt[self.ghost_piece.colour],[0,0])
                    self.screen.blit(s,(xpos,ypos))

class Modern_Tetris_Sprint(Modern_Tetris):

    def __init__(self,height,width,x,y,screen):
        #same attributes as normal modern Tetris
        #with inclusion of time attributes
        super().__init__(height,width,x,y,screen)
        self.miliseconds = 0
        self.seconds = 0
        self.minutes = 0
        
    #stopwatch method to convert the counter (pseudo-miliseconds) to seconds
    #and seconds to minutes
    def stopwatch(self):
        self.miliseconds = (self.counter*2)%100
        if self.counter != 0:
            if self.miliseconds %100 == 0:
                self.seconds += 1
            if self.seconds %60 == 0:
                self.seconds = 0
            if self.counter % 3000 == 0:
                self.minutes += 1
    
    #draws the dynamic UI which will now include the stopwatch
    def draw_ui(self):

        #called to constantly update the clock
        self.stopwatch()

        #renders fonts
        next_text = mt_font.render("Next", True, BLACK)
        hold_text = mt_font.render("Hold", True, BLACK)
        lines_text = mt_font_big.render("Lines: "+str(self.lines_cleared), True, WHITE)
        stopwatch_text = mt_font_big.render(str(self.minutes)+":"
                                        +str(self.seconds)+":"
                                        +str(self.miliseconds), True, WHITE)

        #black backgrounds for boxes UI elements
        pygame.draw.rect(self.screen,BLACK,[self.x + 11*self.scale, self.y + 1*self.scale, 140,480])
        pygame.draw.rect(self.screen,BLACK,[self.x - 150, self.y + 1*self.scale, 140,80])
        pygame.draw.rect(self.screen,BLACK,[self.x - 150, self.y + 1*self.scale + 90, 140,120])

        #adds elements to the screen
        self.screen.blit(next_text, [self.x + 330, self.y])
        self.screen.blit(hold_text, [self.x - 150, self.y])
        self.screen.blit(stopwatch_text, [self.x -140, self.y + 180])
        self.screen.blit(lines_text,[self.x - 140, self.y + 140])