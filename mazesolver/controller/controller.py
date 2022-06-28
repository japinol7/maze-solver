"""Module controller."""
__author__ = 'Joan A. Pinol  (japinol)'

from mazesolver.config.config import (
    log,
    MAZE_ROWS_DEFAULT,
    MAZE_COLUMNS_DEFAULT,
    SOLVER_FUNCTIONS_WITH_DISTANCE_CALC,
    )
from mazesolver.utils.utils import (
    calc_path_from_location_node,
    calc_manhattan_distance,
    )
from mazesolver.model.maze import Maze
from mazesolver.model.node import Node


class MazeController:

    @staticmethod
    def create_maze(name, rows=MAZE_ROWS_DEFAULT, columns=MAZE_COLUMNS_DEFAULT, load_maze=False, is_image=False):
        """Creates and returns a maze either by loading an existing one or generating a new one randomly."""
        maze = Maze(name)
        if load_maze:
            log.info(f"Load {is_image and 'image' or 'text'} maze: {name}")
            if is_image:
                maze.load_image()
            else:
                maze.load()
            log.info(f"Maze size: {maze.rows} * {maze.columns}")
        else:
            log.info(f"Create Maze: {name}")
            log.info(f"Maze size: {rows} * {columns}")
            maze.create(rows, columns)
            maze.save(save_as_input=True)
        log.info(f"Maze Start location: {maze.start}. Maze Goal location: {maze.goal}")
        return maze

    @staticmethod
    def solve_maze(maze, calc_solver, save_maze=True, is_image=False):
        """Solves a given maze as a side effect.
        It returns the solution node if it finds one. Otherwise, None.
        """
        additional_args = {}
        if calc_solver in SOLVER_FUNCTIONS_WITH_DISTANCE_CALC:
            additional_args = {'calc_distance': calc_manhattan_distance(maze.goal)}

        solution_node = calc_solver(maze.start, maze.check_goal, maze.calc_destination_locations,
                                    **additional_args)
        log.info(f"Maze total nodes explored: {Node.count}")
        if not solution_node:
            log.warning("No solutions found.")
            maze.save_with_no_solution()
            return None
        log.info(f"Solution found: {solution_node}")
        path = calc_path_from_location_node(solution_node)
        log.info(f"Path length: {len(path) - 1}")
        maze.mark_path(path)
        return solution_node, path

    @staticmethod
    def save_maze(maze, path, is_image=False):
        if is_image:
            log.info(f"Save image maze: {maze.file_image_name}")
            maze.save_image(path)
        else:
            log.info(f"Save text maze: {maze.file_name}")
            maze.save()
