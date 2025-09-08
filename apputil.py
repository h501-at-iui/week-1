## Exercise 1
# Solution 1
# Write a function that determines whether or not a "word" is a 'palindrome' using .lower() and .replace()
# Define a 'palindrome'
def is_palindrome(word):
    # Normalize the word by removing spaces and converting to lowercase
    normalized_word = word.replace(" ", "").lower()
    # Check if the normalized word is the same forwards and backwards
    return normalized_word == normalized_word[::-1]
# Test cases
print(is_palindrome("Racecar"))  
print(is_palindrome("nurses run"))    
print(is_palindrome("Sit on a potato pan Otis")) 

# Solution 2
# Write a function that determines whether or not a "word" is a 'palindrome' by reversing the string
# Reverse the string using an if-else statement
# Define a 'palindrome'
def is_palindrome(word):
    # Reverse the string
    word_reversed = word[::1]
# After reversing the string, compare it to the original string
    if word_reversed == word:
        return True
    else:
        return False
# Test the function
print(is_palindrome("Racecar"))
print(is_palindrome("nurses run"))  
print(is_palindrome("Sit on a potato pan Otis"))


## Exercise 2
# Solution 1
# Write a function parentheses(sequence) and takes a string and returns True if the parentheses are balanced and False if they are not.
def parentheses(sequence):
    # Initialize a counter for open parentheses
    open_count = 0
    # Iterate through each character in the sequence
    for char in sequence:
        # Increment the counter for an open parenthesis
        if char == '(':
            open_count += 1
        # Decrement the counter for a close parenthesis
        elif char == ')':
            open_count -= 1
        # If the counter goes negative, there are unmatched closing parentheses
        if open_count < 0:
            return False
    # If the counter is zero, all parentheses are balanced
    return open_count == 0
    # Test cases
print(parentheses("(blah)()()()"))  # True
print(parentheses("((())blee)"))    # True
print(parentheses("(()hello((())()))"))  # True
print(parentheses("((((((())"))      # False
print(parentheses("()))"))          # False

# Solution 2
# Write a function parentheses(sequence) and takes a string and returns True if the parentheses are balanced and False if they are not.
# Alternative solution using a stack
# Define a parentheses function
def parentheses(sequence):
    # Initialize an empty stack
    stack = []
    # Using 'char' to move string to a list using if-elif statement
    for char in sequence:
        if char == '(':
            stack.append(char)
    # Check for closing parentheses and match with opening parentheses
        elif char == ')':
            if not stack:
                return False
    # If the stack is not empty, there are unmatched opening parentheses
            stack.pop()
    # Parentheses are balanced if the stack is empty
    return len(stack) == 0
# Test cases
print(parentheses("(blah)()()()"))  # True
print(parentheses("((())blee)"))    # True
print(parentheses("(()hello((())()))"))  # True
print(parentheses("((((((())"))      # False
print(parentheses("()))"))          # False