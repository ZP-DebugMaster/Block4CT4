def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

if __name__ == "_main_":

    num = input("Factorial of what, exactly  ")
    print("The factorial of ", num , " is ", factorial(int(num))
