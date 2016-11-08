'''

'''



def firstRepeatedWord(s):
    s = s.split()

    unique = {}

    for word in s:
        if word in unique:
            return word
        else:
            unique[word] = 1

