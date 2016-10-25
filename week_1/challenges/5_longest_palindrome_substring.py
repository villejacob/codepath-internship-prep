'''
Write a program which takes a String as input and returns a String which is the longest palindromic substring in the
input, given the following assumptions about the input string:

its maximum length is 1000
it contains one unique, longest palindromic substring
Examples:

"abdbabbdba" should return "abdba"
"abdbbbbdba" should return "abdbbbbdba"
'''

def longestPalindromeSubstring(input_string):

    max_length = 1

    start = 0
    end = 0

    # Treat each character as center of palindrome, then iterate outwards O(n^2)
    for i in xrange(1, len(input_string)):

        # Even length substring
        low = i - 1
        high = i
        while low >= 0 and high < len(input_string) and input_string[low] == input_string[high]:
            if high - low + 1 > max_length:
                max_length = high - low + 1
                start = low
                end = high
            low -= 1
            high += 1

        # Odd length substring
        low = i
        high = i
        while low >= 0 and high < len(input_string) and input_string[low] == input_string[high]:
            if high - low + 1 > max_length:
                max_length = high - low + 1
                start = low
                end = high
            low -= 1
            high += 1

    return max_length, input_string[start:end+1], all_palindromes


print longestPalindromeSubstring("abdbbbbdba")