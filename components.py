import numpy as np

class Linalg:
    def __init__():
        pass

    # dot product - used to compute angles and matrix multiplication
    @staticmethod
    def matdot(a, b):
        # The column size of shape A should match row size of of shape B
        # This is standard with the dot product in matrices
        if a.shape[1] != b.shape[0]:
            raise ValueError("Invalid matrix shapes")
            
        m, n = a.shape
        _, p = b.shape

        output = np.zeros((m, p))
        
        # Performs dot product and stores it in output matrix
        # output matrix shape: (matrix A row, matrix B col)
        for i in range(m):
            for j in range(p):
                for k in range(n):
                    output[i, j] += a[i, k] * b[k, j]
        return output
    
        # Ex. A = 2x2, B = 2x1
        # A = [[1, 2], [3,4]], B = [[5],[6]]
        # 1. 1*5=5 + 2*6=12 => 17
        # 2. 3*5=15 + 4*6=24 => 39
        # 3. Store in 2x1 matrix => [[17],[39]]

    # cross product - for 3D vectors: to find new vector parallel to the original plane
    @staticmethod
    def cross(a, b):
        expected_vector = (3,)
        if a.shape != expected_vector or b.shape != expected_vector:
            raise ValueError("Invalid vector shapes")

        # computing (i,j,k) in 3D vector
        i = (a[1] * b[2]) - (a[2] * b[1])
        j = -((a[0] * b[2]) - (a[2] * b[0]))
        k = (a[0] * b[1]) - (a[1] * b[0])

        return np.array([i,j,k])
    
        # Ex. a = <1,0,2>, b = <2,-1,3>
        # 1. i = (0*3) - (2*-1) = 2
        # 2. j = -(1*3) - (2*2) = 1
        # 3. k = (1*-1) - (0*2) = -1
        # output vector = <2,1,-1>
            



    
    

