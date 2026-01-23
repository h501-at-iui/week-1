

# add code below ...

# Create a function palindrome(word) that receives a string and returns True or False depending on whether it is a palindrome.
# You can design the function to change all letters to lowercase and ignore spaces.

# Function - change letters to lowercase
def lowercase(input_string):
    return input_string.lower()

# Function - remove spaces
def remove_spaces(input_string):
    return input_string.replace(" ", "")

# Main function - palindrome check
def palindrome(word):
    word = lowercase(word)
    word = remove_spaces(word)
    if word == word[::-1]:
        return True
    else:
        return False
    
# Test program
print(palindrome("Can NaC"))