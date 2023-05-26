from typing import Dict

from app.models.point import Point


class Edge:
    def __init__(self, args: Dict, start: Point, end: Point) -> None:
        self.args = args
        self.start = start
        self.end = end
        