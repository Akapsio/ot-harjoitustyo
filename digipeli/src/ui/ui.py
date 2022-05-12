from ui.initial_view import InitialView
from ui.user_view import UserView
import pygame

class UI:
    def __init__(self):
        '''UI constructor'''  
        self._current_view = None

    def get_view(self):
        return self._current_view

    def start(self):
        self._show_initial_view()

    def _show_initial_view(self):
        self._hide_current_view()
        self._current_view = InitialView()

    def _show_user_view(self):
        self._hide_current_view()
        self._current_view = UserView()

    def _hide_current_view(self):
        if self._current_view != None:
            self._current_view = None
