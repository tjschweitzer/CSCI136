# THIS IS TERRIBLE STYLE. DON'T DO THIS.
# Inheritance as a mechanism to share fields should only be used in limited circumstances.


class Point2d:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def as_tuple(self):
        return self._x, self._y


class Point3dWrong(Point2d):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self._z = z

    def as_tuple(self):
        x, y = super().as_tuple()
        return x, y, self._z


# Better
class Point3dBetter:
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    # make it explicit when you're transforming from one representation to another
    def as_2d(self):
        return Point2d(self._x, self._y)

    def as_tuple(self):
        return self._x, self._y, self._z


