import pygame
import os

pygame.init()

abs_path = os.path.dirname(__file__)
img_path = os.path.join(abs_path, "img")
font_path = os.path.join(abs_path, "fonts")

#defined button sizes
button_height = 100
button_width = 200
short_button_height = 30

os.chdir(img_path)

#background and button images for menus
menu_bg = pygame.image.load("tetris_menu_bg.png")
ct_button = pygame.image.load("ct_button.png")
mt_button = pygame.image.load("mt_button.png")
ct_button_hover = pygame.image.load("ct_button_hover.png")
mt_button_hover = pygame.image.load("mt_button_hover.png")
ct_button_click = pygame.image.load("ct_button_click.png")
mt_button_click = pygame.image.load("mt_button_click.png")
menu_bg = pygame.transform.scale(menu_bg, (1280,720))
ct_button = pygame.transform.scale(ct_button, (button_width, button_height))
mt_button = pygame.transform.scale(mt_button, (button_width, button_height))
ct_button_hover = pygame.transform.scale(ct_button_hover, (button_width, button_height))
mt_button_hover = pygame.transform.scale(mt_button_hover, (button_width, button_height))
ct_button_click = pygame.transform.scale(ct_button_click, (button_width, button_height))
mt_button_click = pygame.transform.scale(mt_button_click, (button_width, button_height))

ct_button_controls = pygame.transform.scale(ct_button, (button_width, short_button_height))
mt_button_controls = pygame.transform.scale(mt_button, (button_width, short_button_height))
ct_button_controls_hover = pygame.transform.scale(ct_button_hover, (button_width, short_button_height))
mt_button_controls_hover = pygame.transform.scale(mt_button_hover, (button_width, short_button_height))
ct_button_controls_click = pygame.transform.scale(ct_button_click, (button_width, short_button_height))
mt_button_controls_click = pygame.transform.scale(mt_button_click, (button_width, short_button_height))

#game background images
classic_tetris_bg = pygame.image.load("classic_tetris_background.jpg")
modern_tetris_bg = pygame.image.load("modern_tetris_background.jpg")
classic_tetris_bg = pygame.transform.scale(classic_tetris_bg, (1280,1280))
modern_tetris_bg = pygame.transform.scale(modern_tetris_bg, (1280,800))

#ui background images
classic_tetris_border = pygame.image.load("classic_tetris_border.png")
classic_tetris_border1 = pygame.transform.scale(classic_tetris_border, (327,622))
classic_tetris_border2 = pygame.transform.scale(classic_tetris_border, (215,167))
classic_tetris_border3 = pygame.transform.scale(classic_tetris_border, (215,137))

#classic tetris block images
ct_block_blue1 = pygame.image.load("CT_block_blue1.png") #blue white
ct_block_blue2 = pygame.image.load("CT_block_blue2.png") #dark blue
ct_block_red1 = pygame.image.load("CT_block_red1.png") #red
ct_garbage_block = pygame.image.load("CT_garbage_block.png") #grey
ct_block_blue1 = pygame.transform.scale(ct_block_blue1, (30, 30))
ct_block_blue2 = pygame.transform.scale(ct_block_blue2, (30, 30))
ct_block_red1 = pygame.transform.scale(ct_block_red1, (30, 30))
ct_garbage_block = pygame.transform.scale(ct_garbage_block, (30, 30))

#modern tetris block images
mt_block_blue = pygame.image.load("MT_block_blue.png")
mt_block_red = pygame.image.load("MT_block_red.png")
mt_block_orange = pygame.image.load("MT_block_orange.png")
mt_block_yellow = pygame.image.load("MT_block_yellow.png")
mt_block_purple = pygame.image.load("MT_block_purple.png")
mt_block_green = pygame.image.load("MT_block_green.png")
mt_block_dark_blue = pygame.image.load("MT_block_dark_blue.png")
mt_garbage_block = pygame.image.load("MT_garbage_block.png")
mt_block_blue = pygame.transform.scale(mt_block_blue, (30, 30))
mt_block_red = pygame.transform.scale(mt_block_red, (30, 30))
mt_block_orange = pygame.transform.scale(mt_block_orange, (30, 30))
mt_block_yellow = pygame.transform.scale(mt_block_yellow, (30, 30))
mt_block_purple = pygame.transform.scale(mt_block_purple, (30, 30))
mt_block_green = pygame.transform.scale(mt_block_green, (30, 30))
mt_block_dark_blue = pygame.transform.scale(mt_block_dark_blue, (30, 30))
mt_garbage_block = pygame.transform.scale(mt_garbage_block, (30, 30))

os.chdir(font_path)
#fonts
ct_font_pause = pygame.font.Font("ctfont.ttf", 40)
ct_font = pygame.font.Font("ctFont.ttf", 20)
ct_font_small = pygame.font.Font("ctFont.ttf", 15)
mt_font = pygame.font.Font("mtFont.otf", 20)
mt_font_big = pygame.font.Font("mtFont.otf", 30)
mt_font_pause = pygame.font.Font("mtFont.otf", 60)

#initial/commonly used colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
DARK_GRAY = (36,36,36)

#initial array containing tuples of colours
colours = [
(0, 0, 0), #BLACK
(51, 255, 255), #LIGHT BLUE
(255, 51, 51), #RED
(51, 255, 51), #GREEN
(51, 51, 255), #DARK BLUE
(255, 153, 51), #ORANGE
(255, 51, 255), #PINK
(255, 255, 0), #YELLOW
(169, 169, 169) #GREY
]

#array of block images for classic tetris
colours_ct = [
(0, 0, 0), #BLACK
ct_block_blue1, #I
ct_block_blue2, #Z
ct_block_red1, #S
ct_block_blue2, #J
ct_block_red1, #L
ct_block_blue1, #T
ct_block_blue1, #O
ct_garbage_block #GARBAGE
]

#array of block iamges for modern tetris
colours_mt = [
(0, 0, 0), #BLACK
mt_block_blue, #I
mt_block_red, #Z
mt_block_green, #S
mt_block_dark_blue, #J
mt_block_orange, #L
mt_block_purple, #T
mt_block_yellow, #O
mt_garbage_block #GARBAGE
]