"""
    Exercise 3: Create a new string made of the first, middle, and last characters of each input string

    Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first, middle, and last characters.

    Given:

    s1 = "America"
    s2 = "Japan"
    Expected Output:

    AJrpan

"""

s1 = "America"
s2 = "Japan"

print(s1[0] + s2[0] + s1[3] + s2[2:])