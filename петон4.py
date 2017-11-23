#you must convert everything you want to append to str
filename="text.txt"
#with open (filename, 'w') as f:
    #f.write('hello\n')
sent="i beg to dream and differ from the hollow lies"
words=sent.split()
lines=[]
i=0
#for w in words:
#    if i%2!=0:
#        w=w.upper()
#    lines.append(w+'\n')
#    i+=1
for i,w in enumerate(words):
    if i%2!=0:
        w=w.upper()
    j=str(i)
    lines.append(j+' '+w+'\n')
    print(i,w)
with open ('text.txt', 'w', encoding='utf-8') as f:
    f.writelines(lines)
    #for line in lines:
        #f.write(line.upper())    

