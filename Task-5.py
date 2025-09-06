def factorial(num):
    if num>=2:
        fact= num*factorial(num-1)
        return fact
    else:
        return 1

num=int(input("Enter Number : "))
fact=factorial(num)
print("The factorial of",num,"is",fact)