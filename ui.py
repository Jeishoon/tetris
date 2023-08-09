from resources import *

#draws the static UI elements
#such as the background and frames for the dynamic UI elements
def draw_ui(mode,game,screen):
    if mode == "single_classic_normal" or \
        mode == "single_classic_downstack":

        screen.blit(classic_tetris_bg, (0,0)) # BACKGROUND
        screen.blit(classic_tetris_border1, [game.x - 14, game.y - 10])  # MAIN GAME BORDER
        screen.blit(classic_tetris_border3, [game.x + 332, game.y - 4]) # SCORE BORDER
        screen.blit(classic_tetris_border2, [game.x + 332, game.y + 176]) # NEXT PIECE BORDER
        screen.blit(classic_tetris_border2, [game.x + 332, game.y + 376]) # LINES CLEARED BORDER

    if mode == "multi_classic_normal"or \
        mode == "multi_classic_downstack":

        screen.blit(classic_tetris_bg, (0,0))

        for i in range(0,2):
            screen.blit(classic_tetris_border1, [game[i].x - 14, game[i].y - 10]) # MAIN GAME BORDER
            screen.blit(classic_tetris_border3, [game[i].x + 332, game[i].y - 4]) # SCORE BORDER
            screen.blit(classic_tetris_border2, [game[i].x + 332, game[i].y + 176]) # NEXT PIECE BORDER
            screen.blit(classic_tetris_border2, [game[i].x + 332, game[i].y + 376]) # LINES CLEARED BORDER
    
    if mode == "single_modern_zen" or \
        mode == "single_modern_sprint":

        screen.blit(modern_tetris_bg, (0,0))
        pygame.draw.rect(screen,WHITE,[game.x - 10, game.y - 10, 340,620]) # MAIN GAME
        pygame.draw.rect(screen,WHITE,[game.x - 160, game.y - 10, 310,130]) # HOLD PREVIEW
        pygame.draw.rect(screen,WHITE,[game.x - 10, game.y - 10, 490,530]) # PREVIEW QUEUE

        if mode == "single_modern_sprint":
            pygame.draw.rect(screen,WHITE,[game.x - 160, game.y - 10, 310,260]) # HOLD PREVIEW

    if mode == "multi_modern_normal":

        screen.blit(modern_tetris_bg, (0,0))       
        
        for i in range(0,2):
            pygame.draw.rect(screen,WHITE,[game[i].x - 10, game[i].y +590, 340,620]) # MAIN GAME
            pygame.draw.rect(screen,WHITE,[game[i].x - 160, game[i].y +590, 310,130]) # HOLD PREVIEW
            pygame.draw.rect(screen,WHITE,[game[i].x - 10, game[i].y +590, 490,530]) # PREVIEW QUEUE

    if mode == "multi_modern_sprint":

        screen.blit(modern_tetris_bg, (0,0)) 
        
        for i in range(0,2):
            pygame.draw.rect(screen,WHITE,[game[i].x - 10, game[i].y -10, 340,620]) # MAIN GAME
            pygame.draw.rect(screen,WHITE,[game[i].x - 160, game[i].y -10, 310,130]) # HOLD PREVIEW
            pygame.draw.rect(screen,WHITE,[game[i].x - 10, game[i].y -10, 490,530]) # PREVIEW QUEUE
            pygame.draw.rect(screen,WHITE,[game[i].x - 160, game[i].y - 10, 310,260]) # HOLD PREVIEW