'''
A palindrome is a word, phrase, or sequence of characters that reads the same backward as forward, e.g., madam or nurses run.

Write a program which takes a String as input and returns a boolean value which is true if the input is a palindrome and false if it is not, considering only alphanumeric characters and ignoring case.

Example:

"A man, a plan, a canal: Panama" is a palindrome and should return true
"race a car" is not a palindrome and should return false
'''

def isPalindrome(input_string):

    # Parse the string to only recieve alphanumeric characters, convert to lowercase
    string = ''.join(filter(str.isalpha, input_string))
    string = string.lower()

    # Pointers to first and last characters in the string
    start = 0
    end = len(string) - 1

    # Check if characters on opposite ends are equal, continue inwards when equal, else false
    while start <= end:
        if string[start] != string[end]:
            return False
        else:
            start += 1
            end -= 1
    return True

print isPalindrome("race a car")
