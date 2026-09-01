# Write a python program to count number of lines in a file.

count = 0
file = open("file1.txt", "r")
for line in file:
    count = count + 1
print("Number of Lines:", count)
