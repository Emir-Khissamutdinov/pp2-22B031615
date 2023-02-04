list_a = ["a", "b", "c"]
print(list_a)
print(len(list_a))
print(list_a[0])

print()
for x in list_a:
    print(x)

print()
list_a.pop(1)
print(list_a)
list_a.pop()
print(list_a)
list_a.append("d")
print(list_a)
list_a.remove("a")
print(list_a)
