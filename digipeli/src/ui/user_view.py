from tokenize import String
import pygame
from ui.button import Button

class UserView:
    def __init__(self):
        ''''''
        self.create_user_button = Button((255, 255, 255), 30, 80, 40, 25, text = 'Ok')
        self.create_user_textfield = Button((255, 255, 255), 30, 50, 40, 25, text = '')
        self._initialize()

    def _initialize(self, user_text = ""):

        pygame.init()
        screen = pygame.display.set_mode((640, 480))
        screen.fill((255, 255, 255))
        font = pygame.font.SysFont("Calibri", 16)
        text = font.render("Luo uusi käyttäjä", True, (0, 0, 0))
        screen.blit(text, (30, 20))

        self.create_user_textfield.draw(screen, (0, 0, 0))
        self.create_user_button.draw(screen, (0, 0, 0))

        pygame.display.flip()

    def add_text(self, user_text: str):
        text_surface = pygame.font.SysFont("Calibri", 16).render(user_text, True, (255, 255, 255))

