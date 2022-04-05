class Point:
    def __init__(self, x, y):
        """
        :param x: x coordinate
        :param y: y coordinate
        """
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point({}, {})".format(self.x, self.y)

    def draw(self, ax, *, color="red", s=10) -> None:
        """
        :param ax: matplotlib axes

        To use this function install matplotlib
        """
        
        ax.scatter(self.x, self.y, color=color, s=s)


class Rectangle:
    def __init__(self, x, y, w, h):
        """
        :param x: x coordinate of the bottom left corner
        :param y: y coordinate of the bottom left corner
        :param w: width of the rectangle
        :param h: height of the rectangle

        :                +------------------+
        :                |                  |
        :              height               |
        :                |                  |
        :               (xy)---- width -----+
        """
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def __repr__(self):
        return "Rectangle({}, {}, {}, {})".format(self.x, self.y, self.w, self.h)

    def _draw(self, ax, *, edgecolor="black") -> None:
        "To use this function install matplotlib"
        ax.add_patch(
            patches.Rectangle(
                (self.x, self.y), self.w, self.h, fill=False, edgecolor=edgecolor
            )
        )

    def contains(self, point: Point) -> bool:
        return (
            self.x <= point.x <= self.x + self.w
            and self.y <= point.y <= self.y + self.h
        )

    def intersects(self, rect: "Rectangle") -> bool:
        return not (
            self.x > rect.x + rect.w
            or self.x + self.w < rect.x
            or self.y > rect.y + rect.h
            or self.y + self.h < rect.y
        )


class QuadTree(Rectangle):
    def __init__(self, x, y, w, h, *, div_thresh=4) -> None:
        super().__init__(x, y, w, h)
        self.nw = None
        self.ne = None
        self.sw = None
        self.se = None
        self.points = []
        self.subdivision_threshold = div_thresh

    def insert(self, point: Point) -> None:
        if self.subdivision_threshold > len(self.points):
            self.points.append(point)
        else:
            if not any((self.nw, self.ne, self.sw, self.se)):
                self.subdivide()
            if self.nw.contains(point):
                self.nw.insert(point)
            elif self.ne.contains(point):
                self.ne.insert(point)
            elif self.sw.contains(point):
                self.sw.insert(point)
            elif self.se.contains(point):
                self.se.insert(point)

    def query(self, rect: Rectangle) -> list[Point]:
        points = []
        if self.intersects(rect):
            for point in self.points:
                if rect.contains(point):
                    points.append(point)
        if self.nw:
            points.extend(self.nw.query(rect))
        if self.ne:
            points.extend(self.ne.query(rect))
        if self.sw:
            points.extend(self.sw.query(rect))
        if self.se:
            points.extend(self.se.query(rect))
        return points

    def subdivide(self) -> None:
        self.nw = QuadTree(
            self.x,
            self.y,
            self.w / 2,
            self.h / 2,
            div_thresh=self.subdivision_threshold,
        )
        self.ne = QuadTree(
            self.x + self.w / 2,
            self.y,
            self.w / 2,
            self.h / 2,
            div_thresh=self.subdivision_threshold,
        )
        self.sw = QuadTree(
            self.x,
            self.y + self.h / 2,
            self.w / 2,
            self.h / 2,
            div_thresh=self.subdivision_threshold,
        )
        self.se = QuadTree(
            self.x + self.w / 2,
            self.y + self.h / 2,
            self.w / 2,
            self.h / 2,
            div_thresh=self.subdivision_threshold,
        )

    def draw(self, ax, *, edgecolor="black") -> None:
        self._draw(ax, edgecolor=edgecolor)
        if self.nw:
            self.nw.draw(ax, edgecolor=edgecolor)
        if self.ne:
            self.ne.draw(ax, edgecolor=edgecolor)
        if self.sw:
            self.sw.draw(ax, edgecolor=edgecolor)
        if self.se:
            self.se.draw(ax, edgecolor=edgecolor)


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from matplotlib import patches 

    from random import random

    fig, ax = plt.subplots()
    SIZE = 5
    ax.set_xlim(0, SIZE)
    ax.set_ylim(0, SIZE)
    ax.set_aspect("equal")

    points = [Point(random() * SIZE, random() * SIZE) for _ in range(550)]
    qt = QuadTree(0, 0, SIZE, SIZE, div_thresh=3)
    for p in points:
        qt.insert(p)
        p.draw(ax, color="blue", s=7)

    query_rect = Rectangle(random() * SIZE, random() * SIZE, 2, 2)
    # query_rect = Rectangle(1,1, 1, 1)
    query_rect._draw(ax, edgecolor="red")
    res_points = sorted(qt.query(query_rect), key=lambda p: p.x)

    print(f"found {len(res_points)} points inside the query rectangle: {query_rect}")
    for point in res_points:
        print(point)
        point.draw(ax, color="red", s=15)

    qt.draw(ax)
    plt.show()

    print("done!")
