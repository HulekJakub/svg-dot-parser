from typing import List

from svgelements import Group, Text
from models.edge import Edge
from models.point import Point

from models.node import Node
from parser.const import *

class Parser:
    def __init__(self) -> None:
        pass

    def extract_nodes(self, svg: Group) -> List[Node]:
        nodes = []
        for svg_node in svg.get_element_by_id(NETRON_APP_NODES_ELEMENT_ID):
            label = "NOT_FOUND"
            corners = None
            for element in svg_node:
                if 'attributes' in element.values and 'class' in element.values['attributes']:
                    if NETRON_APP_NODE_INTERIOR_CLASS in element.values['attributes']['class']:
                        for sub_element in element:
                            if isinstance(sub_element, Text):
                                label = sub_element.text
                    elif NETRON_APP_NODE_BORDER_CLASS in element.values['attributes']['class']:
                        xmin, ymin, xmax, ymax = element.bbox() # extract corners from border path
                        corners = [Point(xmin, ymin), Point(xmax, ymin), Point(xmin, ymax), Point(xmax, ymax)]
            nodes.append(Node({'label': label}, corners))
        return nodes
    
    def extract_edges(self, svg: Group) -> List[Edge]:
        # path start and finish
        # print(path.first_point)
        # print(path.current_point)
        pass