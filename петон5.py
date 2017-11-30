#a function is a local algorhythm that can be used anywhere in the major code
#def hello(user):
    #print("hello, "+user+"!")
    #if age>10:
    #    print("older than 10")
    #else:
    #    print(age)
    #sum_=0
    #for i in range(16):
    #    sum_+=1
    #print(sum_)
    #print(gl)
    #new.name()=user.title()
    #return user.title()
#global variables can be used in local functions    
#gl=(100)
#hello("Marie", 18)
#print(sum_)
#whereas local variables cannot be used in the global code
#user_title=hello('Marie')
#print(user_title)

#DO NOT FORGET BRACKETS AFTER FUNCTIONS

def elements(word):
    ''' '''
    for l in word:
        print(l)
    print(len(word))

    def tokenize(sentence):
        words = sentence.split()
        return words

sent = 'i beg to dream and differ'

#els=sent.split()
#elements(els)

tok_result=tokenize(sent)
print(tok_result)

for w in tok_result:
    print (w.upper)
        
