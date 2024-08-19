def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        d = 2
        t=True
        while d * d <= result:
            if result % d == 0:
                t=False
            d += 1
        print('Простое') if t else print('Составное')
        return result

    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)
