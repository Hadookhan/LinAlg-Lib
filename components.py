import numpy as np

class Linalg:
    def __init__():
        pass

    
    @staticmethod
    def matdot(a: np.array, b: np.array) -> np.array:
        """
            Matrix Dot Product - used to compute angles and matrix multiplication

            Ex. A = 2x2, B = 2x1
            A = [[1, 2], [3,4]], B = [[5],[6]]
            1. 1*5=5 + 2*6=12 => 17
            2. 3*5=15 + 4*6=24 => 39
            3. Store in 2x1 matrix => [[17],[39]]
        """

        # The column size of shape A should match row size of of shape B
        # This is standard with the dot product in matrices
        if a.shape[1] != b.shape[0]:
            raise ValueError("Invalid A shapes")
            
        m, n = a.shape
        _, p = b.shape

        output = np.zeros((m, p))
        
        # Performs dot product and stores it in output A
        # output A shape: (A A row, A B col)
        for i in range(m):
            for j in range(p):
                for k in range(n):
                    output[i, j] += a[i, k] * b[k, j]
        return output
    
        
    
    
    @staticmethod
    def determinant(A) -> int:
        """
            Find determinant for 2x2 and 3x3 matrices
        """
        A = np.asarray(A) # enforce A as nparray
        if A.shape == (2, 2):
            return (A[0,0]*A[1,1]) - (A[0,1]*A[1,0])
        elif A.shape == (3, 3):
            det = 0
            
            det += A[0,0] * ((A[1,1]*A[2,2]) - (A[1,2]*A[2,1])) # calculating i val
            det -= A[0,1] * ((A[1,0]*A[2,2]) - (A[1,2]*A[2,0])) # calculating j val
            det += A[0,2] * ((A[1,0]*A[2,1]) - (A[1,1]*A[2,0])) # calculating k val
        
            return det
        else:
            raise ValueError("A must be square 2x2 or 3x3")

    @staticmethod
    def transpose(A) -> np.array:
        """
            Calculate Transpose of Matrix A
        """
        r, c = A.shape
        A_T = np.zeros((c,r))

        for i in range(r):
            for j in range(c):
                A_T[j,i] = A[i,j]
        return A_T


    # TODO: FIX THIS
    @staticmethod
    def cofactor(A) -> np.array:
        """
            Calculate Cofactor Expansion of Matrix A
        """
        r, c = A.shape

        cofact = -1

        coeffs = [coeff for coeff in A[0,0:c]]

        # for 3x3 matrices
        def sub_matrix(M, row, col) -> np.array:

            del_r = M[row:]
            del_c = M[:col]

            r, c = M.shape

            sub = np.zeros((2,2))

            for i in range(r):
                for j in range(c):
                    if M[i,j] in del_r or M[i,j] in del_c:
                        continue
                    sub[i,j] = M[i,j]

            return sub

        A_C = np.zeros((r,c))

        for i in range(r):
            for j in range(c):
                coeff = coeffs[j]
                cofact *= i+j
                print(sub_matrix(A, i, j))
                sub_det = Linalg.determinant(sub_matrix(A, i, j))
                A_C[i,j] = cofact * (coeff * sub_det)

        
        return A_C

    @staticmethod
    def __adjoint(A) -> np.array:
        """
            Calculate Adjoint matrix of A (transpose of cofactor matrix)
        """
        pass

    @staticmethod
    def matinverse(A) -> np.array:
        """
            Calculate Inverse of matrix A
        """
        pass
        


    # Computes the vector between two points
    @staticmethod
    def vector_from_points(O: np.array, p: np.array) -> np.array:
        return p - O

    @staticmethod
    def cross(a: np.array, b: np.array) -> np.array:
        """
            Find Cross Product - for 3D vectors: to find new vector parallel to the original plane

            Ex. a = <1,0,2>, b = <2,-1,3>
            1. i = (0*3) - (2*-1) = 2
            2. j = -(1*3) - (2*2) = 1
            3. k = (1*-1) - (0*2) = -1
            output vector = <2,1,-1>
        """
        expected_vector = (3,)
        if a.shape != expected_vector or b.shape != expected_vector:
            raise ValueError("Invalid vector shapes")

        # computing (i,j,k) in 3D vector
        i = (a[1] * b[2]) - (a[2] * b[1])
        j = -((a[0] * b[2]) - (a[2] * b[0]))
        k = (a[0] * b[1]) - (a[1] * b[0])

        return np.array([i,j,k])
    
        
            



    
    

