#l=list(input("Enter the list elements"))
l=[2,4,1,-3,-5,7]
nsum=0
esum=0
osum=0
for i in l:
    if(i<0):
        nsum+=i
    else:
        if(i%2==0):
            esum+=i
        else:
            osum+=i
print("Sum of -ve numbers",nsum)
print("Sum of +ve even numbers",esum)
print("Sum of +ve odd numbers",osum)
#used list representation for this
neg=[i for i in l if i<0]
print(neg)
even=[j for j in l if i%2==0]
print(even)
odd=[k for k in l if i%2!=0]
print(odd)