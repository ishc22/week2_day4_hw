import math
def find_area(circumference):
    area = (circumference * circumference)/(4 * math.pi)
    print(f"Area Of a Circle {area:.2f}")

find_area(10)

def find_hypotenuse(side1, side2):
    hypotenuse = math.hypot(side1, side2)
    print(f"The hypotenuse of a right angle with sides measuring {side2}in {side1}in is {hypotenuse}in")

find_hypotenuse(3, 4) 