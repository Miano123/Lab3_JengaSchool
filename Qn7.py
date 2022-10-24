def main():
    std = ["Ali", 1, 2.5, "Elif", 2, 3.0]
    print(std[0]) #Output is the first index of the string "Ali"
    print(std[-1]) # Output is the last index of the string (3.0)
    print(type(std[2])) # output is the class type of 
                        # the third index of the string (2.5)
    print(std[3]) # Output is the 4th index of the string ("Elif")
    print(std[3][2] # Output is (i) which is the second index
                    # in the sublist ("Elif").
    print(std[0][1] # Output is the second index(l) in the 
                    #first sublist("Ali").
main()
