import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    A=np.array(A)
    m,n =A.shape
    A_t= np.zeros((n,m))
    for i in range (m):
        for j in range (n):
            A_t[j,i] = A[i,j]
    
    return A_t 
        
    
