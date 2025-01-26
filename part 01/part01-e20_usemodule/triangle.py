# Enter you module contents here
# Module metadata
"""This module provides way to calculate the properties of right angled traingle."""
__version__ = "1.0.0"
__author__ = "Anurag Acharya"

def hypotenuse(b, p):
    """
    Calculate the hypotenuse of a right-angled triangle.

    Parameters:
        b (float): Length of the base of the triangle.
        p (float): Length of the perpendicular (height) of the triangle.

    Returns:
        float: Length of the hypotenuse.
    """
    return (b**2 + p**2) ** 0.5

def area(b, p):
    """
    Calculate the area of a right-angled triangle.

    Parameters:
        b (float): Length of the base of the triangle.
        p (float): Length of the perpendicular (height) of the triangle.

    Returns:
        float: Area of the triangle.
    """
    return 0.5 * b * p

if __name__ == "__main__":
    
    base, perpendicular = 3, 4
    print(f"Hypotenuse of a triangle with base {base} and perpendicular {perpendicular}: {hypotenuse(base, perpendicular)}")
    print(f"Area of a triangle with base {base} and perpendicular {perpendicular}: {area(base, perpendicular)}")

