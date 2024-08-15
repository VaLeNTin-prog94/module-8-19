def personal_sum(numbers):
    result, incorrect_data = 0, 0

    for i in numbers:
        try:
            result += i
        except TypeError:
            incorrect_data += 1
            print('Некорректный тип данных для подсчёта суммы-', i)
    return result, incorrect_data


def calculate_average(numbers):
    try:
        sum_chisel, k = personal_sum(numbers)
        try:
            return sum_chisel / (len(numbers) - k)
        except ZeroDivisionError:
            return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')


print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
