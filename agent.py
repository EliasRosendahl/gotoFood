import math

from point import Point

max_distance = 2


class Agent(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def moveTowards(self, target):
        '''Moves the agent towards a point'''
        direction = Point(target.x - self.x, target.y - self.y)

        # Limits length of movement if it's more than max distance
        if math.sqrt(direction.x^2 + direction.y ^2) > max_distance:
            if direction.x is not 0:
                direction.x = (max_distance * direction.x) / direction.x
            if direction.y is not 0:
                direction.y = (max_distance * direction.y) / direction.y

        #sets location of agent
        self.x = self.x + direction.x
        self.y = self.y + direction.y   

    def move(self, scene):
        for food in scene.food:
            self.moveTowards(food.location)
            break