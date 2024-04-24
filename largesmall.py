l=[2,4,1,-3,-5,7]
l1=[]
l2=[]
for i in l:
    if(i%2==0):
        l1.append(i)
    else:
        l2.append(i)
print(max(l1))
largest=0
for j in l1:
    if(largest<j):
        largest=j
print(largest)
print(min(l2))
smallest=0
for k in l2:
    if(smallest>k):
        smallest=k
print(smallest)