#Create a Dictionary of Student Marks

#Student Object
studentObj={"Alice":85, "John":45, "Simon":67, "Richard":65}

#Input Field
studentInput=input("Enter the student's name: ")

#StudentNotFound Error Message Show
studentNotFound=studentObj.get(studentInput,"Student is not found")

#Logic

if studentInput in studentObj:
    print(f"{studentInput}'s marks:", studentObj[studentInput])
else:
    print(studentNotFound)
