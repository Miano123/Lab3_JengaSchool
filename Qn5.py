# For loop to print a reversed string.
def reverse_string(s):
    str1 = "" # Declaring an empty string to store the reverse string.
    for i in s:
        str1 = i + str1
    return str1 # returns the reverse string.
s = "This sentence has 27 chars."
print(reverse_string(s)) # Prints the reverse string.

# Using slice function to print a  reversed string.
my_string = "This sentence has 27 chars."
str1 = str[::-1]
print(str1)
