'''
This problem is concerned with deleting repeated elements from a sorted array.

Write a program which takes as input a sorted int[] and updates it such that:

- all duplicates have been removed
- all remaining valid elements have been shifted left to fill the emptied indices
- all remaining empty indices have values set to 0
- the function returns the number of remaining valid elements (the array size minus the number of removed elements)

For example, given an input array with the values {2,3,5,5,7,11,11,11,11,13}, after the function completes, the values
    in the array should be {2,3,5,7,11,13,0,0,0}, and the function should return 6.

Hint: There is an O(n) time and O(1) space solution.
'''

input_1 = [2, 3, 5, 5, 7, 11, 11, 11, 11, 13]
input_2 = [1, 1, 1, 1, 1, 2, 3, 3, 3, 3, 3]
input_3 = [1]
input_4 = [2, 2, 2]
input_5 = [1, 2, 3, 3, 4, 5, 6, 6, 6, 7, 8, 8, 9]
input_arrays = [input_1, input_2, input_3, input_4, input_5]

def removeDuplicates(array):

    # If input array is empty or has 1 element
    if not array or len(array) <= 1:
        return array

    # Index of unique value
    unique = 0
    # Store last unique value
    unique_val = array[unique]

    # Store all unique values to front of array
    for val in array[1:]:
        # Store new unique values in next location
        if val != unique_val:
            unique += 1
            array[unique] = val
            unique_val = val

    unique += 1
    # Occupy remaining spaces with 0
    while unique < len(array):
        array[unique] = 0
        unique += 1

    return array

for input_array in input_arrays:
    print "With duplicates: \t{}" .format(input_array)
    print "Without duplicates: {}" .format(removeDuplicates(input_array))
    print ""
