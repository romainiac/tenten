from .Color import Color

class ColorSetting:

    def __init__(self, primary: Color, secondary: Color, title: Color):
        self.primary = primary
        self.secondary = secondary
        self.title = title