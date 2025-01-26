#!/usr/bin/env python3

def find_matching(L, pattern):
    ret_list=[]
    for i,words in enumerate(L):
        if pattern in words:
            ret_list.append(i)
            
    return ret_list

def main():
    pass

if __name__ == "__main__":
    main()
