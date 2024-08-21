from threading import Thread, Lock
from random import randint
import time


class Bank:
    def __init__(self):
        self.balance = 0

    lock = Lock()

    def deposit(self):
        for i in range(100):
            add_append = randint(50, 100)
            self.balance += add_append
            print(f"Пополнение: {add_append}. Баланс: {self.balance}")
            time.sleep(0.001)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()

    def take(self):
        for i in range(100):
            withdrawal = randint(50, 100)
            print(f'Запрос на {withdrawal}')
            if withdrawal <= self.balance:
                self.balance -= withdrawal
                time.sleep(0.001)
                print(f"Снятие: {withdrawal}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
