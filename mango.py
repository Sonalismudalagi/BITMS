str1='Mango city- use single qts inside double quotes'
#count=[i for i in str [j for j in i if(j=='s')]]
print([w for w in str1.split() if 's' in w])