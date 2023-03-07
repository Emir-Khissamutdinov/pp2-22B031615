import time
import math

a1 = int(input())
a2 = int(input())

time.sleep(a2 * 0.001)
result = math.sqrt(a1)

print("Square root of", a1, "after", a2, "milliseconds is", result)
