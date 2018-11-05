import unittest

from agent import Agent
from point import Point


class testAgent(unittest.TestCase):
    def setUp(self):
        self.agent = Agent(10, 10)
        self.target = Point(10, 20)

    def test_moveTowards(self):
        self.agent.moveTowards(self.target)
        self.assertEquals(self.agent.x, 10)
        self.assertEquals(self.agent.y, 12)

if __name__ == "__main__":
    unittest.main()