#!/usr/bin/env python3

def transform(s1, s2):
    list1=list(map(int,s1.split()))
    list2=list(map(int,s2.split()))
    z=[x*y for x,y in zip(list1,list2)]
    return z

def main():
    print(transform("1 5 3", "2 6 -1"))
    pass

if __name__ == "__main__":
    main()
