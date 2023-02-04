a = 0
while a != 5:
    a = int(input())
    if a == 4: break
    if a == 3: continue
    print("It is not continued")
else:
    print("The loop is finished without breaks")
