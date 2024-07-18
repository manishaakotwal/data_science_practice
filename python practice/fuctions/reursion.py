# recursion: a defined function can call itself.
def factorial(n):
    # base case
    if n==0:
        return 1
    #recursive case
    else:
        return n * factorial(n-1)
    
print(factorial(5))    
