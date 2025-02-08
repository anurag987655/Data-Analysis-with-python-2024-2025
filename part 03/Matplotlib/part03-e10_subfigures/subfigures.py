#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def subfigures(a):
    x=a[:,0]
    y=a[:,1]
    c=a[:,2]
    d=a[:,3]
    
    plt.subplot(1,2,1)
    plt.plot(x,y,color='c')
    plt.title("Line Plot")
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    
    plt.subplot(1,2,2)
    plt.scatter(x,y,c=c,s=d)
    plt.title("Scatter Plot")
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    
    plt.show()

def main():
    data = np.array([
        [1, 2, 0.5, 30],
        [2, 3, 0.8, 50],
        [3, 5, 1.0, 70],
        [4, 7, 1.5, 90]])
    subfigures(data)

if __name__ == "__main__":
    main()
