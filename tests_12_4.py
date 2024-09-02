import math
import unittest
import random
from pprint import pprint
from unittest import TestCase
import logging


class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
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
                    finishers[place] = participant
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
        self.first = Runner('Вося', 10)
        self.second = Runner('Илья', 5)
        self.third = Runner('Арсен', 10)
        min_speed = math.inf
        self.name = ''
        for run_sped in self.first, self.second, self.third:
            if run_sped.speed < min_speed:
                min_speed = run_sped.speed
                self.name = run_sped.name

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run1(self):
        tournament = Tournament(90, self.first, self.third)
        self.all_results = tournament.start()
        self.assertTrue(self.all_results[len(self.all_results)] == self.name)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run2(self):
        tournament = Tournament(90, self.second, self.third)
        self.all_results = tournament.start()
        self.assertTrue(self.all_results[len(self.all_results)] == self.name)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run3(self):
        tournament = Tournament(90, self.first,
                                self.second, self.third)
        self.all_results = tournament.start()
        self.assertTrue(self.all_results[len(self.all_results)] == self.name)


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            Runner(2)
            logging.info("'test_walk' выполнен успешно")
            r2 = Runner(2)
            for _ in range(10): r2.walk()
            self.assertEquals(r2.distance, 50)
        except TypeError:
            # logging.warning()
            logging.error("Неверный тип данных для объекта Runner", exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            Runner('Вася', -5)
            logging.info("'test_run' выполнен успешно")
            r1 = Runner('Вася', -5)
            for _ in range(10): r1.run()
            self.assertEquals(r1.distance, 100)
        except:
            logging.error("Неверный тип данных для объекта Runner",exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        try:
            logging.info("'test_run' выполнен успешно")
            runner1 = Runner(''.join([random.choice('codec') for i in range(5)]))
            runner2 = Runner(''.join([random.choice('codec') for i in range(5)]))
            for _ in range(10):
                runner1.run()
                runner2.walk()
            self.assertNotEqual(runner1.distance, runner2.walk())
        except:
            logging.error("Неверный тип данных для объекта Runner",exc_info=True)


first = Runner('Вося', 10)
second = Runner('Илья', 5)
third = Runner('Арсен', 10)
t = Tournament(101, first, second)
print(t.start())
logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_test.log', encoding='utf-8',
                    format="%(asctime)s | %(levelname)s  | %(message)s ")
