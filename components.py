import numpy as np
from preset_data import *

def dot(a, b):
    if a.shape[1] != b.shape[0]:
        raise ValueError("Invalid matrix shapes")
        
    m, n = a.shape
    _, p = b.shape

    output = np.zeros((m, p))
    
    for i in range(m):
        for j in range(p):
            for k in range(n):
                output[i, j] += a[i, k] * b[k, j]
    return output
    
    

a_b = dot(a,c)

print(a_b)
np.dot(a,c)