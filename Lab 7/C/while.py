import math
n = int(input())
i = 0
while i<n:
    i+=1
    if math.isqrt(i)**2==i:
        print(i)

n = int(input())
i =2
while  i<=n:
    if n%i==0:
        print(i)
        break
    i+=1

n = int(input())
power = 1
while power<=n:
    print(power,end=" ")
    power *=2

n = int(input())
power = 1
while power<=n:
    print(power,end=" ")
    power *=2

if power == n:
    print("YES")
else:
    print("NO")

N = int(input())  
k = 0  
power = 1  

while power < N:  
    power *= 2  
    k += 1  

print(k) 
