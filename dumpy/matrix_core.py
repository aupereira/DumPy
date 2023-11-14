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

# import unittest
# from dumpy.matrix_st import scalar_mul, scalar_vector_mul, vector_vector_mul, vector_matrix_mul, matrix_vector_mul, matmul_thread

# class TestMatrix(unittest.TestCase):
    
#     def test_scalar_mul(self):
#         self.assertEqual(scalar_mul(2, 3), 6)
#         self.assertEqual(scalar_mul(0, 5), 0)
#         self.assertEqual(scalar_mul(-1, 4), -4)
        
#     def test_scalar_vector_mul(self):
#         self.assertEqual(scalar_vector_mul(2, [1, 2, 3]), [2, 4, 6])
#         self.assertEqual(scalar_vector_mul(0, [1, 2, 3]), [0, 0, 0])
#         self.assertEqual(scalar_vector_mul(-1, [1, 2, 3]), [-1, -2, -3])
        
#     # def test_vector_vector_mul(self):
#     #     self.assertEqual(vector_vector_mul([1, 2, 3], [4, 5, 6]), 32)
#     #     self.assertEqual(vector_vector_mul([0, 1, 0], [1, 0, 1]), 0)
#     #     self.assertEqual(vector_vector_mul([-1, 2, -3], [4, -5, 6]), 0)
        
#     # def test_vector_matrix_mul(self):
#     #     self.assertEqual(vector_matrix_mul([1, 2, 3], [[4, 5], [6, 7], [8, 9]]), [40, 47])
#     #     self.assertEqual(vector_matrix_mul([0, 0, 0], [[1, 2], [3, 4], [5, 6]]), [0, 0])
#     #     self.assertEqual(vector_matrix_mul([1, 1, 1], [[-1, 2], [3, -4], [-5, 6]]), [-2, -1])
        
#     # def test_matrix_vector_mul(self):
#     #     self.assertEqual(matrix_vector_mul([[1, 2], [3, 4], [5, 6]], [1, 2]), [5, 11, 17])
#     #     self.assertEqual(matrix_vector_mul([[0, 0], [0, 0], [0, 0]], [1, 2]), [0, 0, 0])
#     #     self.assertEqual(matrix_vector_mul([[-1, 2], [3, -4], [-5, 6]], [1, 1]), [-1, -1, -1])
        
#     def test_matmul_thread(self):
#         self.assertEqual(matmul_core([[1, 2], [3, 4]], [[5, 6], [7, 8]]), [[19, 22], [43, 50]])
#         self.assertEqual(matmul_core([[0, 0], [0, 0]], [[1, 2], [3, 4]]), [[0, 0], [0, 0]])
#         self.assertEqual(matmul_core([[-1, 2], [3, -4]], [[1, 1], [1, 1]]), [[1, 1], [-1, -1]])
        
# if __name__ == '__main__':
#     unittest.main()