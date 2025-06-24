#Write and Append Data to a File

#Some Variables
fileName='output.txt'
read_write='r+'
append='a'

#Logic

#Write
writeInput=input("Enter text to write to the file: ")

writeFile=open(fileName,read_write)
writing_file=writeFile.write(writeInput + '\n')
print('Data successfully written to',fileName,'.\n')
writeFile.close()

#Append
appendInput=input("Enter additional text to append: ")

appendFile=open(fileName,append)
append_file=appendFile.write(appendInput)
print("Data successfully appended.",'\n')
appendFile.close()

#Read
readFile=open(fileName,read_write)
reading_file=readFile.read()
print("Final content of", fileName,)
print(reading_file)
readFile.close()
