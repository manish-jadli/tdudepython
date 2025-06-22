#Sum of Integers from 1 to 50 Using a Loop
sumCount=0
startValue=1
endValue=51

#logic

#Using the sum range
'''
print("The sum of numbers from", startValue, "to", endValue, "is:",sum(range(startValue,endValue)))
'''
for count in range(startValue,endValue):
    sumCount += count

#Print show in one time if you outside the loop
print("The sum of numbers from", startValue, "to", endValue, "is:", sumCount)
