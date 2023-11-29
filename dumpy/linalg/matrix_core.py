def scalar_mul(A, B):
    return A * B

def scalar_vec_mul(A, B):
    output = []
    for i in range(len(B)):
        output.append(A * B[i])
    return output

def vec_vec_mul(A, B):
    output = 0
    for i in range(len(A)):
        output += A[i] * B[i]
    return output

def vec_mat_mul(A, B):
    output = []
    for i in range(len(B[0])):
        sum = 0
        for j in range(len(A)):
            sum += A[j] * B[j][i]
        output.append(sum)
    return output

# def mat_vec_mul(A, B):
#     output = []
#     for r in range(len(A)):
#         sum = 0
#         for c in range(len(B)):
#             sum += A[r][c] * B[c]
#         output.append(sum)
#     return output

def matmul_core_old(A, B, list=None):
    """Performs a matrix multiplication on two matrices."""
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

def matmul_core(A, B, list=None):
    """Performs a matrix multiplication on two matrices.
    \nExploits spatial locality by transposing the second matrix."""
    res = []
    for i in range(len(A)):
        row = []
        for j in range(len(B)):
            sum = 0
            for k in range(len(A[0])):
                sum += A[i][k] * B[j][k]
            row.append(sum)
        res.append(row)
    if list == None:
        return res
    list.extend(res)

# def tensor_product(A, B):
#     output = []
#     for i in range(len(A)):
#         output.append(scalar_vector_mul(A[i], B))
#     return output