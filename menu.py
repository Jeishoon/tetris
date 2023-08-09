import copy

from button import *
from game import *

#Menu pages
def main_menu(menu_page,pages_stack,screen,clock,running):

    global result

    #function to wait for user key press for rebinding controls
    def wait_keypress(menu_page):

        #draws translucent layer above
        pause_screen = pygame.Surface((1280,720))
        pause_screen.set_alpha(128)
        pause_screen.fill(BLACK)
        screen.blit(pause_screen,(0,0))

        #displaying different text depending on game mode
        if menu_page in [10,11]:
            rebind_text = ct_font.render("Press any key to rebind. Press ESC to cancel", True, WHITE)
            screen.blit(rebind_text, [640 - rebind_text.get_width()//2, 360])

        if menu_page in [13,14]:
            rebind_text = mt_font_big.render("Press any key to rebind. Press ESC to cancel", True, WHITE)
            screen.blit(rebind_text, [640 - rebind_text.get_width()//2, 360])

        pygame.display.flip()

        #main loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                #only returns key if key other than escape is presssed
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return False
                    else:
                        return event.key

#list of texts for classic and modern tetris controls menus

    #initialising classic tetris texts
    ct_left_text = ct_font.render("Left", True, WHITE)
    ct_right_text = ct_font.render("Right", True, WHITE)
    ct_rotate_1_text = ct_font.render("Rotate 1", True, WHITE)
    ct_rotate_2_text = ct_font.render("Rotate 2", True, WHITE)
    ct_soft_drop_text = ct_font.render("Soft Drop", True, WHITE)

    #array of classic tetris text
    ct_texts = [
        ct_left_text,
        ct_right_text,
        ct_rotate_1_text,
        ct_rotate_2_text,
        ct_soft_drop_text
    ]

    #initialising modern tetris texts
    mt_left_text = mt_font.render("Left", True, WHITE)
    mt_right_text = mt_font.render("Right", True, WHITE)
    mt_rotate_1_text = mt_font.render("Rotate 1", True, WHITE)
    mt_rotate_2_text = mt_font.render("Rotate 2", True, WHITE)
    mt_soft_drop_text = mt_font.render("Soft Drop", True, WHITE)
    mt_hard_drop_text = mt_font.render("Hard Drop", True, WHITE)
    mt_hold_text = mt_font.render("Hold", True, WHITE)

    #array of modern tetris texts
    mt_texts = [
        mt_left_text,
        mt_right_text,
        mt_rotate_1_text,
        mt_rotate_2_text,
        mt_soft_drop_text,
        mt_hard_drop_text,
        mt_hold_text
    ]

#Flags for checking button presses

    #flags checking for next/previous menu
    next_menu1 = False
    next_menu2 = False
    next_menu3 = False
    next_menu4 = False
    back_menu = False

    #flags for buttons changing classic Tetris menu
    #and variable for starting level
    up_level = False
    down_level = False
    start_level = 0

    #flags for singleplayer/player 1 controls
    left_control1 = False
    right_control1 = False
    rotate_cw_control1 = False
    rotate_acw_control1 = False
    soft_drop_control1 = False
    hard_drop_control1 = False
    hold_control1 = False

    #flags for player 2 controls
    left_control2 = False
    right_control2 = False
    rotate_cw_control2 = False
    rotate_acw_control2 = False
    soft_drop_control2 = False
    hard_drop_control2 = False
    hold_control2 = False


#arrays containing potential buttons flags on a certain menu pages

    next_menu_list = [next_menu1,next_menu2,next_menu3,next_menu4]

    controls_buttons1 = [
        left_control1,right_control1,rotate_cw_control1,rotate_acw_control1,soft_drop_control1,
        hard_drop_control1,hold_control1    
    ]

    controls_buttons2 = [
        left_control2,right_control2,rotate_cw_control2,rotate_acw_control2,soft_drop_control2,
        hard_drop_control2,hold_control2        
    ]

    #array containing dictionary keys for controls
    #modern controls are same as classic controls with addition of hard drop and hold
    #and so can be made as deep copies of those arrays
    ct_controls_refs = ["left","right","rotate_cw","rotate_acw","soft_drop"]
    mt_controls_refs = copy.deepcopy(ct_controls_refs) + ["hard_drop", "hold"]
    ct_controls_p1_refs = ["p1_left","p1_right","p1_rotate_cw","p1_rotate_acw","p1_soft_drop"]
    mt_controls_p1_refs = copy.deepcopy(ct_controls_p1_refs) + ["p1_hard_drop", "p1_hold"]
    ct_controls_p2_refs = ["p2_left","p2_right","p2_rotate_cw","p2_rotate_acw","p2_soft_drop"]
    mt_controls_p2_refs = copy.deepcopy(ct_controls_p2_refs) + ["p2_hard_drop", "p2_hold"]

    while running:

        #game end screen page
        if menu_page == -1:

            #checks the first value in the array for styling page
            if result[0] == "single_classic_normal" or \
                result[0] == "single_classic_downstack" or \
                result[0] == "multi_classic_normal" or \
                result[0] == "multi_classic_downstack":

                screen.blit(classic_tetris_bg, (0,0))
                exit_button = Button("ct", "main menu", 540, 500, screen)

            if result[0] == "single_modern_zen" or \
                result[0] == "single_modern_sprint" or \
                result[0] == "multi_modern_normal" or \
                result[0] == "multi_modern_sprint":

                    screen.blit(modern_tetris_bg, (0,0))
                    exit_button = Button("mt", "main menu", 540, 500, screen)
            
            #blits text to screen depending on the mode
            if result[0] == "single_classic_normal":
                score_text = ct_font.render("Score: "+str(result[1]), True, WHITE)
                screen.blit(score_text, [640 - score_text.get_width()//2, 360])

            if result[0] == "single_classic_downstack":
                lines_text = ct_font.render("Garbage lines left: "+str(result[1]), True, WHITE)
                screen.blit(lines_text, [640 - lines_text.get_width()//2, 360])

            if result[0] == "multi_classic_normal":
                #checking which player has higehr score
                if result[1] > result[2]:
                    player_text = ct_font.render("Player 1 Wins", True, WHITE)
                if result[2] > result[1]:
                    player_text = ct_font.render("Player 2 Wins", True, WHITE)
                if result[1] == result[2]:
                    player_text = ct_font.render("Draw", True, WHITE)
                
                score_text1 = ct_font.render("Player 1 score: "+str(result[1]), True, WHITE)
                score_text2 = ct_font.render("Player 2 score: "+str(result[2]), True, WHITE)
                screen.blit(player_text, [640 - player_text.get_width()//2, 260])
                screen.blit(score_text1, [640 - score_text1.get_width()//2, 320])
                screen.blit(score_text2, [640 - score_text2.get_width()//2, 380])

            if result[0] == "multi_classic_downstack":
                #checks which player has more garbage left
                if result[1][0] < result[1][1]:
                    player_text = ct_font.render("Player 1 Wins", True, WHITE)
                if result[1][0] > result[1][1]:
                    player_text = ct_font.render("Player 2 Wins", True, WHITE)
                if result[1][0] == result[1][1]:
                    player_text = ct_font.render("Draw", True, WHITE)
                
                #displays the stats for the game
                score_text1 = ct_font.render("Player 1 garbage lines remaning: "+str(result[1][0]), True, WHITE)
                score_text2 = ct_font.render("Player 2 garbage lines remaning: "+str(result[1][1]), True, WHITE)
                screen.blit(player_text, [640 - player_text.get_width()//2, 260])
                screen.blit(score_text1, [640 - score_text1.get_width()//2, 320])
                screen.blit(score_text2, [640 - score_text2.get_width()//2, 380])

            if result[0] == "single_modern_zen":
                score_text = mt_font_big.render("Practice Finished", True, WHITE)
                screen.blit(score_text, [640 - score_text.get_width()//2, 360])

            if result[0] == "single_modern_sprint":
                lines_text = mt_font_big.render("Lines cleared: "+str(result[2]), True, WHITE)
                score_text = mt_font_big.render("Time: "+str(result[1]), True, WHITE)
                screen.blit(lines_text, [640 - lines_text.get_width()//2, 300])
                screen.blit(score_text, [640 - score_text.get_width()//2, 360])

            if result[0] == "multi_modern_normal":
                if result[1] == "draw":
                    score_text = mt_font_big.render("Draw", True, WHITE)                
                if result[1] == "player_1":
                    score_text = mt_font_big.render("Player 1 wins", True, WHITE)       
                if result[1] == "player_2":
                    score_text = mt_font_big.render("Player 2 wins", True, WHITE)    
                
                screen.blit(score_text, [640 - score_text.get_width()//2, 360])

            if result[0] == "multi_modern_sprint":
                if result[3] == "player_1":
                    player_text = mt_font_big.render("Player 1 wins", True, WHITE)     
                if result[3] == "player_2":
                    player_text = mt_font_big.render("Player 2 wins", True, WHITE)
                if result[3] == "draw":
                    player_text = mt_font_big.render("Draw", True, WHITE)
        
                lines_text1 = mt_font_big.render("Player 1 Lines cleared: "+str(result[4]), True, WHITE)
                lines_text2 = mt_font_big.render("Player 2 cleared: "+str(result[5]), True, WHITE)
                score_text1 = mt_font_big.render("Player 1 time: "+str(result[1]), True, WHITE)
                score_text2 = mt_font_big.render("Player 2 time: "+str(result[2]), True, WHITE)
                screen.blit(player_text, [640 - player_text.get_width()//2, 140])
                screen.blit(score_text1, [640 - score_text1.get_width()//2, 200])
                screen.blit(lines_text1, [640 - lines_text1.get_width()//2, 260])
                screen.blit(score_text2, [640 - score_text2.get_width()//2, 320])
                screen.blit(lines_text2, [640 - lines_text2.get_width()//2, 380])               

            exit_button.draw_button()
            buttons = [exit_button]

            if next_menu_list[0] == True:
                return 0, [0]

        #title screen menu page
        if menu_page == 0:
            
            #adds background to screen, and to reset screen each time new menu page chosen
            screen.blit(menu_bg, (0,0))

            #instantiates buttons, drwas buttons and checks button states
            play_classic = Button("ct", "classic", 280, 400, screen)
            play_classic.draw_button()
            classic_controls = Button("ct", "controls", 280, 600, screen)
            classic_controls.draw_button()
            play_modern = Button("mt", "modern", 800, 400, screen)
            play_modern.draw_button()
            modern_controls =  Button("mt", "controls", 800, 600, screen)
            modern_controls.draw_button()
            buttons = [play_classic,play_modern,classic_controls,modern_controls]

            #menu pages advance based on buttons pressed
            if next_menu_list[0] == True:
                pages_stack.append(menu_page)
                return 1, pages_stack
            
            if next_menu_list[1] == True:
                pages_stack.append(menu_page)
                return 6, pages_stack

            if next_menu_list[2] == True:
                pages_stack.append(menu_page)
                return 9, pages_stack

            if next_menu_list[3] == True:
                pages_stack.append(menu_page)
                return 12, pages_stack

        #classic tetris player number menu page
        if menu_page == 1:

            screen.blit(classic_tetris_bg, (0,0))

            singleplayer = Button("ct", "singleplayer", 280, 400, screen)
            singleplayer.draw_button()
            multiplayer = Button("ct", "multiplayer", 800, 400, screen)
            multiplayer.draw_button()
            buttons = [singleplayer, multiplayer]

            if next_menu_list[0] == True:
                pages_stack.append(menu_page)
                return 2, pages_stack
            
            if next_menu_list[1] == True:
                pages_stack.append(menu_page)
                return 4, pages_stack

        #classic tetris single player mode menu page
        if menu_page == 2:
            
            screen.blit(classic_tetris_bg, (0,0))

            play_normal = Button("ct", "normal", 280, 400, screen)
            play_normal.draw_button()
            play_downstack = Button("ct", "downstack", 800, 400, screen)
            play_downstack.draw_button()
            buttons = [play_normal,play_downstack]

            if next_menu_list[0] == True:
                pages_stack.append(menu_page)
                return 3, pages_stack
            
            if next_menu_list[1] == True:
                result = play("single_classic_downstack", classic_single_controls, None, screen, clock)
                return -1, [0]

        #classic tetris single player normal level page
        if menu_page == 3:

            screen.blit(classic_tetris_bg, (0,0))

            level_text = ct_font.render(str(start_level), True, WHITE)
            screen.blit(level_text, [640 - level_text.get_width()//2, 400])

            up_button = Button("ct", ">", 760, 400, screen)
            #only display up button if the level is less than 19
            if start_level < 19:
                up_button.draw_button()
            down_button = Button("ct", "<", 320, 400, screen)
            #only display down button if level is greater than 0
            if start_level > 0:
                down_button.draw_button()
            start_game = Button("ct", "play", 540, 540, screen)
            start_game.draw_button()
            buttons = [start_game]

            if next_menu_list[0] == True:
                result = play("single_classic_normal", classic_single_controls, start_level, screen, clock)
                return -1, [0]

            if up_level == True:
                up_level = False
                start_level += 1

            if down_level == True:
                down_level = False
                start_level -= 1

        #classic tetris multi player mode menu page
        if menu_page == 4:

            screen.blit(classic_tetris_bg, (0,0))

            play_normal = Button("ct", "normal", 280, 400, screen)
            play_normal.draw_button()
            play_downstack = Button("ct", "downstack", 800, 400, screen)
            play_downstack.draw_button()
            buttons = [play_normal,play_downstack]

            if next_menu_list[0] == True:
                pages_stack.append(menu_page)
                return 5, pages_stack
            
            if next_menu_list[1] == True:
                result = play("multi_classic_downstack", classic_multi_controls, None, screen, clock)
                return -1, [0]

        #classic tetris multi player normal level page
        if menu_page == 5:

            screen.blit(classic_tetris_bg, (0,0))

            level_text = ct_font.render(str(start_level), True, WHITE)
            screen.blit(level_text, [640 - level_text.get_width()//2, 400])

            up_button = Button("ct", ">", 760, 400, screen)
            if start_level < 19:
                up_button.draw_button()
            down_button = Button("ct", "<", 320, 400, screen)
            if start_level > 0:
                down_button.draw_button()
            start_game = Button("ct", "play", 540, 540, screen)
            start_game.draw_button()
            buttons = [start_game]

            if next_menu_list[0] == True:
                result = play("multi_classic_normal", classic_multi_controls, start_level, screen, clock)
                return -1, [0]

            if up_level == True:
                up_level = False
                start_level += 1

            if down_level == True:
                down_level = False
                start_level -= 1

        #modern tetris player number menu page
        if menu_page == 6:
                
            screen.blit(modern_tetris_bg, (0,0))

            singleplayer = Button("mt", "singleplayer", 280, 400, screen)
            singleplayer.draw_button()
            multiplayer = Button("mt", "multiplayer", 800, 400, screen)
            multiplayer.draw_button()
            buttons = [singleplayer, multiplayer]

            if next_menu_list[0] == True:
                pages_stack.append(menu_page)
                return 7, pages_stack
            
            if next_menu_list[1] == True:
                pages_stack.append(menu_page)
                return 8, pages_stack

        #modern tetris single player mode menu page
        if menu_page == 7:

            screen.blit(modern_tetris_bg, (0,0))

            play_zen = Button("mt", "zen", 280, 400, screen)
            play_zen.draw_button()
            play_sprint = Button("mt", "sprint", 800, 400, screen)
            play_sprint.draw_button()
            buttons = [play_zen, play_sprint]

            if next_menu_list[0] == True:
                result = play("single_modern_zen", modern_single_controls, None, screen, clock)
                return -1, [0]
            
            if next_menu_list[1] == True:
                result = play("single_modern_sprint", modern_single_controls, None, screen, clock)
                return -1, [0]

        #modern tetris multi player mode menu page
        if menu_page == 8:

            screen.blit(modern_tetris_bg, (0,0))

            play_zen = Button("mt", "normal", 280, 400, screen)
            play_zen.draw_button()
            play_sprint = Button("mt", "sprint", 800, 400, screen)
            play_sprint.draw_button()
            buttons = [play_zen, play_sprint]

            if next_menu_list[0] == True:
                result = play("multi_modern_normal", modern_multi_controls, None, screen, clock)
                return -1, [0]
            
            if next_menu_list[1] == True:
                result = play("multi_modern_sprint", modern_multi_controls, None, screen, clock)
                return -1, [0]

        #controls page for classic
        if menu_page == 9:
            screen.blit(classic_tetris_bg, (0,0))

            singleplayer = Button("ct", "singleplayer", 280, 400, screen)
            singleplayer.draw_button()
            multiplayer = Button("ct", "multiplayer", 800, 400, screen)
            multiplayer.draw_button()
            buttons = [singleplayer, multiplayer]

            if next_menu_list[0] == True:
                pages_stack.append(menu_page)
                return 10, pages_stack
            
            if next_menu_list[1] == True:                
                pages_stack.append(menu_page)
                return 11, pages_stack

        #controls page for classic single
        if menu_page == 10:
            screen.blit(classic_tetris_bg, (0,0))

            for i in range(0,5):
                screen.blit(ct_texts[i],[100,100*(i+1)])

            left = Button("ct_small", pygame.key.name(classic_single_controls["left"]),400,100, screen)
            left.draw_button()
            right = Button("ct_small", pygame.key.name(classic_single_controls["right"]),400,200, screen)
            right.draw_button()
            rotate_cw = Button("ct_small", pygame.key.name(classic_single_controls["rotate_cw"]),400,300, screen)
            rotate_cw.draw_button()
            rotate_acw = Button("ct_small", pygame.key.name(classic_single_controls["rotate_acw"]),400,400, screen)
            rotate_acw.draw_button()
            soft_drop = Button("ct_small", pygame.key.name(classic_single_controls["soft_drop"]),400,500, screen)
            soft_drop.draw_button()

            buttons = [left,right,rotate_cw,rotate_acw,soft_drop]

            for i in range(0,5):
                if controls_buttons1[i] == True:
                    controls_buttons1[i] = False
                    
                    #waits until the user presses a key
                    new_key = wait_keypress(menu_page)

                    #do nothing if the escape key was pressed, otherwise update the dictionary
                    if new_key == False:
                        pass
                    else:
                        classic_single_controls[ct_controls_refs[i]] = new_key 


        #controls page for classic multi
        if menu_page == 11:
            screen.blit(classic_tetris_bg, (0,0))

            for i in range(0,5):
                screen.blit(ct_texts[i],[100,100*(i+1)])
                screen.blit(ct_texts[i],[700,100*(i+1)])

            left1 = Button("ct_small", pygame.key.name(classic_multi_controls["p1_left"]),400,100, screen)
            left1.draw_button()
            right1 = Button("ct_small", pygame.key.name(classic_multi_controls["p1_right"]),400,200, screen)
            right1.draw_button()
            rotate_cw1 = Button("ct_small", pygame.key.name(classic_multi_controls["p1_rotate_cw"]),400,300, screen)
            rotate_cw1.draw_button()
            rotate_acw1 = Button("ct_small", pygame.key.name(classic_multi_controls["p1_rotate_acw"]),400,400, screen)
            rotate_acw1.draw_button()
            soft_drop1 = Button("ct_small", pygame.key.name(classic_multi_controls["p1_soft_drop"]),400,500, screen)
            soft_drop1.draw_button()

            left2 = Button("ct_small", pygame.key.name(classic_multi_controls["p2_left"]),1000,100, screen)
            left2.draw_button()
            right2 = Button("ct_small", pygame.key.name(classic_multi_controls["p2_right"]),1000,200, screen)
            right2.draw_button()
            rotate_cw2 = Button("ct_small", pygame.key.name(classic_multi_controls["p2_rotate_cw"]),1000,300, screen)
            rotate_cw2.draw_button()
            rotate_acw2 = Button("ct_small", pygame.key.name(classic_multi_controls["p2_rotate_acw"]),1000,400, screen)
            rotate_acw2.draw_button()
            soft_drop2 = Button("ct_small", pygame.key.name(classic_multi_controls["p2_soft_drop"]),1000,500, screen)
            soft_drop2.draw_button()

            buttons1 = [
                left1,right1,rotate_cw1,rotate_acw1,soft_drop1,
            ]
            buttons2 = [
                left2,right2,rotate_cw2,rotate_acw2,soft_drop2
            ]

            for i in range(0,5):
                if controls_buttons1[i] == True:
                    controls_buttons1[i] = False
                    new_key = wait_keypress(menu_page)
                    if new_key == False:
                        pass
                    else:
                        classic_multi_controls[ct_controls_p1_refs[i]] = new_key

                if controls_buttons2[i] == True:
                    controls_buttons2[i] = False
                    new_key = wait_keypress(menu_page)
                    if new_key == False:
                        pass
                    else:
                        classic_multi_controls[ct_controls_p2_refs[i]] = new_key                       

        #controls page for modern
        if menu_page == 12:

            screen.blit(modern_tetris_bg, (0,0))

            singleplayer = Button("mt", "singleplayer", 280, 400, screen)
            singleplayer.draw_button()
            multiplayer = Button("mt", "multiplayer", 800, 400, screen)
            multiplayer.draw_button()
            buttons = [singleplayer, multiplayer]

            if next_menu_list[0] == True:
                pages_stack.append(menu_page)
                return 13, pages_stack
            
            if next_menu_list[1] == True:
                pages_stack.append(menu_page)
                return 14, pages_stack

        #controls page for modern single
        if menu_page == 13:
            screen.blit(modern_tetris_bg, (0,0))

            for i in range(0,7):
                screen.blit(mt_texts[i],[100,75*(i+1)])


            left = Button("mt_small", pygame.key.name(modern_single_controls["left"]),400,75, screen)
            left.draw_button()
            right = Button("mt_small", pygame.key.name(modern_single_controls["right"]),400,150, screen)
            right.draw_button()
            rotate_cw = Button("mt_small", pygame.key.name(modern_single_controls["rotate_cw"]),400,225, screen)
            rotate_cw.draw_button()
            rotate_acw = Button("mt_small", pygame.key.name(modern_single_controls["rotate_acw"]),400,300, screen)
            rotate_acw.draw_button()
            soft_drop = Button("mt_small", pygame.key.name(modern_single_controls["soft_drop"]),400,375, screen)
            soft_drop.draw_button()
            hard_drop = Button("mt_small", pygame.key.name(modern_single_controls["hard_drop"]),400,450, screen)
            hard_drop.draw_button()
            hold = Button("mt_small", pygame.key.name(modern_single_controls["hold"]),400,525, screen)
            hold.draw_button()

            buttons = [left,right,rotate_cw,rotate_acw,soft_drop,hard_drop,hold]

            for i in range(0,7):
                if controls_buttons1[i] == True:
                    controls_buttons1[i] = False
                    new_key = wait_keypress(menu_page)
                    if new_key == False:
                        pass
                    else:
                        modern_single_controls[mt_controls_refs[i]] = new_key 

        #controls page for modern multi
        if menu_page == 14:
            screen.blit(modern_tetris_bg, (0,0))

            #texts that label the buttons are added
            for i in range(0,7):
                screen.blit(mt_texts[i],[100,75*(i+1)])
                screen.blit(mt_texts[i],[700,75*(i+1)])

            #creating and drawing buttons for changing player 1 controls
            left1 = Button("mt_small", pygame.key.name(modern_multi_controls["p1_left"]),400,75, screen)
            left1.draw_button()
            right1 = Button("mt_small", pygame.key.name(modern_multi_controls["p1_right"]),400,150, screen)
            right1.draw_button()
            rotate_cw1 = Button("mt_small", pygame.key.name(modern_multi_controls["p1_rotate_cw"]),400,225, screen)
            rotate_cw1.draw_button()
            rotate_acw1 = Button("mt_small", pygame.key.name(modern_multi_controls["p1_rotate_acw"]),400,300, screen)
            rotate_acw1.draw_button()
            soft_drop1 = Button("mt_small", pygame.key.name(modern_multi_controls["p1_soft_drop"]),400,375, screen)
            soft_drop1.draw_button()
            hard_drop1 = Button("mt_small", pygame.key.name(modern_multi_controls["p1_hard_drop"]),400,450, screen)
            hard_drop1.draw_button()
            hold1 = Button("mt_small", pygame.key.name(modern_multi_controls["p1_hold"]),400,525, screen)
            hold1.draw_button()

            #creating and drawing buttons for changing player 2 controls
            left2 = Button("mt_small", pygame.key.name(modern_multi_controls["p2_left"]),1000,75, screen)
            left2.draw_button()
            right2 = Button("mt_small", pygame.key.name(modern_multi_controls["p2_right"]),1000,150, screen)
            right2.draw_button()
            rotate_cw2 = Button("mt_small", pygame.key.name(modern_multi_controls["p2_rotate_cw"]),1000,225, screen)
            rotate_cw2.draw_button()
            rotate_acw2 = Button("mt_small", pygame.key.name(modern_multi_controls["p2_rotate_acw"]),1000,300, screen)
            rotate_acw2.draw_button()
            soft_drop2 = Button("mt_small", pygame.key.name(modern_multi_controls["p2_soft_drop"]),1000,375, screen)
            soft_drop2.draw_button()
            hard_drop2 = Button("mt_small", pygame.key.name(modern_multi_controls["p2_hard_drop"]),1000,450, screen)
            hard_drop2.draw_button()
            hold2 = Button("mt_small", pygame.key.name(modern_multi_controls["p2_hold"]),1000,525, screen)
            hold2.draw_button()

            #arrays containing buttons on all pages
            buttons1 = [
                left1,right1,rotate_cw1,rotate_acw1,soft_drop1,hard_drop1,hold1
            ]
            buttons2 = [
                left2,right2,rotate_cw2,rotate_acw2,soft_drop2,hard_drop2,hold2
            ]

            #cycles through each button
            for i in range(0,7):
                #for player 1 if a control is to be changed
                if controls_buttons1[i] == True:
                    #resets the button flag
                    controls_buttons1[i] = False
                    #calls function awaiting keypress
                    new_key = wait_keypress(menu_page)
                    #does nothing if ESC pressed
                    if new_key == False:
                        pass
                    #changes the key if a different key is pressed
                    else:
                        modern_multi_controls[mt_controls_p1_refs[i]] = new_key

                #for player 2 if a control is to be changed
                if controls_buttons2[i] == True:
                    controls_buttons2[i] = False
                    new_key = wait_keypress(menu_page)
                    if new_key == False:
                        pass
                    else:
                        modern_multi_controls[mt_controls_p2_refs[i]] = new_key

        #drawing the back button on every page except for the start oage
        if menu_page > 0:
            #classic tetris style button for classic tetris pages
            if menu_page in [1,2,3,4,5,9,10,11]:
                back_button = Button("ct", "Back", 20, 600, screen)
                back_button.draw_button()
            #modern tetris style button for modern tetris pages
            if menu_page in [6,7,8,12,13,14]:
                back_button = Button("mt", "Back", 20, 600, screen)
                back_button.draw_button()

            #checks if clicked
            if back_menu == True:
                #back page set to top page of stack
                #stack popped and returns the previous page
                back_page = pages_stack[len(pages_stack)-1]
                pages_stack.pop()
                return back_page, pages_stack

        pygame.display.flip()       
        #events handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            #checks for clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if menu_page in [-1,0,1,2,3,4,5,6,7,8,9,12]:
                        for pages in range(0,len(buttons)):
                        #changes flag of page in the array if a button is clciked
                            if len(buttons)-1 >= pages:
                                next_menu_list[pages] = buttons[pages].click_button()

                    #checks for back button click on all pages except the title page
                    #which shouldn't have a back button
                    if menu_page > 0:
                        #returns result of back button being clicked
                        #present on all pages except title screen
                        back_menu = back_button.click_button()

                    #if on a level selection screen, only allows up and down presses to be
                    #registered if between a range
                    if menu_page in [3,5]:
                        if start_level < 19:
                            up_level = up_button.click_button()
                        if start_level > 0:
                            down_level = down_button.click_button()

                    if menu_page in [10,13]:
                        for pages in range(0,len(buttons)):
                            if len(buttons)-1 >= pages:
                                controls_buttons1[pages] = buttons[pages].click_button()

                    if menu_page in [11,14]:
                        for pages in range(0,len(buttons1)):
                            if len(buttons1)-1 >= pages:
                                controls_buttons1[pages] = buttons1[pages].click_button()
                        for pages in range(0,len(buttons2)):
                            if len(buttons2)-1 >= pages:
                                controls_buttons2[pages] = buttons2[pages].click_button()
