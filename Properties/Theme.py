from enum import Enum
from .Color import Color
from .ColorSetting import ColorSetting
from .FontSetting import FontSetting
from abc import ABC
import pygame

class Theme(ABC):
    pass

class DarkTheme(Theme):

    def __init__(self):
        self.color_setting = ColorSetting(primary=Color.DARK_BLUE, 
                                          secondary=Color.BLACK,
                                          title=Color.WHITE)
        self.font_setting = FontSetting(primary=pygame.font.SysFont('timesnewroman',  30))
        
