from syllables import find_num_syllables #imports find_num_syllables()
paragraph=str(input("Enter a paragraph => ", ))
print(paragraph)
#creates variable paragaph, which is the paragraph
m=paragraph.split() #creates a list with every individual word in the paragraph in it
b=paragraph.split(".") #creates a list with every sentence as a value in it
k=0
hardwords=[]
sentlen=[]
while k<len(m):
    z=m[k]
    z=z.strip(".")
    z=z.lower()
    if z.count("-")>=1:
        k+=1
    elif find_num_syllables(z)>=3 and z.endswith("ed")== False and z.endswith("es")==False :
        hardwords.append(m[k])
        k+=1
    elif find_num_syllables(z)<3:
        k+=1
#above creates list with all hard words
print("Here are the hard words in this paragraph:\n", hardwords, sep="")
n=0
while n<(len(b)-1):
    sent=b[n]
    sent=sent.split()
    length_sent=len(sent)
    sentlen.append(length_sent)
    n+=1
#above crates a list with the length of every sentence
i=0
syl=0
length_words=len(m)
while i<len(m):
    syl+=find_num_syllables(m[i])
    i+=1
#above finds the total number of syllables in the paragraph
PHW=float((len(hardwords)/len(m)))*100
PHWpercent=str(format((PHW), '.2f'))+"%"
asl=float(sum(sentlen)/(len(b)-1))
#above creates PHW, PHWpercent, and ASL
asyl=float((syl/(len(m))))
print("Statistics: ASL:"+str(format(asl, '.2f')), "PHW:"+PHWpercent, "ASYL:"+str(format(asyl, '.2f')))
#above defines asyl and prints statistics
GFRI=(0.4*(asl+PHW))
print("Readability index (GFRI):", format(GFRI, '.2f'))
FKRI=206.835-(1.015*asl)-(86.4*asyl)
print("Readability index (FKRI):", format(FKRI, '.2f'))
#above defines and prints GFRI and FKRI