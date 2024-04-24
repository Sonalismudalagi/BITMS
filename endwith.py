st=input("Enter the string")
va=input("Give the values")
zipped=zip(st,va)
for i in zipped:
    if(i.endswith('i')):
        print(i)
#wf=[l.endswith('i') for p in l]
#print(dict(zip(l,wf)))