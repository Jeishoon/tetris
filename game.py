from das import *
from controls import *
from ct_grid import *
from m_tetris import *
from m_tetris_battle import *


#function for game
def play(mode, controls, ct_level, screen, clock):
################################## SINGLE CLASSIC NORMAL ##################################

    if mode == "single_classic_normal":

        #variables for the position of the classic Tetris boards
        player1_x = 400
        player1_y = 60

        #initialises the game
        game = Classic_Tetris(20,10,player1_x,player1_y,screen)  
        #changes the level to the requested level 
        game.level = ct_level   
        #incremenets counter intially to avoid bugs caused by modulo
        #division when counter is 0
        game.counter += 1  
        #draws the static UI elemnts of the game
        #e.g the frames around the game
        draw_ui(mode,game,screen)
        #updates the display with the UI
        pygame.display.flip()

        #main game loop
        while game.state == "playing":
            #start delay
            if game.counter > 0:
                #periodically moves the current piece down
                if game.fast_down == False:
                    if game.counter % (game.speed[game.level]) == 0:
                        game.move_down()
                #faster moving down if holding down button
                else:
                    if game.counter % (2) == 0:
                        game.move_down()

            das_check(game)
            #loads controls, fills screen, draws the grid, 
            #currently moving piece and preview piece,
            #counter is incrememnted and the screen is updated.
            #clock tick is set at 60 fps
            load_controls(mode,game,controls,screen)
            game.draw_ui()
            game.draw_grid()
            game.draw_piece()
            game.draw_preview(15,9)
            game.counter += 1  
            
            pygame.display.flip()

            clock.tick(50)
        
        #returns information about the game
        #to be displayed on the end screen
        return [mode, game.score]

################################## SINGLE CLASSIC DS ##################################

    if mode == "single_classic_downstack":

        #function to count remaining garbage at the end
        def count_garbage(game):
            garbage_left = 0
            for j in range (0,game.height):
                garbage = False
                for k in range(0,game.width):
                    if game.field[j][k] == 8:
                        garbage = True
                if garbage == True:
                    garbage_left += 1
            return garbage_left

        player1_x = 400
        player1_y = 60

        game = Classic_Tetris_DS(20,10,player1_x,player1_y,screen) 
        game.counter += 1

        draw_ui(mode,game,screen)

        while game.state == "playing":
            if game.counter > 0:
                if game.fast_down == False:
                    if game.counter % (game.speed[game.level]) == 0:
                        game.move_down()

                else:
                    if game.counter % (2) == 0:
                        game.move_down()

            das_check(game)

            load_controls(mode,game,controls,screen)
            game.draw_ui()
            game.draw_grid()
            game.draw_piece()
            game.draw_preview(15,9)
            game.counter += 1  
            game.check_garbage()
            pygame.display.flip()

            clock.tick(50)

        garbage_left = count_garbage(game)
        return [mode, garbage_left]

################################## MULTI CLASSIC NORMAL ##################################

    if mode == "multi_classic_normal":
       
        game1 = Classic_Tetris(20,10,50,60,screen)
        game2 = Classic_Tetris(20,10,700,60,screen)
        
        game1.level = ct_level
        game2.level = ct_level 

        game = [game1, game2]
        draw_ui(mode,game,screen)

        for i in range(0,2):
            game[i].counter += 1

        while game1.state == "playing" or game2.state == "playing":

            load_controls(mode,game,controls,screen)
            game1.draw_ui()
            game1.draw_grid()
            game1.draw_piece()
            game1.draw_preview(15,9)


            game2.draw_ui()
            game2.draw_grid()
            game2.draw_piece()
            game2.draw_preview(15,9)
            
            if game1.state == "playing":
                game1.counter += 1 
                if game1.counter > 0:
                    if game1.fast_down == False:
                        if game1.counter % (game1.speed[game1.level]) == 0:
                            game1.move_down()

                    else:
                        if game1.counter % (2) == 0:
                            game1.move_down()
                
                das_check(game1)

            if game2.state == "playing":
                game2.counter += 1 
                if game2.counter > 0:
                    if game2.fast_down == False:
                        if game2.counter % (game2.speed[game2.level]) == 0:
                            game2.move_down()

                    else:
                        if game2.counter % (2) == 0:
                            game2.move_down()

                das_check(game2)

            pygame.display.flip()

            clock.tick(50)

        return [mode,game1.score,game2.score]

