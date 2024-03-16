import math
from decimal import Decimal, getcontext


class ErrorCalculator():
    # let's just define every parameter in init function

    def __init__(self):
        self.targetValue = self.getTargetValue()
        self.pi = Decimal(math.pi)
        # Set the precision to a higher value
        getcontext().prec = 28

    def getTargetValue(self):
        x = input("Provide targeted error rate (0-1) : ")

        while True:
            if 0<x< 1:

                return Decimal(x)
            else:
                print("please provide a valid error rate")


    def polyArea(self, p, a):
        # p is the number of the side
        # a is the distance from G to any angle
        # 0.5 * a ** 2 * sin (x)
        # x-angled isosceles triangle area formula
        # or//
        # calculate side length of the polygon
        # 1/2 * a * p * s
        side_length = Decimal('2') * a * Decimal(math.sin(math.pi / p))
        # either way, same result
        # calculate area of the polygon

        polygonArea = Decimal('0.5') * p * side_length * a
        return polygonArea

    def circleArea(self, r):
        areaCircle = self.pi * r ** Decimal('2')
        return areaCircle

    def percentDifference(self, p, r):
        EN = Decimal('100') * abs((self.circleArea(r) - self.polyArea(p, r)) / self.circleArea(r))
        return EN

    def errorFunction(self, targetError):
        r = Decimal('1')
        p = 3
        max_sides = 1000  # Maximum number of sides to prevent infinite loop

        while p < max_sides:
            errorValue = self.percentDifference(p, r)
            print(f"N = {p}, Error = {errorValue}")
            if errorValue < targetError:
                return p
            p += 1

        return None  # Return None if no suitable polygon is found within the maximum number of sides


calculator = ErrorCalculator()

target_p = calculator.errorFunction(calculator.targetValue)
if target_p is not None:
    print(f"The smallest N that gives an error below {calculator.targetValue} is: {target_p}")
else:
    print("No suitable polygon found within the maximum number of sides.")


