from abc import ABC, abstractmethod
from PIL import Image, ImageDraw


class Renderer(ABC):
    @abstractmethod
    def render(self, shape):
        pass


class VectorRenderer(Renderer):
    def render(self, shape):
        print(f"Drawing {shape.__class__.__name__} as vector graphic")

        if isinstance(shape, Square):
            print(f"Vector rendering of square with side {shape.side}")
        elif isinstance(shape, Circle):
            print(f"Vector rendering of circle with radius {shape.radius}")
        elif isinstance(shape, Triangle):
            print(f"Vector rendering of triangle with base {shape.base} and height {shape.height}")


class RasterRenderer(Renderer):
    def render(self, shape):
        print(f"Drawing {shape.__class__.__name__} as raster graphic")
        image = Image.new("RGB", (100, 100), "white")
        draw = ImageDraw.Draw(image)
        if isinstance(shape, Square):
            draw.rectangle([10, 10, 90, 90], fill="blue")
        elif isinstance(shape, Circle):
            draw.ellipse([10, 10, 90, 90], fill="red")
        elif isinstance(shape, Triangle):
            draw.polygon([10, 90, 90, 90, 50, 10], fill="green")
        image.show()


class Shape(ABC):
    def __init__(self, renderer):
        self.renderer = renderer

    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):
    def __init__(self, renderer, radius):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        self.renderer.render(self)


class Square(Shape):
    def __init__(self, renderer, side):
        super().__init__(renderer)
        self.side = side

    def draw(self):
        self.renderer.render(self)


class Triangle(Shape):
    def __init__(self, renderer, base, height):
        super().__init__(renderer)
        self.base = base
        self.height = height

    def draw(self):
        self.renderer.render(self)


def main():
    renderer_choice = input("Choose renderer (raster/vector): ").strip().lower()
    if renderer_choice == "raster":
        renderer = RasterRenderer()
    elif renderer_choice == "vector":
        renderer = VectorRenderer()
    else:
        print("Invalid choice of renderer")
        return

    shape_choice = input("Choose shape (circle/square/triangle): ").strip().lower()
    if shape_choice == "circle":
        radius = float(input("Enter radius of the circle: "))
        shape = Circle(renderer, radius)
    elif shape_choice == "square":
        side = float(input("Enter side length of the square: "))
        shape = Square(renderer, side)
    elif shape_choice == "triangle":
        base = float(input("Enter base length of the triangle: "))
        height = float(input("Enter height of the triangle: "))
        shape = Triangle(renderer, base, height)
    else:
        print("Invalid choice of shape")
        return

    shape.draw()


if __name__ == "__main__":
    main()
