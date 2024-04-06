"""Creates and solves mazes of NxN cells with a start and a goal."""

__author__ = 'Joan A. Pinol  (japinol)'

import os
import time

from mazesolver.utils.time_it import time_it
from mazesolver.config.config import (
    LOG_START_APP_MSG,
    LOG_END_APP_MSG,
    MAZE_SOLVER_MAPPING,
    MAZE_SOLVER_DEFAULT,
    FILE_INPUT_PATH,
    FILE_TXT_EXT,
    FILE_IMAGE_EXT,
    )
from mazesolver.config.config import log
from mazesolver.controller.controller import MazeController


def _maze(controller, maze_name, load_maze, rows, columns, print_maze, solver, is_image, save_also_as_text):
    time_start = time.perf_counter()
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
    log.info(f'Total time processing maze: {time.perf_counter() - time_start:.{8}f} s')


def mazes(maze_name, load_maze, rows, columns, print_maze, solver, is_image, save_also_as_text, process_folder):
    log.info(LOG_START_APP_MSG)
    controller = MazeController()

    if process_folder:
        file_names = [(file[:-4], (file.endswith(FILE_IMAGE_EXT) and True or False))
                      for file in os.listdir(FILE_INPUT_PATH)
                      if file.endswith(FILE_TXT_EXT) or file.endswith(FILE_IMAGE_EXT)]
        log.info("Processing all mazes from input directory")
        mazes_total = len(file_names)
        for i, (file_name, is_image_) in enumerate(file_names, start=1):
            log.info('-' * 15)
            log.info(f"Processing maze {i:3} of {mazes_total:3}")
            _maze(controller, file_name, load_maze, rows, columns, print_maze, solver, is_image_, save_also_as_text)
        log.info('-' * 15)
        log.info(LOG_END_APP_MSG)
        return

    _maze(controller, maze_name, load_maze, rows, columns, print_maze, solver, is_image, save_also_as_text)
    log.info(LOG_END_APP_MSG)
