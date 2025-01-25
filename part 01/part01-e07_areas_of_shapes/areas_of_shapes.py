import math

def triangle():
    b = float(input("Give base of the triangle: "))
    h = float(input("Give height of the triangle: "))
    area = 0.5 * b * h
    print(f"The area is {area:.6f}")

def rectangle():
    l = float(input("Give width of the rectangle: "))
    b = float(input("Give height of the rectangle: "))
    area = l * b
    print(f"The area is {area:.6f}")

def circle():
    r = float(input("Give radius of the circle: "))
    area = math.pi * r * r
    print(f"The area is {area:.6f}")

def main():
    while True:
        shape = input("Choose a shape (triangle, rectangle, circle): ").strip().lower()
        
        if not shape:
            break
        
        if shape == "triangle":
            triangle()
        elif shape == "rectangle":
            rectangle()
        elif shape == "circle":
            circle()
        else:
            print("Unknown shape!")

if __name__ == "__main__":
    main()
