'''
Given an natural language text, write an algorithm which will format the text by splitting it into lines of a specified
length, with each line justified such that the text is evenly spaced according to specific rules.

Inputs:

String text - the text to format
int length - the line length for the output
Output: a String[] that meets the following requirements:

Each line should have exactly length characters, including whitespace
Each line should contain as many words as will fit, and the algorithm should return as few lines as possible
Each line should be padded with spaces, distributed as evenly as possible
If the spaces required to pad a line don't divide evenly between words, add the extra spaces between the leftmost words.
Last line of the output should be left justified, with no extra spaces between words and all padding added to the right.
Example:

Given the inputs:

String text = "This is an example of text justification.";
int length = 16;
...the output array should be:

String[] output = {
  "This    is    an",
  "example  of text",
  "justification.  "
};
Hint: you can use String.split(" ") to tokenize the input into words.

Remember to avoid helper functions and libraries

Bonus 1

Add support for both left and right justification via a parameter. Use an enum to specify values for all three use
cases, with the above us case as the default. For left and right justification, the last line should be justified
the same as the rest of the text.

Using the above example inputs, the outputs for these two variants would look like this:

Left justification:

String[] output = {
  "This is an      ",
  "example of text ",
  "justification.  "
};
Right justification:

String[] output = {
  "      This is an",
  " example of text",
  "  justification."
};
'''

# def textJustification(text, length):
#
#     words = text.split()
#
#     justified = []
#     line = ""
#     line_words = []
#
#     for word in words:
#
#         print "\nline_words: {}" .format(line_words), word
#
#         # If there is still room to add another word
#         if len(word) + len(line) < length:
#             line_words.append(word)
#             line = " ".join(line_words)
#         # If next word exceeded spacing for one line
#         elif len(line_words) == 1:
#             to_add = length - len(line)
#             padding = " " * to_add
#             justified.append(line_words[0] + padding)
#             line_words = [word]
#         else:
#             to_add = length - len(line)
#             gaps = len(line_words) - 1
#
#             if gaps != 0:
#                 gaps_all = " " * ((to_add//gaps)+1)
#                 gaps_remain = to_add % gaps
#             else:
#                 gaps_all = " "
#                 gaps_remain = 0
#
#             remain = gaps_all + " "
#
#             remain_line = remain.join(line_words[:gaps_remain+1])
#             full_list = [remain_line] + line_words[gaps_remain+1:]
#             line = gaps_all.join(full_list)
#
#             justified.append(line)
#
#             line_words = [word]
#             line = ''.join(line_words)
#
#     # Last words
#     if len(line_words) != 0:
#         to_add = length - len(line)
#         padding = " " * to_add
#         justified.append(line_words[0] + padding)
#
#     print ""
#     return justified


def fullJustify(words, maxWidth):
    if not words:
        return []
    result = []
    i, j = 0, 0
    currentLen = 0
    while j < len(words):
        if currentLen + len(words[j]) <= maxWidth:
            currentLen += len(words[j]) + 1
            j += 1
        else:
            if i == j-1:
                result.append(words[i] + ' ' * (maxWidth - len(words[i])))
            else:
                number_of_interval = j-i-1
                total_length = sum(map(len, words[i:j]))
                total_space = maxWidth - total_length
                # total_space%number_of_interval  of total_space/number_of_interval +1 spaces
                # and the rest of total_space/number_of_interval spaces
                retStr = (" "*((total_space/number_of_interval)+1)).join(words[i: i+1+total_space%number_of_interval])
                retStr = (" "*((total_space/number_of_interval))).join([retStr] + words[i+1+total_space%number_of_interval:j])
                result.append(retStr)
            currentLen = 0
            i = j
    result.append(" ".join(words[i:j]).ljust(maxWidth))
    return result

text = "This is an example of text justification."
words = text.split()
ans = fullJustify(words, 16)

for line in ans:
    print line
