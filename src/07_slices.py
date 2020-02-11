"""
Python exposes a terse and intuitive syntax for performing 
slicing on lists and strings. This makes it easy to reference
only a portion of a list or string. 

This Stack Overflow answer provides a brief but thorough
overview: https://stackoverflow.com/a/509295

Use Python's slice syntax to achieve the following:
"""

a = [2, 4, 1, 7, 9, 6]

# Output the second element: 4:
second_element = slice(1, 2)
print(a[second_element])

# Output the second-to-last element: 9
second_to_last = slice(4, 5)
print(a[second_to_last])

# Output the last three elements in the array: [7, 9, 6]
last_three_elements = slice(3, 6)
print(a[last_three_elements])


# Output the two middle elements in the array: [1, 7]
two_middle = slice(0, 4, 3)
print(a[two_middle])

# Output every element except the first one: [4, 1, 7, 9, 6]
except_first = slice(1, 6)
print(a[except_first])

# Output every element except the last one: [2, 4, 1, 7, 9]
except_last = slice(0, 5)
print(a[except_last])

# For string s...

s = "Hello, world!"
eight12 = slice(7, 12)
# Output just the 8th-12th characters: "world"
print(s[eight12])