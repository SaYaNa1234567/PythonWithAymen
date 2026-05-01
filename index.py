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
