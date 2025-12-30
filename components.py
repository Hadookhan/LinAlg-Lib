import numpy as np

class Linalg:
    def __init__():
        pass

    @staticmethod
    def dot(a, b):
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
    
    

