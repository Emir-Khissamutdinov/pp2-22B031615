def squares1(n):
    current = 0
    while current != n:
        yield current**2
        current += 1


def even(n):
    current = 2  # first even number larger than 0
    while current < n:
        yield current
        current += 2


def print_even():
    n = int(input())
    for x in even(n):
        print(str(x) + ", ", end="")


def divisible(n):
    current = 12  # first divisible by 3 and 4 larger than 0
    while current < n:
        yield current
        current += 12


def squares(a, b):
    while a < b:
        yield a**2
        a += 1


def square_test():
    for x in squares(5, 12):
        print(x, end=" ")


def decrement_from(n):
    while n > 0:
        yield n
        n -= 1
