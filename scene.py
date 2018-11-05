from food import Food
from agent import Agent


class Scene(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.agents = [Agent(400, 200)]
        self.food = [Food(30, 30, 100)]

    def tick(self):
        for agent in self.agents:
            agent.move(self)