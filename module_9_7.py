def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        d = 2
        while d * d <= result:
            if result % d == 0:
                print("Составное")
            d += 1
        print("Простое")
        return result

    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)
