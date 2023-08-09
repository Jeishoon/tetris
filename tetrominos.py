class TetrominoClassic:

    #shapes/orientations of all tetrominoes
    shapes = [ 
        [[8, 9, 10, 11], [2, 6, 10, 14]], #I piece
        [[4, 5, 9, 10], [2, 6, 5, 9]], #Z piece
        [[5, 6, 8, 9], [1, 5, 6, 10]], #S piece
        [[4, 5, 6, 10], [1, 5, 8, 9], [0, 4, 5, 6], [1, 2, 5, 9]], #J piece
        [[4, 5, 6, 8], [0, 1, 5, 9], [2, 4, 5, 6], [1, 5, 9, 10]], #L piece
        [[4, 5, 6, 9], [1, 4, 5, 9], [1, 4, 5, 6], [1, 5, 6, 9]], #T piece
        [[5, 6, 9, 10]] #O piece
        ]

    #constructor method
    def __init__(self,x,y,shape):
        self.x = x
        self.y = y
        self.type = shape
        self.colour = shape + 1
        self.rotation = 0

    #clockwise piece rotation
    def rotate_cw(self):
        self.rotation = (self.rotation + 1) % len(self.shapes[self.type])

    #anticlockwise piece rotation 
    def rotate_acw(self):
        self.rotation = abs((self.rotation -1) % len(self.shapes[self.type]))

    #returns figures
    def get_state(self):
        return self.shapes[self.type][self.rotation]

class TetrominoModern(TetrominoClassic):
#class for shapes/rotations of modern tetris pieces

    shapes = [ 
        [[4, 5, 6, 7], [2, 6, 10, 14], [8, 9, 10, 11], [1, 5, 9, 13]], #I piece
        [[0, 1, 5, 6], [2, 6, 5, 9], [4, 5, 9, 10], [1, 4, 5, 8]], #Z piece
        [[1, 2, 4, 5], [1, 5, 6, 10], [5, 6, 8, 9], [0, 4, 5, 9]], #S piece
        [[1, 5, 6, 7], [2, 3, 6, 10], [5, 6, 7, 11], [2, 6, 9, 10]], #J piece
        [[3, 5, 6, 7], [2, 6, 10, 11], [5, 6, 7, 9], [1, 2, 6, 10]], #L piece
        [[1, 4, 5, 6], [1, 5, 6, 9], [4, 5, 6, 9], [1, 4, 5, 9]], #T piece
        [[1, 2, 5, 6]] #O piece
        ]

    def __init__(self,x,y,shape):
        super().__init__(x,y,shape)