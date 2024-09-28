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
    def __init__(self, r):
        super().__init__(r)
        self.r = r

    def draw(self):
        t = np.linspace(0, 2 * np.pi, 400)
        x = self.r * np.cos(t)
        y = self.r * np.sin(t)
        plt.plot(x, y, label=f'Circonferenza: $r = {self.r}$')
        plt.gca().set_aspect('equal')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Grafico di una circonferenza')
        plt.legend()
        plt.grid(True)
        plt.show()

    def calculate_area(self):
        return 3.14 * pow((self.number * 2) / 2, 2)

    def calculate_perimeter(self):
        return self.number * (2 * 3.14)


class Parable(Shape):
    def __init__(self, a, b, c):
        super().__init__(a)
        self.b = b
        self.c = c

    def get_b(self):
        return self.b

    def get_c(self):
        return self.c

    def draw(self):

        a = self.number
        b = self.b
        c = self.c

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
    def __init__(self, a, b):
        super().__init__(a)
        self.b = b
        self.a = self.number

    def get_b(self):
        return self.b

    def draw(self):
        t = np.linspace(0, 2 * np.pi, 400)

        x = self.a * np.cos(t)
        y = self.b * np.sin(t)
        plt.plot(x, y, label=f'Ellisse: $x^2/{self.a^2} + y^2/{self.b^2} = 1$')
        plt.gca().set_aspect('equal')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Grafico di un ellisse')
        plt.legend()
        plt.grid(True)
        plt.show()

    def calculate_area(self):
        return 3.14 * self.a * self.b

    def calculate_perimeter(self):
        return 2 * 3.14 * math.sqrt((pow(self.a, 2) + pow(self.b, 2)) / 2.0)


def main():
    c = Circle(5)
    d = Parable(1, 5, 2)
    s = Ellipse(5, 3)
    print(c.draw())
    print(d.draw())
    print(s.draw())


if __name__ == '__main__':
    main()