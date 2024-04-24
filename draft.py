detail={"Name":"Sonali","Age":21,"DOB":"24-12-2003","Aadhar":123456789101,"Debitcard":1234567891023456,"Ph":9876543210,"PIN":583275,"Ht":5.2,"TAX%":12.5}
for i in detail:
    print(i)
print(detail)
print(detail.values,end=' ')
#sep="#".join(detail)
#print(sep)
print(detail.items,end=' ')
for key,value in detail.items():
    print(f"{key}#{value}",end=',')
#for key in detail.items():
 #   for value in detail.items():
  #      print(f"{key}#{value}",end=',')
  print('Name:%s