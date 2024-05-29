"""
Name : Loi Chai Lam
Date : 5/3/2018

Often poetic meters of some fixed beat length (per line) have some
rhythmic pattern composed of light and heavy syllables from the
source language (for example, English or Sanskrit). It is common to
treat the light syllable to measure as being 1 beat in length, while a
heavy syllable to measure as 2 beats.
In such a framework, given a fixed beat length of n, write a program
that can compute the total number of patterns involving light and/or
heavy syllables?
As an example, a line with a fixed beat length of 5 can be composed of a pattern that is light-light-heavy-light (1+1+2+1=5),
or heavy-light-heavy (2+1+2=5), or any one of the other six possible
patterns.

"""

light_syllable = 1
heavy_syllable = 2

n = 4


def total_number_of_pattern1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2  # because it can be (2) or (1,1), so 2 patterns
    else:
        return total_number_of_pattern1(n - light_syllable) + total_number_of_pattern1(n - heavy_syllable)


def total_number_of_pattern2(n, total_pattern):
    if n == 0:
        return total_pattern
    elif n == 1:
        return total_number_of_pattern2(n-1, 1 + total_pattern)
    elif n == 2:
        return total_number_of_pattern2(n-2, 2 + total_pattern)
    else:
        return total_number_of_pattern2(n - light_syllable, total_pattern) + total_number_of_pattern2(n - heavy_syllable, total_pattern)


print(total_number_of_pattern1(n))
print(total_number_of_pattern2(n, 0))
# 8
