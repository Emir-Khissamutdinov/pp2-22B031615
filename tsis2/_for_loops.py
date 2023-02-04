a_list = ["word", 7, True, False, True]
a = 0
for x in range(len(a_list)):
    print(a_list[x])
    a = int(input())
    if a == 4: break
    if a == 3: continue
    print("It is not continued")
else:
    print("The loop is finished without breaks")


for y in "anything":
    pass
