def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
numSelect = input("What number would you like to get the factorial of?")
numFact = factorial(numSelect)
print(f"The factorial of {numSelect} is {numFact}!")
