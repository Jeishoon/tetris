import pygame

from pause import *

#dictionaries containing controls for games
classic_single_controls = {
    "left": pygame.K_LEFT,
    "right": pygame.K_RIGHT,
    "rotate_cw": pygame.K_x,
    "rotate_acw": pygame.K_z,
    "soft_drop": pygame.K_DOWN
}

classic_multi_controls = {
    "p1_left": pygame.K_a,
    "p1_right": pygame.K_d,
    "p1_rotate_cw": pygame.K_c,
    "p1_rotate_acw": pygame.K_x,
    "p1_soft_drop": pygame.K_s,

    "p2_left": pygame.K_LEFT,
    "p2_right": pygame.K_RIGHT,
    "p2_rotate_cw": pygame.K_PERIOD,
    "p2_rotate_acw": pygame.K_COMMA,
    "p2_soft_drop": pygame.K_DOWN
}

modern_single_controls = {
    "left": pygame.K_LEFT,
    "right": pygame.K_RIGHT,
    "rotate_cw": pygame.K_x,
    "rotate_acw": pygame.K_z,
    "soft_drop": pygame.K_DOWN,
    "hard_drop": pygame.K_SPACE,
    "hold": pygame.K_LSHIFT
}

modern_multi_controls = {
    "p1_left": pygame.K_a,
    "p1_right": pygame.K_d,
    "p1_rotate_cw": pygame.K_c,
    "p1_rotate_acw": pygame.K_x,
    "p1_soft_drop": pygame.K_s,
    "p1_hard_drop": pygame.K_v,
    "p1_hold": pygame.K_LSHIFT,
    
    "p2_left": pygame.K_LEFT,
    "p2_right": pygame.K_RIGHT,
    "p2_rotate_cw": pygame.K_PERIOD,
    "p2_rotate_acw": pygame.K_COMMA,
    "p2_soft_drop": pygame.K_DOWN,
    "p2_hard_drop": pygame.K_SLASH,
    "p2_hold": pygame.K_RSHIFT
}

