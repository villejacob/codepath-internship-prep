'''
Write a program which takes a String[] as input and returns a String which is the longest common prefix,
or an empty string if there is none.

Examples:

{"bceefgh", "bcfghijk", "bcefgh"} should return "bc"
{"abcdefgh", "aefghijk", "abcefgh"} should return "a"
{"", "aefghijk", "abcefgh"} should return ""
'''


def longestCommonPrefix(input_strings):

    # 0(nk) where n is the number of strings and k is the length of the common prefix

    prefix = ""

    # For each of the characters in the length of the first string
    for i in xrange(len(input_strings[0])):
        # Store the current character
        current = input_strings[0][i]
        # Compare this character against the other strings at the same index
        for string in input_strings:
            if current != string[i]:
                # When a string has a different value, return the last valid prefix
                return prefix
        # Add this new character to the prefix
        prefix += current

    return prefix


print longestCommonPrefix(["abcdef", "abcdgef", "abcdef"])
