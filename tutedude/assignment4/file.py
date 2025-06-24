#Read a File and Handle Errors

#Some Variables
fileName='sample.txt'
read='r'

#Logic for Read File and Handling File Not Found Error
try:
    with open(fileName,read) as file:
        reading_file = file.read()
        print('Reading file content:')
        print(reading_file)
        file.close()
except FileNotFoundError:
    print("Error: The file", fileName, "was not found.")

