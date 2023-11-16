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

# def tensor_product(A, B):
#     output = []
#     for i in range(len(A)):
#         output.append(scalar_vector_mul(A[i], B))
#     return output