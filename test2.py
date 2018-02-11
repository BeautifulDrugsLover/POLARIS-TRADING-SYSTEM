import re
l1=[]
l2=[]
c=0

with open('scrapper.txt','rt') as f:
    for i in f:
        b=re.search(r'2">(.+?)</a>',i)
        if(b==None):
            continue
        else:
            if(c%2==0):
                l1=l1+[b.group()[6:-8:]]
            else:
                l2=l2+[b.group()[3:-4]]
        c=c+1

print(set(l2))
l=dict(zip(l1,l2))

print(c)

import csv
with open('companies.csv','w') as file:
    obj = csv.writer(file)
    for key,value in l.items():
        obj.writerow([key,value])

