#checks for das movement (holding down left/right)
def das_check(game):

        #checks if the flag for DAS is True
        #meaning that the arrow key is pressed
        if game.fast_left == True:
            game.left_counter += 1
            #only activates DAS when above a certain delay
            #for repeated movement
            if game.left_counter > 10:
                if game.counter %3 == 0:
                    game.move_lr(-1)
        #DAS flag switched to false when player stops holding key
        #so DAS counter is reset to avoid continued DAS movement
        else:
            game.left_counter = 0
        
        #DAS for the opposite direction
        if game.fast_right == True:
            game.right_counter += 1
            if game.right_counter > 10:
                if game.counter %3 == 0:
                    game.move_lr(1)
        else:
            game.right_counter = 0