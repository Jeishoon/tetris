################################## LIBRARIES ##################################

from tetrominos import *
from game import *
from button import *
from controls import *
from menu import *

################################## PYGAME SETUP ##################################

#initialises Pygame
pygame.init()

#window/clock configuration
resolution = (1280,720)
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption("Multiplayer Tetris")
clock = pygame.time.Clock()

################################## CLASSES ##################################

################################## STANDARD TETRIS ##################################
 
################################## MAIN CLASSIC ##################################

################################## DOWNSTACK CLASSIC ##################################

################################## MAIN MDOERN ##################################

################################## GHOST PIECE METHODS ##################################

################################## MODERN SPRINT ##################################

################################## MODERN TWO PLAYER ##################################

################################## GAME/MENU FUNCTIONS ##################################

################################## MENUS ##################################

################################## MAIN PROGRAM ##################################

#running variable indicates whether program is running, used in loops
#result used for storing information about a newly finished game
running = True
result = []

def main():

    #default: shows title page with no pages in the backtracking stack, and no next page
    menu_page = 0
    next_page = None
    pages_stack = [0]

    #loops while the program is running
    while running:

        for event in pygame.event.get():
            #closes the application
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

         #if next page has no value as no button has been clicked
        if next_page == None:
            next_page,new_stack = main_menu(menu_page,pages_stack,screen,clock,running)
        
        #if a button is clicked, updates the pages stack, changes the page
        #resets the next page variable
        if next_page != None:
            menu_page = next_page
            pages_stack = new_stack
            next_page = None

main()
