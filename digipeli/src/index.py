import pygame
from digigame import Digigame

'''Class for initializing the game'''

class Index:
    def __init__(self):
        self.digigame = Digigame()

    def mainloop(self):
        '''Initiates the main loop'''

        while True:
            self.digigame.handle_events()

if __name__ == '__main__':
    index = Index()
    index.mainloop()
