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
        if math.sqrt(direction.x ** 2 + direction.y ** 2) > max_distance:
            k = max_distance / math.sqrt(direction.x ** 2 + direction.y ** 2)
            if direction.x != 0:
                direction.x = k * direction.x
            if direction.y != 0:
                direction.y = k * direction.y

        #sets location of agent
        self.x = self.x + direction.x
        self.y = self.y + direction.y


        print(self.x, self.y, direction.x, direction.y)

    def move(self, scene):
        for food in scene.food:
            self.moveTowards(food.location)
            break