import pygame

class InitialView:
    def __init__(self):
        self.initialize()
        
    def initialize(self):

        pygame.init()
        screen = pygame.display.set_mode((640, 480))
        screen.fill((255, 255, 255))
        font = pygame.font.SysFont("Calibri", 48)
        text = font.render("Digipeli", True, (0, 0, 0))
        screen.blit(text, (320 - (text.get_width()/2), 240 - (text.get_height()/2)))
        font = pygame.font.SysFont("Calibri", 16)
        text2 = font.render("Paina \"Space\" aloittaaksesi", True, (0, 0, 0))
        screen.blit(text2, (320 - (text2.get_width()/2), 300 - (text2.get_height()/2)))
        
        pygame.display.flip()
