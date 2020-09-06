class Square:
    def __init__(self, position):
        self.position = position
        self.occupated = False
        self.figure = None

    def set_figure(self, figure):
        self.figure = figure
        self.occupated = True

    def get_figure(self):
        return self.figure

    def is_occupated(self):
        return self.occupated

    def set_occupation(self, occupation):
        self.occupated = occupation

    def get_name(self):
        return self.position
