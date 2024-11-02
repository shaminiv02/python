#factorial of a number using recursive function
def factorial(x):
    if x==0:
        return 1
    else:
        return x*factorial(x-1)

a=int(input("enter a number"))
print(factorial(a))
