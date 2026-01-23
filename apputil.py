

# add code below ...

# Exercise 1:

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

# Exercise 2:

# Write a function parentheses(sequence) that takes a string and returns True if the string's parentheses are balanced, False if not.
# Try to come up with a second way to complete the problem.

# Main function - uses .count() method to check for balanced parentheses
def parentheses(sequence):
    if sequence.count("(") == sequence.count(")"):
        return True
    else: 
        return False
    
# Test program
print(parentheses("(here is a word) and (here is another word) and (here is not"))
print(parentheses("(But here is a word) and (here is another word) and (here is the last word)"))

# Second function - iterate through the string to check parentheses balance out
def parentheses_v2(sequence):
    balance = 0
    for char in sequence:
        if char == "(":
            balance += 1
        elif char == ")":
            balance -= 1
        
    if balance == 0:
        return True
    else:
        return False
    
# Test program
print(parentheses_v2("(Here is one) and here is not)"))
print(parentheses_v2("(And here is one) and (here is two)"))