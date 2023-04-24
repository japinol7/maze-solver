"""Module a_star."""
__author__ = 'Joan A. Pinol  (japinol)'

from mazesolver.container import PriorityQueue
from mazesolver.model.node import Node


def calc_a_star(start_location, check_goal, calc_destination_locations, calc_distance):
    """Implements astar search algorithm for traversing a graph or tree data structure."""
    next_node = PriorityQueue()
    next_node.push(Node(start_location, None, 0, calc_distance(start_location)))
    explored = {start_location: 0}

    while not next_node.is_empty:
        current_node = next_node.pop()
        current_state = current_node.state
        if check_goal(current_state):
            return current_node
        for location in calc_destination_locations(current_state):
            # all node heuristic costs are 1 since we do not have cost information for each step in our input mazes
            new_cost = current_node.cost + 1
            if location not in explored or explored[location] > new_cost:
                explored[location] = new_cost
                next_node.push(Node(location, current_node, new_cost, calc_distance(location)))
    return None
