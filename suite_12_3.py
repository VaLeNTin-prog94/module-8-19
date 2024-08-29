import math
import unittest
from math import inf
from pprint import pprint
import random
from unittest import TestCase


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant.name
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def tearDown(self):
        print(self.all_results)

    def setUp(self):
        self.runner1 = Runner('Усейн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)
        min_speed = math.inf
        self.name = ''
        for run_sped in self.runner1, self.runner3, self.runner2:
            if run_sped.speed < min_speed:
                min_speed = run_sped.speed
                self.name = run_sped.name

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run1(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        self.all_results = tournament.start()
        self.assertTrue(self.all_results[len(self.all_results)] == self.name)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run2(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        self.all_results = tournament.start()
        self.assertTrue(self.all_results[len(self.all_results)] == self.name)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run3(self):
        tournament = Tournament(90, self.runner1,
                                self.runner2, self.runner3)
        self.all_results = tournament.start()
        self.assertTrue(self.all_results[len(self.all_results)] == self.name)

class RunnerTest(unittest.TestCase):
    is_frozen=False
    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner = Runner(''.join([random.choice('abcdef') for i in range(5)]))
        for _ in range(10): runner.walk()
        self.assertEquals(runner.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner = Runner(''.join([random.choice('codec') for i in range(5)]))
        for _ in range(10): runner.run()
        self.assertEquals(runner.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner1 = Runner(''.join([random.choice('codec') for i in range(5)]))
        runner2 = Runner(''.join([random.choice('codec') for i in range(5)]))
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.walk())

test_unittest=unittest.TestSuite()
test_unittest.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
test_unittest.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))
runner=unittest.TextTestRunner(verbosity=2)
runner.run(test_unittest)