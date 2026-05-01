'''
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
'''

name=input('words:').split()
empty='ay'
newword=''
for i in range(len(name)):
    newword=name[i]+name[i][0]+empty
    newword=newword[1:]
    print(newword)
    

    

    

