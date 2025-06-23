#Some Variable
sumCount=0

#Uses a for loop to iterate over numbers from 1 to 50
startValue=1
endValue=51

#logic for Using the sum range
for count in range(startValue,endValue):
    sumCount += count

#Print show in one time if you outside the loop
print("The sum of numbers from", startValue, "to", endValue, "is:", sumCount)
