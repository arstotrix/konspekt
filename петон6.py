lines2016 = []
i = 0
n = 0
with open ('happiness-cantril-ladder.csv', encoding='utf-8') as f:
    #for line in f:
    lines = f.readlines()
    for line in lines:
        #print(line)
        pieces = line.split(",")
        #print(pieces)
        if pieces[2] == '2016':
            lines2016.append(pieces)
            #n+=1
#print(lines2016[:10])
#for line in lines2016:
#    print(line)
    
user_cntr=input("papers, please: ")
for line in lines2016:
    if line[0] == user_cntr:
        value = float(line[3].strip())
        i+=1;
        print(value)
        #print ("STILL LOWER THAN IN GLORIOUS ARSTOTZKA")
if i == 0:
    print("sorry, i don't know")
    #print("REJECTED. GLORY TO ARSTOTZKA")

