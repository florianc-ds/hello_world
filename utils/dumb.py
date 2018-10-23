class Shape:

    def __init__(self, sides):
        self.sides = sides

    def introduce(self):
        print('hello I\'m a %s-sided shape..!' % self.sides)
