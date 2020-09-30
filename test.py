import unittest


# class Rectangle:
#     @property
#     def width(self):
#         return self.__width
#
#     def set_width(self, width):
#         self.__width = width
#
#     @property
#     def height(self):
#         return self.__height
#
#     def set_height(self, height):
#         self.__height = height
#
#     @property
#     def area(self):
#         return self.__width * self.__height
#
#
# class Square(Rectangle):
#     def set_width(self, width):
#         super().set_width(width)
#
#     def set_height(self, height):
#         super().set_height(height)


class RectangleImmutable:
    __slots__ = ('_width', '_height')

    def __init__(self, width, height):
        super().__setattr__('_width', width)
        super().__setattr__('_height', height)

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def __setattr__(self, key, value):
        raise AttributeError('attributes are immutable')

    @property
    def area(self):
        return self._width * self._height


class SquareImmutable(RectangleImmutable):
    def __init__(self, size):
        super().__init__(size, size)


# rectangle = SquareImmutable(4)
# print(rectangle.area)


class SquareTest(unittest.TestCase):
    def test_area(self):
        rectangle = SquareImmutable(4)

        self.assertEqual(rectangle.area, 16)

        with self.assertRaises(AttributeError):
            rectangle.width = 5

        with self.assertRaises(AttributeError):
            rectangle.width = 4
