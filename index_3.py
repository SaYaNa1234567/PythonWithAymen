'''
A natural number N is given. Print all its digits one by one, in the usual order (and then in reverse), separating them with spaces or new lines. For example: 179 => 1 7 9; 179 => 9 7 1
Write a method (or function, depending on the language) that converts a string to camelCase, that is, all words must have their first letter capitalized and spaces must be removed.

Examples (input --> output):
"hello case" --> "HelloCase"
"camel case word" --> "CamelCaseWord"

'''
word="hello case"
lis=word.split()
new_var=''
for i in lis:
    new_var+=i.capitalize()
print(new_var)

