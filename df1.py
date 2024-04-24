def sonali():
    return "This is Sonali!"
dict1={"FName":sonali,"Age":20,"Addr":"I-110"}
print("The original dictionary:"+str(dict1))
res=dict1['FName']()
print("The required resul is:",str(res))
#function returns 
def sonali():
    print("This is Sonali!")
dict1={"FName":sonali,"Age":20,"Addr":"I-110"}
print("The original dictionary:"+str(dict1))
dict1['FName']()
#with arguments
def add(a,b):
    print("Addition=",a+b)
dict1={"FName":add,"Age":20,"Addr":"I-110"}
print("The original dictionary:"+str(dict1))
dict1['FName'](10,20)