from threading import Thread
from queue import Queue
from random import randint
import time


class Table:
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = None

    def __str__(self):
        return f'{self.number}'


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return self.name

    def run(self):
        waiting = randint(3, 10)
        time.sleep(waiting)


class Cafe:
    def __init__(self, *args):

        self.guests = None
        self.queue = Queue()
        self.args = args

    def guest_arrival(self, *guests):
        for g in range(len(guests)):
            for table in self.args:
                if table.guest is None:
                    table.guest = guests[g]
                    print(f"{guests[g]} сел(-а) за стол номер {table}")
                    guests[g].start()
                    break
            else:
                self.queue.put(guests[g])
                print(f'{guests[g]} в очереди')

    def discuss_guests(self):
        while self.queue.empty() == False:
            for table in self.args:
                if table.guest is None:
                    table.guest = self.queue.get()
                    print(f'{table.guest} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    table.guest.start()
            for table in self.args:
                if not table.guest.is_alive():
                    print(f"{table.guest} покушал(-а) и ушёл(ушла)")
                    print(f'Стол номер {table.number} свободен"')
                    table.guest = None
        t = True
        while t:
            k = 0
            for table in self.args:
                if table.guest is not None:
                    print(f"{table.guest} покушал(-а) и ушёл(ушла)")
                    print(f'Стол номер {table.number} свободен"')
                    table.guest = None
                if table.guest is None:
                    k+=1
            if k == len(self.args):
                t = False

# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
cafe = Cafe(*tables)
cafe.guest_arrival(*guests)
cafe.discuss_guests()
