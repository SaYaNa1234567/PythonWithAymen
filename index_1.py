
'''

Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
'''
## mine
name=input('words:').split()
empty='ay'
newword=''
for i in range(len(name)):
    newword=name[i]+name[i][0]+empty
    newword=newword[1:]
    print(newword)
    

## yours
    


def pig_it(text):
  words = str(text.split())
  res = []
  for x in words:
    if x.isalpha():
      pigi = x[1:]+x[0]+'ay'
      res.append(pigi)
    else:
      res.append(x)
  return ' '.join(res)

print(pig_it('hi sanya'))
print(pig_it('i am not sanya:0'))
>>>>>>> 7eb888ed0266324d3bb865a218e98ea5965e00f8
