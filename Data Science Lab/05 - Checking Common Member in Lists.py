# Write a Python program that takes two lists and returns
# True if they have at least one common member.

list1 = [10, 20, 30]
set1 = set(list1)  # Convert list to set

list2 = [40, 50, 60]
set2 = set(list2)  # Convert list to set

result = set1 & set2  # Find common elements

# If there is no common element
if result == set():
    print("False")
else:
    print("True")
