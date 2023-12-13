def printvec(v, round=3):
    """Prints a vector."""
    print("[ ", end="")
    for i in range(len(v)):
        print(round(v[i], round), end=" ")
    print("]")

def printmat(A, round=3):
    """Prints a matrix."""
    for i in range(len(A)):
        print("[ ", end="")
        for j in range(len(A[0])):
            print(round(A[i][j], round), end=" ")
        print("]")