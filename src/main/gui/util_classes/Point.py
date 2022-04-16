class Point:
    """2d point on screen to make click operations manageable."""

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def set_x(self, x: float):
        self.x = x

    def set_y(self, y: float):
        self.y = y

    def precedes(self, other):
        """
        Checks whether both dimensions of point are smaller or equal to the other point.

        :param other: Point
        :return: bool
        """
        return self.x <= other.x and self.y <= other.y

    def follows(self, other):
        """
        Checks whether both dimensions of point are greater or equal to the other point.

        :param other: Point
        :return: bool
        """
        return self.x >= other.x and self.y >= other.y

    def upper_right(self, other):
        """
        Returns top right corner of rectangle made by two points.

        :param other: Point
        :return: Point
        """
        return Point(max(self.x, other.x), max(self.y, other.y))

    def lower_left(self, other):
        """
        Returns bottom left corner of rectangle made by two points.

        :param other: Point
        :return: Point
        """
        return Point(min(self.x, other.x), min(self.y, other.y))

    def add(self, other):
        """
        Adds other point to point.

        :param other: Point
        :return: Point
        """
        return Point(self.x + other.x, self.y + other.y)

    def subtract(self, other):
        """
        Subtracts other point from point.

        :param other: Point
        :return: Point
        """
        return Point(self.x - other.x, self.y - other.y)

    def opposite(self):
        """
        Returns **new Point** as an opposite of a point.

        :return: Point
        """
        return Point(-self.x, -self.y)
