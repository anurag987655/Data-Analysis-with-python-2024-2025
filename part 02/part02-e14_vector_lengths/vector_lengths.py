#!/usr/bin/env python3

import numpy as np
#import scipy.linalg

def vector_lengths(a):
    return np.sqrt(np.sum(a*a,axis=1)) 

def main():
    a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    lengths = vector_lengths(a)
    print("Vector lengths:", lengths)


if __name__ == "__main__":
    main()
