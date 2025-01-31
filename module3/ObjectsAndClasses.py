import logging

import matplotlib.pyplot as plt

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)


    class SimpleClass:
        field_with_default_and_without_contructor = 100

        def __init__(self, filed_with_constructor, filed_with_constructor_default=200):
            self.filed_with_constructor = filed_with_constructor
            self.filed_with_constructor_default = filed_with_constructor_default

        def describe(self):
            return f"SimpleClass(field_with_default_and_without_contructor={self.field_with_default_and_without_contructor}, filed_with_constructor={self.filed_with_constructor}, filed_with_constructor_default={self.filed_with_constructor_default}"


    logging.info(f"New object 'SimpleClass(5, 9)'={SimpleClass(5, 9).describe()}")
    logging.info(f"New object 'SimpleClass(3)'={SimpleClass(3).describe()}")


    class ShapeDrawer:
        def __init__(self, shapes=()):
            self.shapes = shapes

        def draw_shapes(self):
            for s in self.shapes:
                s.draw()
            plt.axis('scaled')
            plt.show()


    class Shape():
        def __init__(self, center=(0, 0)):
            self.center = center


    class Circle(Shape):
        def __init__(self, center_x=0, center_y=0, radius=0, color=None):
            super().__init__((center_x, center_y))
            self.radius = radius
            self.color = color

        def add_radius(self, radius):
            self.radius += radius
            return self.radius

        def draw(self):
            logging.info("Drawing a %s", self.describe())
            plt.gca().add_patch(plt.Circle(self.center, radius=self.radius, fc=self.color))

        def describe(self):
            return f"Circle(center={self.center}, radius={self.radius}, color={self.color})"


    class Rectangle(Shape):
        def __init__(self, center_x=0, center_y=0, height=0, width=0, color=None):
            super().__init__((center_x, center_y))
            self.height = height
            self.width = width
            self.color = color

        def draw(self):
            logging.info("Drawing a %s", self.describe())
            plt.gca().add_patch(plt.Rectangle(self.center, height=self.height, width=self.width, fc=self.color))

        def describe(self):
            return f"Rectangle(center={self.center}, radius={self.height}, radius={self.width}, color={self.color})"


    circle1 = Circle(60, 0, 10, "red")
    circle2 = Circle(-20, -20, 20, "yellow")
    circle3 = Circle()

    logging.info(
        f"We have a circle object {circle1} of type {type(circle1)} with attributes radius={circle1.radius} and color={circle1.color}")
    logging.info(
        f"We have a circle object {circle2} of type {type(circle2)} with attributes radius={circle2.radius} and color={circle2.color}")
    logging.info(
        f"We have a circle object {circle3} of type {type(circle3)} with attributes radius={circle3.radius} and color={circle3.color}")

    logging.info(f"We have a circle object {circle1} of type {type(circle1)}: %{circle1.describe()}")
    logging.info(f"We have a circle object {circle2} of type {type(circle2)}: %{circle2.describe()}")
    logging.info(f"We have a circle object {circle3} of type {type(circle3)}: %{circle3.describe()}")

    circle2.color = "blue"

    logging.info(
        f"adding 40 to radius {circle2.radius} of object {circle2.describe()} results to {circle2.add_radius(40)}")

    logging.info(
        f"We have a circle object {circle2} of type {type(circle2)} with attributes now changed to radius={circle2.radius} and color={circle2.color}")

    logging.info(f"We have the following attributes for object {circle1.describe()}, {dir(circle1)}")

    rectangle1 = Rectangle(5, -55, 30, 60, 'green')
    logging.info(f"We have created a {rectangle1}")

    ShapeDrawer((circle1, circle2, rectangle1)).draw_shapes()
