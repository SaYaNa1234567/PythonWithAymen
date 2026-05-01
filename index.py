def pig_it(text):
  words = str(text.split())
  res = []
  for x in words:
    if x.isalpha():
      pigi = words[1:] +words[0]+'ay'
      res.append(pigi)
    else:
      res.append(x)
  return res

pig_it('hi sanya')
pig_it('i am not sanya:0')
