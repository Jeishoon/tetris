import random

from tetris_grid import *

################################## MAIN CLASSIC ##################################

class Classic_Tetris(TetrisGrid):

    #inherits from TetrisGrid class, and has own attributes
    def __init__(self,height,width,x,y,screen):
        super().__init__(height,width,x,y,screen)
        self.queue = [None,None]
        self.level = 0
        self.score = 0
        self.counter = -75
        #list of speeds
        self.speed = [
            48,43,38,33,28,
            23,18,13,8,6,5,
            5,5,4,4,4,3,3,3,
            2,2,2,2,2,2,2,2,
            2,2,1
            ]

        #when instantiated, fills the queue with intial pieces
        for i in range(0,2):
            initial_piece = random.randint(0,6)
            self.queue[i] = initial_piece

        #sets the intial piece
        self.current_piece = TetrominoClassic(3,0,self.queue[0])

    #piece generation function
    def new_piece(self):
        #moves the next piece into the current piece position
        self.queue[0] = self.queue[1]
        #random generation function dice roll #1
        self.next_piece = random.randint(0,7)
        if self.next_piece == self.queue[0] or self.next_piece == 7:
            #dice roll 2 if duplicate piece or rolled 7
            self.next_piece = random.randint(0,6)
        else:
            pass
        #remove used piece from queue
        self.queue.pop(1)
        #make current piece the next piece in queue
        self.current_piece = TetrominoClassic(3,0,self.queue[0])
        #add next piece to queue
        self.queue.append(self.next_piece)
        pygame.time.wait(200)
    
    def draw_preview(self,x,y):
        #creates new tetris piece using the upcoming piece   
        self.preview_piece = TetrominoClassic(x,y,self.queue[1])
        #same drawing function as the draw piece
        for i in range(4):
            for j in range(4):
                p = i *4 +j
                if p in self.preview_piece.get_state():
                    #gives altered x/y positions of pieces
                    if self.preview_piece.type == 0:
                        xpos = (self.x-80) + self.scale * (j + x)
                        ypos = (self.y-70) + self.scale * (i + y)
                    if self.preview_piece.type == 1:
                        xpos = (self.x-60) + self.scale * (j + x)
                        ypos = (self.y-50) + self.scale * (i + y)
                    if self.preview_piece.type == 2:  
                        xpos = (self.x-60) + self.scale * (j + x)
                        ypos = (self.y-50) + self.scale * (i + y)
                    if self.preview_piece.type == 3:
                        xpos = (self.x-65) + self.scale * (j + x)
                        ypos = (self.y-50) + self.scale * (i + y)
                    if self.preview_piece.type == 4:
                        xpos = (self.x-65) + self.scale * (j + x)
                        ypos = (self.y-50) + self.scale * (i + y)
                    if self.preview_piece.type == 5:  
                        xpos = (self.x-60) + self.scale * (j + x)
                        ypos = (self.y-50) + self.scale * (i + y)
                    if self.preview_piece.type == 6:
                        xpos = (self.x-75) + self.scale * (j + x)
                        ypos = (self.y-50) + self.scale * (i + y)

                    self.self.screen.blit(colours_ct[self.preview_piece.colour], [xpos, ypos])

    #clears lines if a full row is detected from the original TetrisGrid class
    #but includes scoring/lines
    def clear_lines(self):
        lines = 0
        for i in range(1, self.height):
            spaces = 0
            for j in range(self.width):
                if self.field[i][j] == 0:
                    spaces += 1
            if spaces == 0:
                lines += 1
                for below_row in range(i, -1, -1):
                    above_row = below_row -1
                    if above_row != -1:
                        for j in range(self.width):
                            self.field[below_row][j] = self.field[above_row][j]
                    else:
                        for j in range(self.width):
                            self.field[below_row][j] = 0
        
        #only checked if lines are cleared
        if lines > 0:
            #points given depended on lines cleared
            if lines == 4:
                self.score += 1200 * (self.level + 1)
            if lines == 3:
                self.score += 300 * (self.level + 1)
            if lines == 2:
                self.score += 100 * (self.level + 1)
            if lines == 1:
                self.score += 40 * (self.level + 1)
            
            #adds number of lines cleared to total line count
            #increases level when level up lines number reached
            self.lines_cleared += lines
            if self.lines_cleared >= (self.level + 1)*10:
                self.level += 1

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

    #draws the tetris grid
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
                    self.screen.blit(colours_ct[self.field[i][j]], [self.x + self.scale * (j),
                                          self.y + self.scale * (i)])

    #draws the currently falling piece
    def draw_piece(self):
        #checks for a falling piece present on the board
        if self.current_piece is not None:
            for i in range(4):
                for j in range(4):
                    p = i *4 + j
                    #finds all spaces that the piece occupies 
                    #draws a rectangle for each space that the piece occupies
                    if p in self.current_piece.get_state():
                        self.screen.blit(colours_ct[self.current_piece.colour], [self.x + self.scale * (j + self.current_piece.x), self.y + self.scale * (i + self.current_piece.y)])

    #draws dynamic UI elements
    def draw_ui(self):

        #initialising texts
        score_text = ct_font.render("Score", True, WHITE)
        score_num = ct_font.render(str(self.score), True, WHITE)
        level_text = ct_font.render("Level "+str(self.level), True, WHITE)
        lines_text = ct_font.render("Lines "+str(self.lines_cleared), True, WHITE)
        next_text = ct_font.render("Next", True, WHITE)

        #drawing box backgrounds
        pygame.draw.rect(self.screen,BLACK,[self.x + 340, self.y, 200,130])
        pygame.draw.rect(self.screen,BLACK,[self.x + 340, self.y + 180, 200,160])
        pygame.draw.rect(self.screen,BLACK,[self.x + 340, self.y + 380, 200,160])

        #adding all elements to the screen
        self.screen.blit(score_text, [self.x + 360, self.y + 30])
        self.screen.blit(score_num, [self.x + 360, self.y + 60])
        self.screen.blit(next_text, [self.x + 390, self.y + 200])
        self.screen.blit(level_text, [self.x + 360, self.y + 410])
        self.screen.blit(lines_text, [self.x + 360, self.y + 470])