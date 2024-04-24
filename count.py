st=input("Enter the string")
l=[]
l=st.split()
wf=[l.count(p) for p in l]
print(dict(zip(l,wf)))