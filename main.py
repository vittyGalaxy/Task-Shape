from matplotlib import pyplot as plt
import math
import numpy as np


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
        circle = plt.Circle((0.5, 0.5), self.number)
        fig, ax = plt.subplots()
        ax.axis("equal")
        ax.set_xlim([(self.number * (-1)), self.number])
        ax.set_ylim([(self.number * (-1)), self.number])

        ax.add_patch(circle)
        plt.show()

    def calculate_area(self):
        return 3.14 * pow((self.number * 2) / 2, 2)

    def calculate_perimeter(self):
        return self.number * (2 * 3.14)


class Parable(Shape):
    def draw(self):
        a = 1
        b = 0
        c = 0

        x = np.linspace(-10, 10, 400)
        y = a * pow(x, 2) + b * x + c
        plt.plot(x, y, label=f'Parabola: $y = {a}x^2 + {b}x + {c}$')

        plt.xlabel('x')
        plt.ylabel('y')
        plt.title("Grafico di una parabola")
        plt.legend()
        plt.grid(True)

        plt.show()


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


def main():
    c = Circle(5)
    d = Parable(2)
    print(c.draw())
    print(c.draw(d.draw()))


if __name__ == '__main__':
    main()