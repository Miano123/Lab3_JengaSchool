def main():
    for i in range(20):
        print("X"*i) # Prints out "X" 1-19 in a triangular shape.
        print "X"*(2*i) # Output missing parentheses error.
        print"X"*i + "O"*i # Error missing parentheses.
        print"X"*i + "O"*(20-i) # Error missing parentheses.
main()
