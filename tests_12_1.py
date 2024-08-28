import unittest
import random


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner = Runner(''.join([random.choice('abcdef') for i in range(5)]))
        for _ in range(10): runner.walk()
        self.assertEquals(runner.distance, 50)

    def test_run(self):
        runner = Runner(''.join([random.choice('codec') for i in range(5)]))
        for _ in range(10): runner.run()
        self.assertEquals(runner.distance, 100)

    def test_challenge(self):
        runner1 = Runner(''.join([random.choice('codec') for i in range(5)]))
        runner2 = Runner(''.join([random.choice('codec') for i in range(5)]))
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.walk())
