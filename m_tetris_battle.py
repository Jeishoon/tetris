from m_tetris import *

class Modern_Tetris_2P(Modern_Tetris):

    #initialised the same as normal modern Tetris
    #with addition of garbage lines to be send or added
    def __init__(self,height,width,x,y,screen):
        super().__init__(height,width,x,y,screen)
        self.field = []
        self.garbage_now = 0
        self.garbage_sent = 0

        #filling grid with empty spaces
        for i in range(height):
            new_line = []
            for j in range(width):
                new_line.append(0)
            self.field.append(new_line)

        #creates initial 7 bag of pieces
        for i in range(0,2):
            random.shuffle(self.bag)
            for piece in self.bag:
                self.queue.append(piece)
        
        #initialises pieces lower down due to higher field
        self.current_piece = TetrominoModern(3,20,self.queue[0])
        self.ghost_piece = copy.deepcopy(self.current_piece)

    #new method requires to spawn piece at right height
    def new_piece(self):

        #dequeues first item and sets current piece to that piece
        self.queue = self.queue[1:]
        self.current_piece = TetrominoModern(3,20,self.queue[0])
        #if the queue is running low on pieces, refill it
        if len(self.queue) < 7:
            random.shuffle(self.bag)
            for piece in self.bag:
                self.queue.append(piece)

    #draws bottom 20 spaces of grid
    #since top 20 are used only to store pieces moving upwards
    def draw_grid(self):
        #cycles through each cell
        for i in range(20,self.height):
            for j in range(self.width):
                #default draws as black cells
                pygame.draw.rect(self.screen,BLACK,[self.x + self.scale *j, 
                                (self.y +self.scale*i), 
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

    #hard drop function
    def hard_drop(self):

        #keeps moving the piece down until it would overlap
        while not self.overlap():
            self.current_piece.y += 1
        self.current_piece.y -= 1
        self.lock()

    #adding garbage to the grid
    def add_garbage(self):
        
        #checks for rows that have pieces in to move up
        #so that empty lines do not have to be moved up
        for row in range(1,self.height):
            occupy  = False
            for cell in range(self.width):
                if self.field[row][cell] > 0:
                    occupy = True

            #moves the row up if it contains a non space piece
            if occupy == True:
                below_row = row
                above_row = below_row - self.garbage_now
                for j in range(0,self.width):
                    self.field[above_row][j] = self.field[below_row][j]
                    self.field[below_row][j] = 0

        #creates line with a randomly chosen space
        line_add = []
        for i in range(self.width):
            line_add.append(8)
        space = random.randint(0,self.width-1)
        line_add[space] = 0
        #adds garbage lines from the bottom upwards
        for row in range(39,39-self.garbage_now,-1):
            self.field[row] = list(line_add)
        #resets the garbage to be added
        self.garbage_now = 0

    #method to clear lines adjusted to account for reduction in garbage
    #from garbage countering
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
                for below_row in range(i, 1, -1):
                    above_row = below_row -1
                    for j in range(self.width):
                        self.field[below_row][j] = self.field[above_row][j]
        
        #adds garbage if no lines cleared
        if lines == 0:
            if self.garbage_now > 0:
                self.add_garbage()

        #removes garbage if lines are cleared
        if lines > 0:
            self.lines_cleared += lines
            if self.garbage_now > 0:
                self.garbage_now -= lines
                if self.garbage_now < 0:
                    lines = -(self.garbage_now)
                    self.garbage_now = 0

        #sents garbage to opponent if no incoming garbage
        #and done after garbage is cleared so that excess lines
        #are sent to opponent
        if lines > 1 and self.garbage_now == 0:       
            if lines == 2:
                self.garbage_sent = 1
            if lines == 3:
                self.garbage_sent = 2
            if lines == 4:
                self.garbage_sent = 4



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

    #hold method adjusted to reset held piece
    #to correct height for the new tetris grid height
    def hold(self):
        if self.held_piece == None:
            self.held_piece = self.current_piece
            self.held_piece.rotation = 0
            self.held_state = True
            self.new_piece()

        elif self.held_piece != None and self.held_state == False:
            self.held_piece, self.current_piece = self.current_piece, self.held_piece
            self.held_piece.rotation = 0
            self.current_piece.x = 3
            self.current_piece.y = 20
            self.held_state = True

        else:
            pass
    
    #draws the UI to incude
    def draw_ui(self):
        
        next_text = mt_font.render("Next", True, BLACK)
        hold_text = mt_font.render("Hold", True, BLACK)
        garbage_meter = pygame.Rect(self.x + 310, self.y + 1200, 10, 
            (-1)*(self.scale*20))
        garbage_meter.normalize()

        pygame.draw.rect(self.screen,BLACK,[self.x + 11*self.scale, self.y + 21*self.scale, 140,480])
        pygame.draw.rect(self.screen,BLACK,[self.x - 150, self.y + 21*self.scale, 140,80])
        pygame.draw.rect(self.screen,BLACK,garbage_meter)
        
        self.screen.blit(next_text, [self.x + 330, self.y+600])
        self.screen.blit(hold_text, [self.x - 150, self.y+600])

class Modern_Tetris_Battle():

    def __init__(self,game1,game2,screen):
        self.game1 = game1
        self.game2 = game2
        self.screen = screen

    #sends garbage between players
    def send_garbage(self):
        if self.game1.garbage_sent > 0:
            self.game2.garbage_now += self.game1.garbage_sent
            self.game1.garbage_sent = 0
        if self.game2.garbage_sent > 0:
            self.game1.garbage_now += self.game2.garbage_sent
            self.game2.garbage_sent = 0

    #draws the garbage meters to move up and down
    #based on garbage to be added for the two games
    def draw_garbage_meter(self):
        p1_meter =  pygame.Rect(self.game1.x + 310, self.game1.y + 1200, 10, 
            (-1)*(self.game1.garbage_now * self.game1.scale))
        p2_meter = pygame.Rect(self.game2.x + 310, self.game2.y + 1200, 10, 
            (-1)*(self.game2.garbage_now * self.game2.scale))
        #normalise function used to display negative height going upwards
        p1_meter.normalize()
        p2_meter.normalize()
        pygame.draw.rect(self.screen, colours[2], p1_meter)
        pygame.draw.rect(self.screen, colours[2], p2_meter)