import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.dropdown import DropDown
from kivy.clock import Clock

kivy.require('2.1.0')

# Configuración de la ventana
Window.size = (400, 600)
Window.clearcolor = (1, 1, 1, 1)  # Fondo blanco

class HoverBehavior(ButtonBehavior):
    def __init__(self, **kwargs):
        super(HoverBehavior, self).__init__(**kwargs)
        self.bind(on_enter=self.on_enter)
        self.bind(on_leave=self.on_leave)

    def on_enter(self, *args):
        self.color = (0, 0, 1, 1)

    def on_leave(self, *args):
        self.color = (1, 1, 1, 1)

# probando
