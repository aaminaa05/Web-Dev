n = int(input())
arr = list(map(int,input().split()))
for i in range(0,n,2):
    print(arr[i],end=" ")

n = int(input())
arr = list(map(int,input().split()))
for i in range(0,n):
    if arr[i]%2==0:
        print(arr[i],end=" ")

n = int(input())
arr = list(map(int,input().split()))
cnt = 0
for i in range(0,n):
    if arr[i]>0:
        cnt+=1
print(cnt)

n = int(input())
arr = list(map(int,input().split()))
cnt=0
for i in range(n-1):
    if arr[i]<arr[i+1]:
        cnt+=1
print(cnt)

n = int(input())
arr = list(map(int,input().split()))
cnt = 0
for i in range(n-1):
    if arr[i] * arr[i+1]>0:
        print("YES")
        break
else: print("NO")

n= int(input())

arr = list(map(int, input().split()))

count = 0
for i in range(1, n - 1):

    if arr[i - 1] < arr[i] and arr[i + 1] < arr[i]:
        count += 1

print(count)

n = int(input())
arr = list(map(int,input().split()))

left = 0
right = n-1
while left<right:
    arr[left],arr[right] = arr[right],arr[left]
    left+=1
    right-=1
print(" ".join(map(str,arr)))