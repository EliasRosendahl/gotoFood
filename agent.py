import math

from point import Point

max_distance = 50


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

    def eat(self, food):
        pass


    def move(self, scene):
        # Should have findClosets() funtion and not run every frame
        if len(scene.food) != 0:
            self.closets = scene.food[0]
        for food in scene.food:
            if self.distance(self.closets.location) > self.distance(food.location):
                self.closets = food

        self.moveTowards(self.closets)

        if self.x == self.closets.location.x and self.y == self.closets.location.y:
            self.eat(self.closets)
            scene.food.remove(self.closets)

    def distance(self, target):
        direction = Point(target.x - self.x, target.y - self.y)
        return math.sqrt(direction.x ** 2 + direction.y ** 2)