#!/usr/bin/env python3

def sum_equation(L):
    if not L:
        return "0 = 0"
    else:
        equation=" + ".join(map(str,L))
        total=sum(L)
    return f"{equation} = {total}" 
def main():
    pass

if __name__ == "__main__":
    main()
