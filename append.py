'''n=[10,20,30,40,50,30,50]
y=[]
for i in n:
    if i not in y:
        y.append(i)
print(y)'''

#y=[10,20,30,40,50]
#n=[60,70,80,90,100,20]
sam=list(input("Enter list elements"))
ram=list(input("Enter list elements"))
print("the duplicates are")
for i in sam:
    if i in ram:
        print(i,end='')