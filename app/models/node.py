from typing import Dict, List

from models.point import Point


class Node:
    def __init__(self, args: Dict, corners: List[Point]) -> None:
        self.args = args
        self.corners = corners

