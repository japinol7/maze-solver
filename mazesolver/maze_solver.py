"""Creates and solves mazes of NxN cells with a start and a goal."""

__author__ = 'Joan A. Pinol  (japinol)'

from mazesolver.utils.time_it import time_it
from mazesolver.config.config import (
    LOG_START_APP_MSG,
    LOG_END_APP_MSG,
    )
from mazesolver.config.config import log
from mazesolver.solver import calc_dfs
from mazesolver.controller.controller import MazeController


def mazes(maze_name, load_maze, rows, columns, print_maze):
    log.info(LOG_START_APP_MSG)
    controller = MazeController()

    maze = time_it(controller.create_maze, name=maze_name, load_maze=load_maze,
                   rows=rows, columns=columns)
    print_maze and print(maze)

    solution_node = time_it(controller.solve_maze, maze=maze, calc_solver=calc_dfs, save_maze=True)
    if solution_node and print_maze:
        print(maze)
    log.info(LOG_END_APP_MSG)
