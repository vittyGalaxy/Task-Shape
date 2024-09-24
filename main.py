from matplotlib import pyplot as plt
import math


class Shape:
    def __init__(self, number):
        self.number = number

    def get_number(self):
        return self.number

    def draw(self):
        pass

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def draw(self):
        #todo
        pass

    def calculate_area(self):
        return 3.14 * pow((self.number * 2) / 2, 2)

    def calculate_perimeter(self):
        return self.number * (2 * 3.14)


class Parable(Shape):
    def draw(self):
        pass


class Ellipse(Shape):
    def __init__(self, number, number2):
        super().__init__(number2)
        self.number2 = number2

    def get_number2(self):
        return self.number2

    def draw(self):
        pass

    def calculate_area(self):
        return 3.14 * self.number * self.number2

    def calculate_perimeter(self):
        return 2 * 3.14 * math.sqrt((pow(self.number, 2) + pow(self.number2, 2)) / 2.0)