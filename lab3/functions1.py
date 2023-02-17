import math
import random


def ounces(grams):
    return 28.3495231 * grams


def centigrade(f):
    return (5 / 9) * (f - 32)


def solve(numheads, numlegs):
    rabbits = (numlegs - 2*numheads) / 2
    return [rabbits, numheads - rabbits]


def filter_prime(arr):
    arr2 = []
    for x in arr:
        is_prime = True
        y = 2
        while y < x:
            if x % y == 0:
                is_prime = False
        if is_prime: arr2.append(x)
    return arr2


def rev(string):
    spl = string.split(" ")
    spl.reverse()
    return "".join(spl)


def has_33(nums):
    contains3 = False
    for x in nums:
        if contains3 and x == 3:
            return True
        elif contains3 and x != 3:
            contains3 = False
        elif not contains3 and x == 3:
            contains3 = True
    return False


def spy_game(nums):
    contains0 = False
    contains00 = False
    for x in nums:
        if contains00 and x == 7:
            return True
        elif contains00 and x != 7:
            contains00 = False
            contains0 = False
        elif contains0 and x == 0:
            contains00 = True
        elif contains0 and x != 0:
            contains0 = False
        elif not contains0 and x == 0:
            contains0 = True
    return False


def sphere_volume(radius):
    return 3/4 * math.pi * radius**3


def unique(arr):
    arr2 = []
    for x in arr:
        for y in arr2:
            if y is x:
                break
        else:
            arr2.append(x)
    return arr2


def is_palindrome(string):
    for x in range(len(string)):
        if string[x] != string[-x - 1]:
            return False
    return True


def histogram(arr):
    for x in arr:
        print("*"*x)


def guess():
    guess_this = random.randint(1, 20)
    name = input("Enter your name: ")
    count = 0
    while True:
        inp = int(input("Guess a number: "))
        count += 1
        if inp == guess_this:
            print(f"Good job, {name}! You guessed my number in {count} guesses!")
            break
        elif inp < guess_this:
            print("Too low")
        else:
            print("Too large")
