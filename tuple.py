p=tuple([30,40,50,60,70,80])
q=(10,20,30,40,50,60)
s=()
print("Class of p",type(p))
def duplicate():
    print("The duplicates are:")
    for i in p:
        if i in q:
            print(i,end=' ')
duplicate()
def concat():
    r=p+q
    print("\nConcatenated tuple is",r)
    print("MAX=",max(r))
    print("MIN=",min(r))
    print("LENGTH=",len(r))
concat()
def mul():
    print("Tuple reapeated=",q*2)
mul()
print("MAX of p",max(p))
print("MAX of q",max(q))
print("MIN of p",min(p))
print("MIN of q",min(q))
print("len of p",len(p))
print("len of q",len(q))

