"""
    Exercise 10: Check if all items in the tuple are the same
    tuple1 = (45, 45, 45, 45)
    Expected output:

    True
"""

def cheak(t):
    return all(i == t[0] for i in t)

tuple1 = (45, 45, 45, 45)

print(cheak(tuple1))