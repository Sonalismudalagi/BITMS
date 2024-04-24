date=int(input("Enter date"))
month=int(input("Enter the month"))
year=int(input("Enter the year"))
c=year//100
d=year%100
#f=k+[(13*m-1)/5]+D+[D/4]+[c/4]-2*c
f=date+((13*month-1)/5)+ d+ (d/4)+ (c/4)-2*c
theday=int(f%7)
days={0:"Monday",1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday",5:"Saturday",6:"Sunday"}
print(days[theday+1])