def pig_it(text):
  words = text.split()
  res = []
  for x in words:
    if x.isalpha():
      pig = word[:1] +word[0]+"ay"
      result.append(pig)
    else:
      result.append(pig)
  return res

pig_it('hi sanya')
pig_it("i am not sanya:0")
