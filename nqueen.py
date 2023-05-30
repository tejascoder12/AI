# n decides the size of the board
n = 5
# a is a 2-D array to hold the board and following code initializes a with zeros
a = [[0 for _ in range(n)] for _ in range(n)]
# b is a dictionary (like map) that stores key-value pairs. It is used to store row a
b = {}

# To check if the column is safe
def isColumnSafe(r, c):
    while r >= 0:
        if a[r][c] == 1:
            return False
        r = r - 1
    return True

# To check if the left diagonal is safe
def isLeftDiagonalSafe(r, c):
    while r >= 0 and c >= 0:
        if a[r][c] == 1:
            return False
        r = r - 1
        c = c - 1
    return True

# To check if the right diagonal is safe
def isRightDiagonalSafe(r, c):
    while r >= 0 and c < n:
        if a[r][c] == 1:
            return False
        r = r - 1
        c = c + 1
    return True

# Function to check if the given row and column position is safe or not.
# Returns False if not safe, else True
def isSafe(row, col):
    if not isColumnSafe(row, col):
        return False
    if not isLeftDiagonalSafe(row, col):
        return False
    if not isRightDiagonalSafe(row, col):
        return False
    return True

# Recursive function to check row-wise safe position for each queen (n).
def checkBoard(r, c):
    if r >= n:
        return True

    for col in range(c, n):
        if isSafe(r, col):
            a[r][col] = 1
            b[r] = col
            if checkBoard(r + 1, 0):
                return True
            a[r][col] = 0
            del b[r]

    return False

if __name__ == '__main__':
    if checkBoard(0, 0):
        print("Solution exists. Board configuration:")
        for row in a:
            print(row)
    else:
        print("No solution exists for the given board size.")
