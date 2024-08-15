class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        self.__vin = vin
        self.__numbers = numbers
        self.get___is_valid_vin()
        self.get__is_valid_numbers()

    def get_vin(self):
        return self.__vin

    def get_number(self):
        return self.__numbers

    def __is_valid_vin(self):
        if not (isinstance(self.get_vin(), int)):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if not (1000000 <= self.get_vin() <= 9999999):
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        else:
            return True

    def get___is_valid_vin(self):
        return self.__is_valid_vin()

    def __is_valid_numbers(self):
        if not (isinstance(self.get_number(), str)):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        elif len(self.get_number()) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        else:
            return True

    def get__is_valid_numbers(self):
        return self.__is_valid_numbers()


class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
