#!/usr/bin/env python3
from functools import reduce
import numpy as np 

def matrix_power(a, n):
    size = a.shape[0]  
    
    if n == 0:
        return np.identity(size, dtype=int)   
    
    if n < 0:
        a = np.linalg.inv(a)  
        n = -n  

   
    result = reduce(lambda x, _: x @ a, range(n), np.identity(size))

    return result   

def main():
    a = np.array([[1, 2, 3],
                  [4, 5, 0],
                  [7, 8, 9]])
    
    print(matrix_power(a, 0))  
    print(matrix_power(a, 2))  
    print(matrix_power(a, -8)) 

if __name__ == "__main__":
    main()