################################## MULTI CLASSIC DS ##################################

    if mode == "multi_classic_downstack":

        #function to count remaining garbage at the end
        def count_garbage(game):
            garbage_left = [0,0]
            for i in range(0,2):
                for j in range (0,game[i].height):
                    garbage = False
                    for k in range(0,game[i].width):
                        if game[i].field[j][k] == 8:
                            garbage = True
                    if garbage == True:
                        garbage_left[i] += 1
            return garbage_left

        game1 = Classic_Tetris_DS(20,10,50,60,screen)
        game2 = Classic_Tetris_DS(20,10,700,60,screen) 

        game = [game1, game2]

        for i in range(0,1):
            game[i].counter += 1

        draw_ui(mode,game,screen)

        while game1.state == "playing" or game2.state == "playing":

            load_controls(mode,game,controls,screen)

            game1.draw_grid()
            game1.draw_piece()
            game1.draw_ui()
            game1.draw_preview(15,9)
            game1.check_garbage()

            game2.draw_grid()
            game2.draw_piece()
            game2.draw_ui()
            game2.draw_preview(15,9)
            game2.check_garbage()

            if game1.state == "playing":
                
                game1.counter += 1 
                if game1.counter > 0:
                    if game1.fast_down == False:
                        if game1.counter % (game1.speed[game1.level]) == 0:
                            game1.move_down()

                    else:
                        if game1.counter % (2) == 0:
                            game1.move_down()
            
                das_check(game1)

            if game2.state == "playing":

                game2.counter += 1 
                if game2.counter > 0:
                    if game2.fast_down == False:
                        if game2.counter % (game2.speed[game2.level]) == 0:
                            game2.move_down()

                    else:
                        if game2.counter % (2) == 0:
                            game2.move_down()
                    
                das_check(game2)

            pygame.display.flip()

            clock.tick(50)

        garbage_left = count_garbage(game)
        return [mode,garbage_left,game1.counter,game2.counter]


################################## SINGLE MDOERN ZEN ##################################

    if mode == "single_modern_zen":
        
        game = Modern_Tetris(20,10,400,60,screen) 
        draw_ui(mode,game,screen)

        game.counter += 1

        while game.state == "playing":

            if game.fast_down == False:
                if game.counter % (48) == 0:
                    game.move_down()

            else:
                if game.counter % (2) == 0:
                    game.move_down()
            
            das_check(game)

            load_controls(mode,game,controls,screen)
            game.draw_ui()
            game.draw_grid()
            game.draw_piece()
            game.draw_ghost()
            game.draw_held(-2,3)


            for i in range(1,6):
                game.draw_preview(14,i*3,game.queue[i])

            game.counter += 1
            pygame.display.flip()

            clock.tick(50)

        return [mode]


################################## SINGLE MODERN SPRINT ##################################

    if mode == "single_modern_sprint":

        game = Modern_Tetris_Sprint(20,10,400,60,screen) 
        draw_ui(mode,game,screen)

        while game.state == "playing":

            game.counter += 1

            if game.fast_down == False:
                if game.counter % (48) == 0:
                    game.move_down()

            else:
                if game.counter % (2) == 0:
                    game.move_down()
            
            das_check(game)

            load_controls(mode,game,controls,screen)
            game.draw_ui()
            game.draw_grid()
            game.draw_piece()
            game.draw_ghost()
            game.draw_held(-2,3)


            for i in range(1,6):
                game.draw_preview(14,i*3,game.queue[i])

            #game state changed to indicate successful finish
            if game.lines_cleared >= 40:
                game.state = "finish"
                game.lines_cleared = 40
            pygame.display.flip()

            clock.tick(50)
    
        time = str(game.minutes)+":"+str(game.seconds)+":"+str(game.miliseconds)
        return [mode,time,game.lines_cleared]

