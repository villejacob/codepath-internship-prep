'''
Alice is a teacher with a class of n children, each of whom has been assigned a numeric rating. The classroom is seated
in a circular arrangement, with Alice at the top of the circle. She has a number of gold stars to give out based on each
child's rating, but with the following conditions:

Each child must receive at least one gold star
Any child with a higher rating than his or her immediate neighbor should get more stars than that neighbor
Assuming n >= 3, what is the minimum total number of stars Alice will need to give out?

Write a program which takes as its input an int[] containing the ratings of each child, ordered by seating position,
and returns an int value for the minimum total number of stars that Alice will need to give out.

Hint: this problem can be solved with an algorithm that runs in O(n) time.

For example:

In a class of three children with ordered ratings of {1, 2, 2}, Alice will need to give out {1, 2, 1} stars accordingly,
for a total number of 4 stars overall.
'''

def giveStars(ratings):

    stars = [1]

    # From left to right -> keep track of increasing rating
    #   Python syntax: enumerate creates index i when looping through ratings
    #   ra
    for i, rating in enumerate(ratings[1:], 1):
        # When the next child has more stars, increment last stars value
        if rating > ratings[i - 1]:
            stars.append(stars[i - 1] + 1)
        # BONUS: if same rank, same stars
        elif rating == ratings[i - 1]:
            stars.append(stars[i - 1])
        # When next child has less rank, reset stars to 1
        else:
            stars.append(1)

    # From right to left <- keep track of increasing rating (aka decreasing rating when going left to right)
    for i, rating in enumerate(reversed(ratings[:len(ratings)-1]), 1):
        # equivalent index of the array when not reversed
        j = len(ratings) - i - 1
        # If current element to the left is larger than the element on the right
        if rating > ratings[j+1]:
            # If the stars given to the child with more rank is not more than the child with less rank, give 'em more
            if stars[j] <= stars[j+1]:
                stars[j] = stars[j+1] + 1

    star_count = 0
    for star in stars:
        star_count += star

    return star_count


print giveStars([1, 2, 2, 3, 4, 5, 3, 2, 5, 4, 3, 2, 1])