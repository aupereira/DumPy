def scalar_mul(A, B):
    return A * B

def scalar_vector_mul(A, B):
    output = []
    for i in range(len(B)):
        output.append(A * B[i])
    return output

# def vector_vector_mul(A, B):
#     output = 0
#     for i in range(len(A)):
#         output += A[i] * B[i]
#     return output

# def vector_matrix_mul(A, B):
#     output = []
#     for r in range(len(B[0])):
#         sum = 0
#         for c in range(len(A)):
#             sum += A[c] * B[c][r]
#         output.append(sum)
#     return output

# def matrix_vector_mul(A, B):
#     output = []
#     for r in range(len(A)):
#         sum = 0
#         for c in range(len(B)):
#             sum += A[r][c] * B[c]
#         output.append(sum)
#     return output

# Yes, this DOES contain for loops, and those for loops are way faster than
# generator objects. Deal with it.
def matmul_core(A, B, list=None):
    res = []
    for r in range(len(A)):
        row = []
        for c in range(len(B[0])):
            sum = 0
            for i in range(len(A[0])):
                sum += A[r][i] * B[i][c]
            row.append(sum)
        res.append(row)
    if list == None:
        return res
    list.extend(res)