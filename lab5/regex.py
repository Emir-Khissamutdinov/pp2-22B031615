import re


txt = "Aaa_abb_c e_ff_gGg"

x = re.search(r"ab*", txt)
if x: print(1, x.group())

x = re.search(r"ab{2,3}", txt)
if x: print(2, x.group())

x = re.findall(r"[a-zа-я]+_[a-zа-я]+", txt)
print(3, x)

x = re.findall(r"[A-ZА-Я][a-zа-я]+", txt)
print(4, x)

x = re.compile(r"a.*b", re.DOTALL)
x = re.search(x, txt)
if x: print(5, x.group())

x = re.sub(r"[ ,.]", ":", txt)
print(6, x)


def camel(match):
    return match.group(1) + match.group(2).upper()


x = re.sub(r"(.*?)_([a-zA-Z])", camel, txt)
print(7, x)


x = re.split(r"[A-ZА-Я]", txt)
print(8, x)


def space(match):
    return match.group(1) + " " + match.group(2)


x = re.sub(r"(\w)([A-ZА-Я])", space, txt)
print(9, x)


def snake(match):
    return match.group(1).lower() + "_" + match.group(2).lower()


x = re.sub(r"(.+?)([A-Z])", snake, txt)
print(10, x)
