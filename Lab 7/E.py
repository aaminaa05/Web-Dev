def minn(a,b,c,d):
    return min(a,b,c,d)

a,b,c,d=map(int,input().split())
print(minn(a,b,c,d))
 

def db_power(a,  n):
    return(a**n)
a,n=map(int,input().split())
print(db_power(a,n))

def xor(x,y):
    return x!=y
x,y = map(int,input().split())
print(xor(x,y))