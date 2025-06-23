#Check if a Number is Even or Odd
number=int(input("Enter a number: "))
oddVar=number % 2 == 0

#Logic of odd or even number
if oddVar:
    print(number, "is an even number.")
else:
    print(number, "is an odd number.")
