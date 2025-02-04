#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    x=[]
    with open(filename,"r") as f:
        pattern=r'\s*(\d+)\s+(\d+)\s+(\d+)\s+(\w+\s*\w+)'
        for line in f:
            match=re.search(pattern,line)
            if match:
                x.append(match.group(1)+"\t"+match.group(2)+"\t"+match.group(3)+"\t"+match.group(4))
            
    return x


def main():
    for item in red_green_blue():
        print (item)

if __name__ == "__main__":
    main()
