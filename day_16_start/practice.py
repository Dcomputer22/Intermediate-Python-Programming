class Rectangle:
    length = 0
    breadth = 0

    def calculate_area(self):
        print(f"Area of a rectangle:", self.length * self.breadth )

my_rectangle = Rectangle()
my_rectangle.breadth = 12
my_rectangle.length = 10
my_rectangle.calculate_area()