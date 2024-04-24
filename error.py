#print(dir(locals()['__builins__'])
try:
    en=[2,3,5,6]
    print(en)
except ZeroDivisionError:
    print("0 no division")
except IndexError:
    print("index out")
#new
try:
    num=int(input("Enter"))
    
    