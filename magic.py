class Mango:
    def __init__(self):
        print("This is a constructor")
    def tae(self):
        print("This is no parameter function")
    def jk(self,a,b):
        print("This is parameterized function",a+b)
    def magicalprime(self,a):
        flag=0
        flag1=0
        rem=0
        for i in range(2,a):
            if(a%i==0):
                flag=1
            while(a!=0):
                rem=rem%10
                a=a//10
                temp=rem*10+a
            print(temp)
        for i in range(2,temp):
            if(temp%i==0):
                flag1=1
        if(flag==0 and flag1==0):
            print("Magical Prime")
        else:
            print("Not magical prime")
m=Mango()
m.tae()
m.jk(10,20)
m.magicalprime(7)
        