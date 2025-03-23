import math
a = int(input())
b = int(input())
print(math.sqrt(a**2+b**2))

n = int(input())
print(f"The next number for the number {n} is {n+1}. ")
print(f"The previous number for the number {n} is {n-1}.")

n = int(input())
k = int(input())
print(k//n)

n = int(input())
k = int(input())
print(k%n)

v = int(input())
t = int(input())
s = 109
pos = (v*t) % s
print(pos)