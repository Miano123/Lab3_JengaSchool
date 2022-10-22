# Printing individual characters of a string seperated by open 
# and close parentheses.

def main():
    str = "This sentence has 27 chars."
    for c in str:
        print(f"({c})", end="")
main()
