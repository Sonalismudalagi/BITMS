d1=input("Enter the key")
d2=input("Enter values")
my_dict=dict(zip(d1,d2))
print(my_dict)
for key,value in my_dict.items():
    if key[0].lower=='b':
        print(f"The value of {key} is {value}")