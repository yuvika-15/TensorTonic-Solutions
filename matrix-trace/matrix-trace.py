import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    A= np.array(A)
    m,n = A.shape

    trace=0
    for i in range (min(m,n)):
        trace += A[i,i]
    
    return trace
