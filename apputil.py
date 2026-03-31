def palindrome(word):
    word = word.lower()
    word = word.replace(",", "")
    word = word.replace(".", "")
    word = word.replace(" ", "")
    reversed_word = word[::-1]
    return word == reversed_word 
    
result = palindrome("Sit on a potato pan, otis")
print(result)

# add code below ...
def parentheses(sequence):
    if(sequence.startswith("(")) and sequence.endswith(")") and sequence.count('(') == sequence.count(')'):
        return True
    else:
        return False

parentheses("((((((()) ")