################################## MULTI MODERN NORMAL ##################################

    if mode == "multi_modern_normal":

        game1 = Modern_Tetris_2P(40,10,165,-540,screen)
        game2 = Modern_Tetris_2P(40,10,800,-540,screen)
        game = [game1, game2]
        game_battle = Modern_Tetris_Battle(game1,game2,screen)
        draw_ui(mode,game,screen)

        for i in range(0,2):
            game[i].counter += 1

        while game1.state == "playing" and game2.state == "playing":

            load_controls(mode,game,controls,screen)

            game1.draw_ui()
            game1.draw_grid()
            game1.draw_piece()
            game1.draw_ghost()
            game1.draw_held(-2,23)

            for i in range(1,6):
                game1.draw_preview(14,20+i*3,game1.queue[i])

            game2.draw_ui()
            game2.draw_grid()
            game2.draw_piece()
            game2.draw_ghost()
            game2.draw_held(-2,23)
  
            for i in range(1,6):
                game2.draw_preview(14,20+i*3,game2.queue[i])

            game_battle.send_garbage()
            game_battle.draw_garbage_meter()

            if game1.state == "playing":
                
                game1.counter += 1

                if game1.fast_down == False:
                    if game1.counter % (48) == 0:
                        game1.move_down()

                else:
                    if game1.counter % (2) == 0:
                        game1.move_down()

                das_check(game1)


            if game2.state == "playing":
 
                game2.counter += 1

                if game2.fast_down == False:
                    if game2.counter % (48) == 0:
                        game2.move_down()

                else:
                    if game2.counter % (2) == 0:
                        game2.move_down()

                das_check(game2)

            pygame.display.flip()

            clock.tick(50)

        if game1.state == "forced_over" or game2.state == "forced_over":
            return [mode, "draw"]
        if game1.state == "over":
            return [mode, "player_2"]
        if game2.state == "over":
            return [mode, "player_1"]

################################## MULTI MODERN SPRINT ##################################

    if mode == "multi_modern_sprint":
        
        game1 = Modern_Tetris_Sprint(20,10,165,60,screen)
        game2 = Modern_Tetris_Sprint(20,10,800,60,screen)
        game = [game1, game2]
        draw_ui(mode,game,screen)

        for i in range(0,2):
            game[i].counter += 1

        while game1.state == "playing" or game2.state == "playing":  

            if game1.lines_cleared >= 40:
                game1.state = "finish"

            if game2.lines_cleared >= 40:
                game2.state = "finish"

            load_controls(mode,game,controls,screen)

            game1.draw_ui()
            game1.draw_grid()
            game1.draw_piece()
            game1.draw_ghost()
            game1.draw_held(-2,3)

            for i in range(1,6):
                game1.draw_preview(14,i*3,game1.queue[i])

            game2.draw_ui()
            game2.draw_grid()
            game2.draw_piece()
            game2.draw_ghost()
            game2.draw_held(-2,3)
  
            for i in range(1,6):
                game2.draw_preview(14,i*3,game2.queue[i])

            if game1.state == "playing":
                
                game1.counter += 1

                if game1.fast_down == False:
                    if game1.counter % (48) == 0:
                        game1.move_down()

                else:
                    if game1.counter % (2) == 0:
                        game1.move_down()

                das_check(game1)


            if game2.state == "playing":

                game2.counter += 1

                if game2.fast_down == False:
                    if game2.counter % (48) == 0:
                        game2.move_down()

                else:
                    if game2.counter % (2) == 0:
                        game2.move_down()

                das_check(game2)

            pygame.display.flip()

            clock.tick(50)

        game1_time = str(game1.minutes)+":"+str(game1.seconds)+":"+str(game1.miliseconds)
        game2_time = str(game2.minutes)+":"+str(game2.seconds)+":"+str(game2.miliseconds)

        if game1.state == "finish" and game2.state == "finish":
            if game1.counter < game2.counter: 
                return [mode, game1_time, game2_time, "player_1", game1.lines_cleared, game2.lines_cleared]
            if game2.counter < game1.counter: 
                return [mode, game1_time, game2_time, "player_2", game1.lines_cleared, game2.lines_cleared]
            if game2.counter == game1.counter: 
                return [mode, game1_time, game2_time, "draw", game1.lines_cleared, game2.lines_cleared]                
        elif game1.state == "finish" and game2.state != "finish":
            return [mode, game1_time, game2_time, "player_1", game1.lines_cleared, game2.lines_cleared]
        elif game1.state != "finish" and game2.state == "finish":
            return [mode, game1_time, game2_time, "player_2", game1.lines_cleared, game2.lines_cleared]
        else:
            return [mode, game1_time, game2_time, "draw", game1.lines_cleared, game2.lines_cleared]