from point import Point


class Food(object):
    def __init__(self, x, y, value):
        self.location = Point(x, y)
        self.x = x
        self.y = y
        self.value = value