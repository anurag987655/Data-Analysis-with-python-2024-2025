#!/usr/bin/env python3

# Don't modify the below hack
try:
    from src import triangle
except ModuleNotFoundError:
    import triangle

def main():
    # Call the functions from here
    b,p=(3,4)
    triangle.area(b,p)
    triangle.hypotenuse(b,p)

if __name__ == "__main__":
    main()
