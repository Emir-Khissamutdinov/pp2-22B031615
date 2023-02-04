print("5 + 5 ==", 5 + 5)
print("5 - 5 ==", 5 - 5)
print("5 * 5 ==", 5 * 5)
print("3 / 2 ==", 3 / 2)
print("3 // 2 ==", 3 // 2)
print("5 % 5 ==", 5 % 5)
print("2 ** 10 ==", 2 ** 10)

print()

a = 5
a **= 3
print("a is equal to", a)

print()

print("a == 5", a == 5)
print("a != 5", a != 5)
print("a > 5", a > 5)
print("a < 5", a < 5)
print("a >= 5", a >= 5)
print("a <= 5", a <= 5)

print()

bool_a = True
bool_b = False
print("And", bool_a and bool_b)
print("Or", bool_a or bool_b)
print("Not", not bool_a)

print()

list_a = ["something", "anything"]
print("Is eth in list_a[0]:", "eth" in list_a[0])
print("Is something not in list_a:", "something" not in list_a)

print()

a = "word"
b = "word"
print("If a is b:", a is b)
print("If a is not b:", a is not b)

print()

a = 6  # 0110
b = 10  # 1010
print("AND", a & b)
print("OR", a | b)
print("XOR", a ^ b)
print("NOT", ~a)
print("LEFT SHIFT", a << 1)
print("RIGHT SHIFT", a >> 2)
