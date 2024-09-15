import random


def euclid(a, b):
    if a == 0 or b == 0:
        return max(a, b)
    else:
        if a > b:
            return euclid(a - b, b)
        else:
            return euclid(a, b - a)


n = random.randint(0, 500)
m = random.randint(0, 500)

print(n, m)

print(euclid(n, m))