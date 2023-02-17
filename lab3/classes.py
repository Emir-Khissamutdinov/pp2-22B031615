import math


class First:
    def getString(self):
        self.string = input("Enter a string: ")

    def printString(self):
        self.string.upper()
        print(self.string)


class Shape:
    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Point:
    x = 0
    y = 0

    def show(self):
        print(f"({self.x}, {self.y})")

    def move(self, x, y):
        self.x = x
        self.y = y

    def dist(self, point):
        dx = abs(self.x - point.x)
        dy = abs(self.y - point.y)
        return math.sqrt(dx**2 + dy**2)


class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount


def is_prime(num):
    for x in range(2, num):
        if num % x == 0:
            return False
    return True


def filter_primes(arr):
    filter(is_prime, arr)
