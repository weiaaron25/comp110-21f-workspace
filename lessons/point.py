from __future__ import annotations


class Point:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def scale_by(self, factor: float) -> None:
        self.x *= factor
        self.y *= factor

    def scale(self, factor: float) -> Point:
        x: float = self.x * factor
        y: float = self.y * factor
        scaled_factor: Point = Point(x, y)
        return scaled_factor


p0: Point = Point(1.0, 2.0)
p0.scale_by(2.0)
print(f"{p0.x}, {p0.y}")

p1: Point = p0.scale(2.0)
print(f"{p1.x}, {p1.y}")