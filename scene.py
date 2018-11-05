import random

from food import Food
from agent import Agent


class Scene(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.agents = [Agent(400, 200), Agent(200, 400), Agent(300, 300)]
        self.food = [Food(30, 30, 100)]

    def tick(self):
        for agent in self.agents:
            agent.move(self)

    def spawnFood(self):
        self.food.append(Food(random.randrange(720), random.randrange(480), 100))