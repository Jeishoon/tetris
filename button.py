from resources import *

#class for buttons used in menus
class Button():

    #initialised/styled dependent on game mode represented/used
    def __init__(self, gm, text, x, y, screen):
        #uses classic tetris images
        if gm == "ct":
            self.image = ct_button
            self.click_image = ct_button_click
            self.hover_image = ct_button_hover
            self.font = ct_font_small.render(text, True, BLACK)
        #uses modern tetris images
        if gm == "mt":
            self.image = mt_button
            self.click_image = mt_button_click
            self.hover_image = mt_button_hover
            self.font = mt_font.render(text, True, WHITE)
        #smaller images used for controls screens
        if gm == "ct_small":
            self.image = ct_button_controls
            self.click_image = ct_button_controls_click
            self.hover_image = ct_button_controls_hover
            self.font = ct_font_small.render(text, True, BLACK)
        if gm == "mt_small":
            self.image = mt_button_controls
            self.click_image = mt_button_controls_click
            self.hover_image = mt_button_controls_hover
            self.font = mt_font.render(text, True, WHITE)
        self.x = x
        self.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.screen = screen

    #draws the button to the screen
    def draw_button(self):

        cursor = pygame.mouse.get_pos()
        #if the button is being hovered
        if self.x + self.width > cursor[0] > self.x and \
            self.y + self.height > cursor[1] > self.y:
            self.screen.blit(self.hover_image, (self.x, self.y))


        #if not being hovered
        else:
            self.screen.blit(self.image, (self.x, self.y))

        #adds text to the button
        self.screen.blit(self.font, [self.x + self.width/2 - self.font.get_width()//2, 
                                self.y + self.height/2 - self.font.get_height()//2])

    #handles button clicks
    def click_button(self):

        cursor = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        #checks if the mouse is inside of the button
        if self.x + self.width > cursor[0] > self.x and \
            self.y + self.height > cursor[1] > self.y:
            #checks for a click and returns true if detected
            #returns false if not
            if click[0] == 1:
                self.screen.blit(self.click_image, (self.x,self.y))
                self.screen.blit(self.font, [self.x + self.width/2 - self.font.get_width()//2, 
                                    self.y + self.height/2 - self.font.get_height()//2])
                return True

            #resets clicked button to original appearance
            self.screen.blit(self.font, [self.x + self.width/2 - self.font.get_width()//2, 
                                    self.y + self.height/2 - self.font.get_height()//2])

            #returns false if button not clicked
            return False
        return False
