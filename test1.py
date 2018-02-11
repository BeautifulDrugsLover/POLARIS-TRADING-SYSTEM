import string
greenday = []
eminem = []
p1=0
p2=0
exc=string.punctuation

word = " American "



word = "".join(x for x in word if x not in exc )
word=word.split()
word=[x.lower() for x in word]

with open ('Greenday.txt','rt') as f:
    for line in f:
        if len(line)==0:
            continue
        else:
            intake=line.lower()
            intake ="".join(x for x in intake if x not in exc)
            greenday=greenday+intake.split()


with open ('Eminem.txt','rt') as f:
    for line in f:
        if len(line)==0:
            continue
        else:
            intake=line.lower()
            intake="".join(x for x in intake if x not in exc)
            eminem=eminem+intake.split()


for i in word:
    p1=p1+greenday.count(i)
    p2=p2+eminem.count(i)

a=p1/len(greenday)
b=p2/len(eminem)

gr=(a/(a+b))
em=(b/(a+b))
print(gr,em)
if (gr>em):
    print("GreenDay")
else:
    print("Eminem")








