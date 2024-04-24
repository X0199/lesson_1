import math

class Triangle:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        if a + b > c or a + c > b or b + c > a:
            print("True triangle: ")
        else:
            raise Exception("Triangle does not exist!")
    def sides(self):
        print(f"The sides of the triangle are {self.a}, {self.b}, {self.c}.")

    def p(self):
        pers = self.a + self.b + self.c
        print(f"The perspective of the triangle is {pers}.")

    def pyut(self):
        if self.a ** 2 == self.b ** 2 + self.c ** 2 or self.b ** 2 == self.a ** 2 + self.c ** 2 or self.c ** 2 == self.b ** 2 + self.a ** 2:
            print("The triangle is rectangular.")
        elif self.a == self.b == self.c:
            print("The triangle is equilateral.")
        elif self.a != self.b != self.c:
            print("The triangle is calene.")
        elif self.a == self.b != self.c or self.a == self.c != self.b or self.b == self.c != self.a:
            print("The triangle is isosceles.")

    def surface(self):
        p = (self.a + self.b + self.c) / 2
        s = math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        print(f"The surface of the triangle is {s}")


triangle = Triangle(5,3,4)
triangle.sides()
triangle.p()
triangle.pyut()
triangle.surface()