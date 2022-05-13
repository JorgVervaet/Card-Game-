class Symbol:
    def __init__(self, color, icon):
        self.color = color
        self.icon = icon


class Card(Symbol):
    def __init__(self, color, icon, value):
        super().__init__(color, icon)
        self.values = value
    def __str__(self):    
        return f"{self.color}{self.icon}{self.values}"
