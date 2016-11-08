'''
Anagram
'''


def string_anagram(string):

    # Get input when using STDIN
    # n = int(raw_input())
    # for i in xrange(0, n):

    for word in string.split():

        # str_a = raw_input()
        str_a = word
        len_a = len(str_a)

        # Not possible when odd
        if len_a % 2 != 0:
            print -1
            # continue

        # Define the two strings
        str_b = str_a[(len_a / 2):]
        str_a = str_a[:(len_a / 2)]

        # Dictionaries to story characters in each string and the number of occurrences
        a_dict = {}
        b_dict = {}

        diff = 0

        # Count occurrences of each value in the first string
        for char in str_a:
            if char in a_dict:
                a_dict[char] += 1
            else:
                a_dict[char] = 1

        for char in str_b:
            if char in b_dict:
                b_dict[char] += 1
            else:
                b_dict[char] = 1

        for char, count in b_dict.items():
            if char in a_dict:
                diff += abs(a_dict[char] - b_dict[char])
            # else:
                # diff += b_dict[char]

        print a_dict
        print b_dict
        print diff


input_string = "aaaaab"
string_anagram(input_string)
