# Example 1
# Write a program which prints area of Triangle
# area of Triangle is 1/2 * (base * height)

# Example 2
# Write a program which prints area of Square
# area of Square is 4 * side

# Example 3
# Create common class Shape which will print area of provided shape (either Triangle or Square)


class Shape:
    def __new__(cls, name, *args, **kwargs):
        if "Triangle" == name:
            return Triangle(*args, **kwargs)
        elif "Square" == name:
            return Square(*args, **kwargs)


class Triangle:
    base = None
    height = None

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return (self.base * self.height)/2


class Square:
    side = None

    def __init__(self, side):
        self.side = side

    def area(self):
        return 4 * self.side

# t1 = Triangle()
# t1.height = 4
# t1.base = 3
# area1 = t1.area()
# area = Triangle.area(t1)
# print(f'area1 is {area}')

t1 = Triangle(base=3, height=4)
area = t1.area()
print(f'area1 is {area}')

t1 = Square(side=4)
area = t1.area()
print(f'area1 is {area}')

s1 = Shape(name="Triangle", base=3, height=4)
area1 = s1.area()
print(f"area of shape1 is {area1}")

s2 = Shape(name="Square", side=4)
area2 = s2.area()
print(f"area of shape2 is {area2}")