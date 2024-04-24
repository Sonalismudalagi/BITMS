fp=open("abc.txt",'w')         #open
fp.write("Hello")              #write
print(fp)
if fp:
    print("Done")
print(fp.closed)                #checks if the file is closed or not
fp.close()                      #close
#append
fp1=open("abc.txt",'a')         #append
fp1.write("\nHow are you??")
fp1.writelines("Today its Thursday The date is 18th of April")   #writelines
print(fp1)
if fp1:
    print("Done")
print(fp1.name)                    #display name of file
fp1.close()
#read
fp2=open("abc.txt",'r')
print(fp2.read(15))               #read
fp2.seek(0)
print(fp2.readline(2))            #readline
print(fp2.mode)                    #mode of file
fp2.close()                        