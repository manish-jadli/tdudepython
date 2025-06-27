# Demonstrate List Slicing

#Variable of Number

numberArray=[1,2,3,4,5,6,7,8,9,10]
startValue=0
endValue=5
fiveNumberArray=numberArray[startValue:endValue]

#Original List

print("Original list:",numberArray)

#Extract first five elements

print("Extracted first five elements:",fiveNumberArray)

#Reversed extracted elements

#Copy fiveNumberArray
fiveNumberArrayCopy=fiveNumberArray.copy()

#Reverse fiveNumberArrayCopy

fiveNumberArrayCopy.reverse()
print("Reversed extracted elements:",fiveNumberArrayCopy)