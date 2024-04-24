name="SONALI SANGAMESH"
v="AEIOU"
res=[char for char in name if char in v]
print(res)
res=[char for char in name if char not in v]
print(res)
'''for i in name:
    for j in v:
        if j not in name:
            print(i)'''
print(name[::3])
print(name[::-3])
for i in range(0,len(name)):
    if(i%2==0 and i!=0):
        print('-',end='')
    else:
        print(name[i],end='')
