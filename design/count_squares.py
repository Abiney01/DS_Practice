from collections import defaultdict
class CountSquares:
    def __init__(self):
        self.ptsCount = defaultdict(int)
        self.pts = []

    def add(self, point) -> None:
        self.ptsCount[tuple(point)] += 1
        self.pts.append(point)

    def count(self, point):
        res = 0
        px, py = point
        for x, y in self.pts:
            if (abs(py - y) != abs(px - x)) or x == px or y == py:
                continue
            res += self.ptsCount[(x, py)] * self.ptsCount[(px, y)]
        return res
    
squares = CountSquares()
squares.add([1, 1])
squares.add([2, 2])
squares.add([1, 2])
squares.count([2, 1])
squares.count([3, 3])
squares.add([2, 2])
squares.count([2, 1]) 