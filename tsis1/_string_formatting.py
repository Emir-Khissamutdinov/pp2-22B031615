text1 = "The second argument will be here: {1}, the first one is here: {0}"
text2 = "There will be three digits after the point: {:.3f}"
text3 = "Here arguments are placed respectively: {}, {}, {}"
text4 = "The first argument should be named h: {h}"
print(text1.format(1337, 420))
print(text2.format(9))
print(text3.format(5, 7, 3))
print(text4.format(h="arg"))
