emp={"Name":"Sonali","Age":20,"Salary":1000}
print(emp)
dict1={}
print(type(dict1))
print("Name is: %s" %emp["Name"])
#emp["Age"]=int(input("Age:"))
print(emp)
#del emp["Name"]
print(emp)
#del emp
#print(emp)
for x in emp:
    print(x)  #prints the key values
for i in emp:
    print(emp[i])
print(emp.keys())
print(emp.values())
print(emp.get("Age"))
print(emp.items())
emp.update({"Hobby":"Poetry"})
print(emp)
