def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
def Catalan(n):
    print(factorial(2*n)/(factorial(n)*factorial(n+1)))
