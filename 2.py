#2
from scipy.linalg import solve

A = np.array([
    [1, 2, 3],
    [2, 5, 3],
    [3, 2, 2]
])
B = np.array([7, 4, 5])

X = solve(A, B)
print("Nghiệm của hệ phương trình là:", X)
#3

A = np.array([
    [1, -1, 2],
    [2, 3, 1],
    [4, 2, -1]
])

B = np.array([3, 5, 7])

X = np.linalg.solve(A, B)
print("Nghiệm của hệ phương trình là:", X)

