def pig_it(text):
  text = str(text)
  words = text.split()
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
## 2
def fuck(num):
  i = 5
  count = 0
  while num // i >=1:
    count += num//i
    i *= 5
  return count

print(fuck(6))

print(fuck(5))

## 2 only fac

def fuck(num):
  res = 1
  for x in range(1, num+1):
    res *= x
  return res
print(fuck(6))
## 3

N = int(input())
dig = str(N)
print(' '.join(dig))
print(' '.join(dig[::-1]))

## 4 
def wsp(text):

  words = text.split()
  res = ""
  for x in words:
    f1 = x[0].upper()
    rest = x[1:].lower()
    res += f1+rest
  return res
print(wsp('ad asd'))


