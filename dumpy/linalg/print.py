type Vector = list[float or int]
type Matrix = list[Vector]

def printvec(v: Vector, digits: int =3) -> None:
    """Prints a vector.

    Parameters:
        v (Vector): The vector to be printed.
        digits (int, optional): The number of decimal places to round the vector elements to. Default is 3.
    
    Returns:
        None
    """

    print("[ ", end="")
    for i in range(len(v)):
        print(round(v[i], digits), end=" ")
    print("]")

def printmat(A: Matrix, digits: int =3) -> None:
    """Prints a matrix.

    Parameters:
        A (Matrix): The matrix to be printed.
        digits (int, optional): The number of decimal places to round the vector elements to. Default is 3.
    
    Returns:
        None
    """
    
    for i in range(len(A)):
        print("[ ", end="")
        for j in range(len(A[0])):
            print(round(A[i][j], digits), end=" ")
        print("]")