#DAY1 26/4/24
#Problem 1
n=int(input("NO>"))
if(n%2==0 and (n>=2 and n<=5)):
    print("Not weird")
elif((n%2==0) and (n>=6 and n<=20)):
     print("Weird")
elif(n%2==0 and n>20):
     print("Not weird")
elif(n%2!=0):
    print("Weird")
else:
    print("Invalid input")
#Problem 2
a = int(input())
b = int(input())
print(a+b)
print(a-b)
print(a*b)
#Problem 3
a = int(input())
b = int(input())
print(a//b)
print(a/b)
#EXTRA
n = int(input())
for i in range(n):
    print(i**2)
#EXTRA 2
def is_leap(year):
    leap = False
    if(year%4==0 and year%100!=0):
        leap=True
    elif(year%100==0 and year%4==0 and year%400==0):
        leap=True
    else:
        leap=False
    # Write your logic here
    
    return leap

year = int(input())
print(is_leap(year))
#EXTRA 3
n = int(input())
for i in range(1,n+1):
    print(i,end='')
