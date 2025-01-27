#!/usr/bin/env python3

import numpy as np

def get_rows(a):
    return [a[i] for i in range(len(a.T[0]))]#could have done directly as in solution using row for row in a 

def get_columns(a):
    return [a[:,i]for i in range(len(a[0]))]

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Rows:", get_rows(a))
    print("Columns:", get_columns(a))

if __name__ == "__main__":
    main()
