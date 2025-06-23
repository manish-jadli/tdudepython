#Calculate Factorial Using a Function

#User Enter the Integer Input Value
inputVal=int(input("Enter a number: "))

def factorial(val):
    if val <2:
        return 1
    else:
        return val * factorial(val -1)

#Final Result
factorialResult=factorial(inputVal)

#Print the Result Value
print("Factorial of", inputVal, "is: ",factorialResult)