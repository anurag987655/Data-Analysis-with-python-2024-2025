import numpy as np

def diamond(n):
    if n == 1:
        return np.array([[1]])
    
    identity = np.eye(n, dtype=int)
    remaining_column = np.fliplr(identity[:, :-1])
    merge = np.concatenate((identity, remaining_column), axis=1)
    
    row_rem = np.flipud(merge[1:, :])
    
    final = np.concatenate((row_rem, merge), axis=0)
    
    return final

def main():
    print(diamond(2))

if __name__ == "__main__":
    main()