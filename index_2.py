
'''
Write a program that will calculate the number of trailing zeros in a factorial of a given number.

N! = 1 * 2 * 3 *  ... * N

'''
def factorial(numb):
    n=1
    for i in range(1,numb+1):
        n *= i
    return n

print(factorial(numb=12))
