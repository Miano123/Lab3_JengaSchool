# use for loop with different range to print out the string

def main():
    str = "This sentence has 27 chars."
    for c in range(7):
        print(str[c], end="") #Prints out the first 6 letters of the string.

    for c in range(1,7):
        print(str[c], end="") #Prints out the second letter to 
                              #the 6th letter of the string.

    for c in range(len(str)):
        print(str[c], end="") #prints out the entire string.

main()
