d={'A':1,'B':2,'C':3}
key=input("enetr key")
if key in d.keys():
    print("key is present")
    print(d[key])
else:
    print("Key isn't present")