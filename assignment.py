# Read from a file
with open("ramadhan.txt", "r") as file:
    content = file.read()
# Modify the content to remove words in "ramadhan.txt"  
modified_content = content.replace("holy", "one of the holiest")  

with open("ramadhan.txt", "w") as file:
    file.write(modified_content)

# print("File has been successfully modified and saved!")
print("replacements done and saved successfully!")




