#!/usr/bin/env python3

import scipy.stats
import numpy as np

def load():
    import pandas as pd
    return pd.read_csv("src/iris.csv").drop('species', axis=1).values

def lengths():
    a=load()#returns a vector whose first element is sepal length and 3rd is petal length
    r,p_val=scipy.stats.pearsonr(a[:, 0],a[:, 2])   
    return r

def correlations():
    a=load()
    r=np.corrcoef(a,rowvar=False)
    return r

def main():
    print(lengths())
    print(correlations())

if __name__ == "__main__":
    main()
