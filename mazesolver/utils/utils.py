"""Module utils."""
__author__ = 'Joan A. Pinol  (japinol)'

from math import sqrt
from typing import NamedTuple


class Point(NamedTuple):
    x: int
    y: int


def calc_path_from_location_node(node):
    path = [node.state]
    while node.parent is not None:
        node = node.parent
        path += [node.state]
    return path


def linear_search(iterable, key):
    for item in iterable:
        if item == key:
            return True
    return False


def binary_search(sequence, key):
    low = 0
    high = len(sequence) - 1
    while low <= high:
        mid = (low + high) // 2
        if sequence[mid] < key:
            low = mid + 1
        elif sequence[mid] > key:
            high = mid - 1
        else:
            return True
    return False


def calc_euclidean_distance(goal):
    def distance(location):
        x_delta = location.x - goal.x
        y_delta = location.y - goal.y
        return sqrt((x_delta * x_delta) + (y_delta * y_delta))
    return distance


def calc_manhattan_distance(goal):
    def distance(location):
        x_delta = abs(location.x - goal.x)
        y_delta = abs(location.y - goal.y)
        return x_delta + y_delta
    return distance

