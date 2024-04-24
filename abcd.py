y=int(input("Enter the year"))
if(y>=1000 or y<=99999):
    year=y
c=year//100
d=year%100
days={0:"Monday",1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday",5:"Saturday",6:"Sunday"}
def zellers(day,month,year):
    m=int(input("Enter month"))
    if(m>=1 or m<=12):
    month=m 
    if(m in [1,3,5,7,8,10,12]):
        d=int(input("Enter the day"))
        if(d>=1 or d<=31):
            date=d
    elif(m in [4,6,9,11]):
        d1=int(input("Enter date"))
        if(not(d1<0 and d1>31)):
            date=d1
    elif(m in [2]):
        d2=int(input("Enter date"))
        if(d2>=1 or d2<29):
            date=d2
    else:
        print("Invalid date")
else:
    print("INcorrect month")
f=k+[(13*m-1)/5]+D+[D/4]+[c/4]-2*c
f=date+((13*month-1)/5)+ d+ (d/4)+ (c/4)-2*c
theday=int(f%7)
# days={0:"Monday",1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday",5:"Saturday",6:"Sunday"}
# print(days[theday+1])