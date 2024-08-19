from itertools import combinations


def all_variants(text):
    k = 1
    while k <= len(text):
        for e in combinations(text, k):
            yield ''.join(e)
        k += 1


a = all_variants("abc")
for i in a:
    print(i)
