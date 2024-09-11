import numpy as np

A = np.random.randint(1, 10, (3, 3))
B = np.random.randint(1, 10, (3, 3))

sum_matrices = A + B

difference_matrices = A - B

product_matrices = np.dot(A, B)

hadamard_product = A * B

det_A = np.linalg.det(A)

inv_A = np.linalg.inv(A) if det_A != 0 else 'Ma tran A khong co nghich dao'

transpose_A = np.transpose(A)

pseudo_inv_A = np.linalg.pinv(A)

frobenius_norm_A = np.linalg.norm(A, 'fro')

norm_L1_rows = np.linalg.norm(A, 1, axis=1)
norm_L2_rows = np.linalg.norm(A, 2, axis=1)

submatrix_2x2 = A[:2, :2]

scalar_product = A * 2

symmetric_matrix = np.dot(A.T, A)

trace_A = np.trace(A)

eigenvalues, eigenvectors = np.linalg.eig(A)

is_diagonalizable = np.all(np.isreal(eigenvalues))

C = np.ones((3, 3))
sum_with_C = A + C

diag_vector = np.random.randint(1, 10, 3)
diagonal_matrix = np.diag(diag_vector)

is_orthogonal = np.allclose(np.dot(A.T, A), np.eye(3))

D = np.random.randint(1, 10, (4, 4))

inv_D = np.linalg.inv(D) if np.linalg.det(D) != 0 else 'Ma tran D khong co nghich dao'

D_squared = np.dot(D, D)
E = np.random.randint(1, 10, (4, 4))
E_inv = np.linalg.inv(E) if np.linalg.det(E) != 0 else 'Ma tran E khong co nghich dao'
E_squared = np.dot(E, E_inv)

D = np.dot(np.dot(A.T, B), A)
det_D = np.linalg.det(D)

inv_D = np.linalg.inv(D) if det_D != 0 else 'Ma tran D khong co nghich dao'

I = np.eye(4)
sum_with_I = D + I

vector_F = np.random.randint(1, 10, 3)
F = np.diag(vector_F)

is_diagonal_F = np.allclose(F, np.diag(np.diag(F)))

Z = np.eye(3)
product_F_Z = np.dot(F, Z)
is_equal_F = np.allclose(product_F_Z, F)

trace_F = np.trace(F)

print(f"A:\n{A}")
print(f"B:\n{B}")
print(f"Tong ma tran A va B:\n{sum_matrices}")
print(f"Chenh lech ma tran A va B:\n{difference_matrices}")
print(f"Tich ma tran A va B:\n{product_matrices}")
print(f"Tich Hadamard A va B:\n{hadamard_product}")
print(f"Det A: {det_A}")
print(f"Nghich dao A:\n{inv_A}")
print(f"Chuyen vi A:\n{transpose_A}")
print(f"Gia nghich dao Moore-Penrose A:\n{pseudo_inv_A}")
print(f"Chuan Frobenius A: {frobenius_norm_A}")
print(f"Norm L1 cua moi hang A:\n{norm_L1_rows}")
print(f"Norm L2 cua moi hang A:\n{norm_L2_rows}")
print(f"Ma tran con 2x2 o goc tren ben trai A:\n{submatrix_2x2}")
print(f"Phép nhân về hướng của A với a = 2:\n{scalar_product}")
print(f"Ma tran doi xung A^T x A:\n{symmetric_matrix}")
print(f"Trace cua A: {trace_A}")
print(f"Tri rieng va vector rieng cua A:\n{eigenvalues}\n{eigenvectors}")
print(f"Ma tran A co kha nang cheo hoa: {is_diagonalizable}")
print(f"Ma tran C:\n{C}")
print(f"Tong A va C:\n{sum_with_C}")
print(f"Ma tran duong cheo tu vector:\n{diagonal_matrix}")
print(f"Ma tran A co phai la ma tran truc giao: {is_orthogonal}")
print(f"Ma tran D:\n{D}")
print(f"Nghich dao D:\n{inv_D}")
print(f"Ma tran D x D:\n{D_squared}")
print(f"Ma tran E x E^-1:\n{E_squared}")
print(f"Ma tran D = A.T x B x A:\n{D}")
print(f"Det D: {det_D}")
print(f"Nghich dao D:\n{inv_D}")
print(f"Tong D va ma tran don vi I:\n{sum_with_I}")
print(f"Ma tran F:\n{F}")
print(f"Ma tran F co phai la ma tran cheo: {is_diagonal_F}")
print(f"Tich F x Z:\n{product_F_Z}")
print(f"Tich F x Z co bang F: {is_equal_F}")
print(f"Trace cua F: {trace_F}")
