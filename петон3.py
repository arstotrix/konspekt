fname='C:\\Users\\student\\Documents\\river.txt'
print(fname)
#print("for\nexample")
with open(fname, encoding="utf-8") as f:
    #text = f.read()
    lines=f.readlines()
#lines=text.split('\n')
print(lines)
#print(lines[:5])

#text=""
#f=open(fname)
#text=f.read()
#print(text)
#f.close
text_el=[]
for line in lines:
    words=line.split()
    text_el.append(words)
    for word in words:
        print(word)
    print()
#print(text_el[-2:])
#print(len(text_el))
