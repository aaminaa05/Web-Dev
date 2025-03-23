a = int(input())
b = int(input())
for i in range(a,b+1):
    if i%2==0:
        print(i, end =" ")

a,b,c,d=map(int,input().split())
for i in range(a,b+1):
    if i%d==c:
        print(i,end=" ")


import math
a = int(input())
b = int(input())
for i in range(a,b+1):
   if math.isqrt(i)**2==i:
      print(i, end=" ")

x = int(input())
d = int(input())
cnt = 0
for i in x:
    if i==d:
        cnt+=1
print(cnt)

x = int(input())
s=sum(int(i) for i in str(x))
print(s)

x = int(input())
reverse=0
while x!=0:
    digit = x%10
    reverse = reverse*10+digit
    x//=10
print(str(reverse))

x = int (input())
for i in range(2,30001):
    if x%i==0:
        print(i)
        break

x = int (input())
for i in range(1,x+1):
    if x%i==0:
        print(i,end=" ")
        
x = int(input())
cnt = 0

for i in range(1, int(x**0.5) + 1):  
    if x % i == 0:
        cnt += 1  
        if i != x // i:  
            cnt += 1  

print(cnt)

cnt =0
for _ in range(100):
    cnt+=int(input())
print(cnt)

n = int(input())
cnt = 0
for _ in range(0,n):
    cnt+= int(input())
print(cnt)

binary = input()  
decimal = 0 

for digit in binary:
    decimal = decimal * 2 + int(digit)  

print(decimal)  

n = int(input())
cnt =0
for _ in range (0,n):
    digit = int(input())
    if digit==0:
        cnt+=1
print(cnt)