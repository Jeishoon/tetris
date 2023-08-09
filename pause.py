import pygame

from button import *
from ui import *

#pausing the game
def pause(mode,game,screen):
    paused = True

    #darkens the screen
    pause_screen = pygame.Surface((1280,720))
    pause_screen.set_alpha(128)
    pause_screen.fill(BLACK)
    screen.blit(pause_screen,(0,0))
    pygame.display.flip()

    #styles buttons in classic tetris style
    if mode == "single_classic_normal" or \
        mode == "single_classic_downstack" or \
        mode == "multi_classic_normal" or \
        mode == "multi_classic_downstack":

        #draws text to screen
        pause_text = ct_font_pause.render("Paused", True, WHITE)
        screen.blit(pause_text, [1280/2 - pause_text.get_width()/2,
                                720/2 - pause_text.get_height()/2])

        #initialises buttons
        resume_button = Button("ct", "resume", 280, 400, screen)
        exit_button = Button("ct", "exit", 800, 400, screen)

    if mode == "single_modern_zen" or \
        mode == "single_modern_sprint" or \
        mode == "multi_modern_normal" or \
        mode == "multi_modern_sprint":

        #draws text to screen
        pause_text = mt_font_pause.render("Paused", True, WHITE)
        screen.blit(pause_text, [1280/2 - pause_text.get_width()/2,
                                720/2 - pause_text.get_height()/2])

        #initialises buttons
        resume_button = Button("mt", "resume", 280, 400, screen)
        exit_button = Button("mt", "exit", 800, 400, screen)

    #main paused loop
    while paused:

        #constantly draws the buttons and checks for clicks
        resume_button.draw_button()
        exit_button.draw_button()
        option1 = resume_button.click_button()
        option2 = exit_button.click_button()
        pygame.display.flip()

        #resume game
        if option1 == True:
            draw_ui(mode,game,screen)
            paused = False

        #exits game by changing game state to instantly over
        if option2 == True:
            if mode == "single_classic_normal" or \
            mode == "single_classic_downstack" or \
            mode == "single_modern_zen" or \
            mode == "single_modern_sprint":

                game.state = "forced_over"

            if mode == "multi_classic_normal" or \
            mode == "multi_classic_downstack" or \
            mode == "multi_modern_normal" or \
            mode == "multi_modern_sprint":

                for i in range(0,2):
                    game[i].state = "forced_over"
            
            #unpausing to end game
            paused = False
                
        for event in pygame.event.get():
            #quits the game
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            #unpauses
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    draw_ui(mode,game,screen)
                    paused = False
