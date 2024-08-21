from threading import Thread
import time


class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = 100

    def run(self):
        k = 0
        print(f'{self.name}, на нас напали!')
        while self.power <= self.enemies:
            time.sleep(1)
            self.enemies -= self.power
            k += 1
            print(f"{self.name} сражается {k} день(дня)., осталось {self.enemies} воинов.")
        else:
            print(f'{self.name} одержал победу спустя {k} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
