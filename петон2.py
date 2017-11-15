#nums=[]
#for n in range(5):
#    print(n)
#    nums.append(n)
#print (nums)
#print (len(nums))
#text="rapit nos atrociter"
#words=text.split()
#print(words)
#print(words[2:])
#for w in words:
#    print(w)
#nums=[[1,2,3]]*3
#print(nums)
#for row in nums:
    #print(row)
    #print('inner')
#    for n in row:
#        print (n, end=' ')
#    print()
#w="hello world"
#letters=[]
#for j in w:
#    letters.append(j)
#print(letters)
#nums=[1,2,3]
#nums_str=""
#for a in nums:
#    nums_str+=(" "+str(a))
#print(nums_str[1:])
letters=list('hello')
#new=letters.pop(-1)
#print(letters.index('e'))
#print(letters.count('l'))
i=0
nums=[[1,2,3,4]]*5
#print(nums)
for row in nums:
    if i%2!=0:
        print(row.reverse())
    else:
        print(row)
    i+=1

