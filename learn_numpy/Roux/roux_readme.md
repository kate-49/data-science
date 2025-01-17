Roux
Define a roux array as a 1-D array such that, when it's reversed, it represents the sequence of square numbers 1, 4, 9, 16, ... with 0s interwoven between them.

Examples

# roux array of length 5
[9 0 4 0 1]
# roux array of length 8
[ 0 16  0  9  0  4  0  1]
# roux array of length 12
[ 0 36  0 25  0 16  0  9  0  4  0  1]
Note: odd-length arrays begin with a square number while even-length arrays begin with a zero.

Implement a function called make_roux(n) that inputs n, the desired size of the array, and outputs the corresponding roux array. Then test it on the examples above.


def make_roux(n):
    """returns a roux array of length n"""

    # your code here