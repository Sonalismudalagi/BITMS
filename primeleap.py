n=[2004,1996,17,10,85]
'''def prime():
    flag=0
    for i in n:
        for j in range(1,i):
            if(i%j==0):
                flag=1
    if(flag==0):
        print("Prime")
    else:
        print("Not prime")'''
def leap_year():
    for i in n:
        if(i%4==0 and i%1000!=0):
            print("Leap year")
        elif(i%1000==0 and i%400==0 and i%4==0):
                print("Century leap year")
        else:
            print("Not leap year")
#prime()
leap_year()