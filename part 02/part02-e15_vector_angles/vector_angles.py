

import numpy as np
import scipy.linalg

def vector_angles(X, Y):
    product=np.sum(X*Y,axis=1)
    norm_x=scipy.linalg.norm(X,2,axis=1)
    norm_y=scipy.linalg.norm(Y,2,axis=1)
    
    result=product/(norm_x*norm_y)
    result=np.clip(result,-1,1)
    
    return np.degrees(np.arccos(result))

def main():
    X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    Y = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
    
    angles = vector_angles(X, Y)
    print("Angles between vectors (in degrees):", angles)

if __name__ == "__main__":
    main()
