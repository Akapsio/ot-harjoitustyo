from ui.ui import UI
from ui.button import Button
import pygame

class Digigame:
    '''Class for running the game itself'''
    def __init__(self):
        '''The class constructor'''
        self.initial_view = False
        self.user_view = False
        self.view = UI()
        self.initialize()
        users = []
        words = []

    def initialize(self):
        self.draw_initial()
        self.initial_view = True

    def check_state(self):
        pass

    def draw_initial(self):
        self.user_view = False
        self.view.show_initial_view()
        self.initial_view = True

    def draw_user(self):
        self.initial_view = False
        self.view._show_user_view()
        self.user_view = True

    def clicked_on_add_user(self):
        pass

    def update_text(self):
        clock = pygame.time.Clock()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                elif len(text) >= 16:
                    continue
                else:
                    user_text += event.unicode
                    self.view._show_user_view()
                clock.tick(60)
        return

    def handle_events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if self.initial_view == True:
                    if event.key == pygame.K_SPACE:
                        self.draw_user()
                if self.user_view == True:
                    if event.key == pygame.K_ESCAPE:
                        self.draw_initial()
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                if self.user_view == True:
                    if position[0] >= 30 and position[0] <= 70:
                        # Check to see if cursor over Textbox
                        if position[1] >= 80 and position[1] <= 110:
                            self.clicked_on_add_user()
                        # Check to see if cursor over textfield1
                        if position[1] >= 50 and position[1] <= 70:
                            self.update_text()
