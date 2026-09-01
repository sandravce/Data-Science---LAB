# Write a Python program to open a file and copy the contents to another file.

source_file = open("file1.txt", "r")
contents = source_file.read()
source_file.close()

destination_file = open("file2.txt", "w")
destination_file.write(contents)
destination_file.close()

print("Contents copied successfully.")
