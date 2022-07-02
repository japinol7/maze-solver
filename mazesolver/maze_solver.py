"""Creates and solves mazes of NxN cells with a start and a goal."""

__author__ = 'Joan A. Pinol  (japinol)'

from mazesolver.utils.time_it import time_it
from mazesolver.config.config import (
    LOG_START_APP_MSG,
    LOG_END_APP_MSG,
    MAZE_SOLVER_MAPPING,
    MAZE_SOLVER_DEFAULT,
    )
from mazesolver.config.config import log
from mazesolver.controller.controller import MazeController


def mazes(maze_name, load_maze, rows, columns, print_maze, solver, is_image, save_also_as_text):
    log.info(LOG_START_APP_MSG)
    controller = MazeController()
    maze = time_it(controller.create_maze, name=maze_name, load_maze=load_maze, is_image=is_image,
                   rows=rows, columns=columns)
    print_maze and print(maze)

    solver = solver or MAZE_SOLVER_DEFAULT
    log.info(f"Solver algorithm: {solver}")
    res_node, path = time_it(controller.solve_maze, maze=maze, calc_solver=MAZE_SOLVER_MAPPING[solver].method)

    time_it(controller.save_maze, maze=maze, path=path, is_image=is_image, save_also_as_text=save_also_as_text)
    if res_node and print_maze:
        if not maze.is_path_marked:
            maze.mark_path(path)
        print(maze)
    log.info(LOG_END_APP_MSG)
