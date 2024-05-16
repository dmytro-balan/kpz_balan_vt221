from abc import ABC, abstractmethod
from PIL import Image, ImageDraw


class Renderer(ABC):
    @abstractmethod
    def render(self, shape):
        pass


class VectorRenderer(Renderer):
    def render(self, shape):
        pass  # Тут реалізується рендеринг векторної графіки, якщо потрібно


class RasterRenderer(Renderer):
    def render(self, shape):
        print(f"Drawing {shape.__class__.__name__} as raster graphic")
        image = Image.new("RGB", (100, 100), "white")
        draw = ImageDraw.Draw(image)
        draw.rectangle([10, 10, 90, 90], fill="blue")  # Приклад рендерингу квадрата як растрового зображення
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
    raster_renderer = RasterRenderer()

    square = Square(raster_renderer, 4)
    square.draw()


if __name__ == "__main__":
    main()
