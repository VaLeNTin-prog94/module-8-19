def k_count(n):
    return len(str(n).replace('.', ' ').split()[-1])


def type_a_b(a, b):
    if type(a) == float and type(b) != float:
        return 1
    elif type(b) == float and type(a) != float:
        return 2
    elif type(a) == float and type(a) == float:
        return 3


def add_everything_up(a, b):
    try:
        match type_a_b(a, b):
            case 1:
                return round(a + b, k_count(a))
            case 2:
                return round(a + b, k_count(b))
            case 3:
                return round(a + b, k_count(a) if k_count(a) > k_count(b) else k_count(b))

    except TypeError:
        return str(a) + str(b)


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.7676, 7.4343434))
