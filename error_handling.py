filename = input("Enter the filename: ")

# input the correct file to open the text file "ramadhan.txt"
# it will display the content of the text file"
try:
    
    with open(filename, "r") as file:
        content = file.read()
        print("File content:\n", content)
# input an incorrect e.g "powerlearn.txt"  to open the a text file 
# it will display this Error: File not found. Please check the filename and try again."
except FileNotFoundError:
    print("Error: File not found. Please check the filename and try again.")
    
# if you change permision for text file('ramadhan.txt'), it will display this Error: File not found. Please check the filename and try again."
except PermissionError:
    print("Error: You don't have permission to read this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