#loads controls into game based on game mode
def load_controls(mode,game,controls,screen):

    #gives user option to exit pygame across all game modes
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
        #controls for single player classic tetris
        if (mode == "single_classic_normal" or \
            mode == "single_classic_downstack") and \
            game.state == "playing":
            
            if event.type == pygame.KEYDOWN:
                if event.key == controls["rotate_acw"]:
                    game.rotate(-1)
                if event.key == controls["rotate_cw"]:
                    game.rotate(1)
                if event.key == controls["soft_drop"]:
                    game.fast_down = True
                if event.key == controls["left"]:
                    game.move_lr(-1)
                    game.fast_left = True
                if event.key == controls["right"]:
                    game.move_lr(1)
                    game.fast_right = True

            #detects when the key is no longer being pressed
            #to stop holding down/das movement
            if event.type == pygame.KEYUP:
                if event.key == controls["soft_drop"]:
                    game.fast_down = False   
                if event.key == controls["left"]:
                    game.fast_left = False
                if event.key == controls["right"]:
                    game.fast_right = False     
        
        #controls for single palyer modern tetris
        if (mode == "single_modern_zen" or \
            mode == "single_modern_sprint") and \
                game.state == "playing":
            
            if event.type == pygame.KEYDOWN:
                if event.key == controls["rotate_acw"]:
                    game.rotate(-1)
                if event.key == controls["rotate_cw"]:
                    game.rotate(1)
                if event.key == controls["soft_drop"]:
                    game.fast_down = True
                if event.key == controls["left"]:
                    game.move_lr(-1)
                    game.fast_left = True
                if event.key == controls["right"]:
                    game.move_lr(1)
                    game.fast_right = True
                if event.key == controls["hard_drop"]:
                    game.hard_drop()
                if event.key == controls["hold"]:
                    game.hold()

            if event.type == pygame.KEYUP:
                if event.key == controls["soft_drop"]:
                    game.fast_down = False   
                if event.key == controls["left"]:
                    game.fast_left = False
                if event.key == controls["right"]:
                    game.fast_right = False     

        #controls for multiplayer classic tetris
        if mode == "multi_classic_normal" or \
            mode == "multi_classic_downstack":
        
            if event.type == pygame.KEYDOWN:
                if game[0].state == "playing":
                    if event.key == controls["p1_rotate_acw"]:
                        game[0].rotate(-1)
                    if event.key == controls["p1_rotate_cw"]:
                        game[0].rotate(1)
                    if event.key == controls["p1_soft_drop"]:
                        game[0].fast_down = True
                    if event.key == controls["p1_left"]:
                        game[0].move_lr(-1)
                        game[0].fast_left = True
                    if event.key == controls["p1_right"]:
                        game[0].move_lr(1)
                        game[0].fast_right = True

                if game[1].state == "playing":
                    if event.key == controls["p2_rotate_acw"]:
                        game[1].rotate(-1)
                    if event.key == controls["p2_rotate_cw"]:
                        game[1].rotate(1)
                    if event.key == controls["p2_soft_drop"]:
                        game[1].fast_down = True
                    if event.key == controls["p2_left"]:
                        game[1].move_lr(-1)
                        game[1].fast_left = True
                    if event.key == controls["p2_right"]:
                        game[1].move_lr(1)
                        game[1].fast_right = True

            if event.type == pygame.KEYUP:
                if game[0].state == "playing":
                    if event.key == controls["p1_soft_drop"]:
                        game[0].fast_down = False
                    if event.key == controls["p1_left"]:
                        game[0].fast_left = False
                    if event.key == controls["p1_right"]:
                        game[0].fast_right = False

                if game[1].state == "playing":
                    if event.key == controls["p2_soft_drop"]:
                        game[1].fast_down = False
                    if event.key == controls["p2_left"]:
                        game[1].fast_left = False
                    if event.key == controls["p2_right"]:
                        game[1].fast_right = False

        #controls for multiplayer modern tetris
        if mode == "multi_modern_normal"or \
            mode == "multi_modern_sprint":
        
            if event.type == pygame.KEYDOWN:
                if game[0].state == "playing":
                    if event.key == controls["p1_rotate_acw"]:
                        game[0].rotate(-1)
                    if event.key == controls["p1_rotate_cw"]:
                        game[0].rotate(1)
                    if event.key == controls["p1_soft_drop"]:
                        game[0].fast_down = True
                    if event.key == controls["p1_left"]:
                        game[0].move_lr(-1)
                        game[0].fast_left = True
                    if event.key == controls["p1_right"]:
                        game[0].move_lr(1)
                        game[0].fast_right = True
                    if event.key == controls["p1_hold"]:
                        game[0].hold()
                    if event.key == controls["p1_hard_drop"]:
                        game[0].hard_drop()

                if game[1].state == "playing":
                    if event.key == controls["p2_rotate_acw"]:
                        game[1].rotate(-1)
                    if event.key == controls["p2_rotate_cw"]:
                        game[1].rotate(1)
                    if event.key == controls["p2_soft_drop"]:
                        game[1].fast_down = True
                    if event.key == controls["p2_left"]:
                        game[1].move_lr(-1)
                        game[1].fast_left = True
                    if event.key == controls["p2_right"]:
                        game[1].move_lr(1)
                        game[1].fast_right = True
                    if event.key == controls["p2_hold"]:
                        game[1].hold()
                    if event.key == controls["p2_hard_drop"]:
                        game[1].hard_drop()

            if event.type == pygame.KEYUP:
                if game[0].state == "playing":
                    if event.key == controls["p1_soft_drop"]:
                        game[0].fast_down = False
                    if event.key == controls["p1_left"]:
                        game[0].fast_left = False
                    if event.key == controls["p1_right"]:
                        game[0].fast_right = False

                if game[1].state == "playing":
                    if event.key == controls["p2_soft_drop"]:
                        game[1].fast_down = False
                    if event.key == controls["p2_left"]:
                        game[1].fast_left = False
                    if event.key == controls["p2_right"]:
                        game[1].fast_right = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pause(mode,game,screen)
