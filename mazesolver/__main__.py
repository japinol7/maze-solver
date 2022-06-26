"""Module __main__. Entry point."""
__author__ = 'Joan A. Pinol  (japinol)'

from argparse import ArgumentParser
import traceback

from mazesolver.config.config import (
    MAZE_ROWS_COLS_MAX,
    MAZE_ROWS_COLS_MIN,
    MAZE_ROWS_DEFAULT,
    MAZE_COLUMNS_DEFAULT,
    MAZE_SOLVERS,
    MAZE_NAME_DEFAULT,
    )
from mazesolver.config.config import log
from mazesolver.validator.validator import InputValidator
from mazesolver.maze_solver import mazes


def main():
    # Parse optional arguments from the command line
    parser = ArgumentParser(description="Maze solver.",
                            prog='mazesolver')
    parser.add_argument('-c', '--create', default=False, action='store_true',
                        help="create a new maze instead of loading one.")
    parser.add_argument('-p', '--print', default=False, action='store_true',
                        help="print the maze created or load and the maze solution to the console.")
    parser.add_argument('-n', '--name', default=None,
                        help="the maze's name.")
    parser.add_argument('-nr', '--rows', default=None,
                        help=f"the number of rows. Must be between {MAZE_ROWS_COLS_MIN} and {MAZE_ROWS_COLS_MAX}.")
    parser.add_argument('-nc', '--columns', default=None,
                        help=f"the number of columns. Must be between {MAZE_ROWS_COLS_MIN} and {MAZE_ROWS_COLS_MAX}.")
    parser.add_argument('-s', '--solver', default=None,
                        help=f"solver algorithm. Available solvers: {', '.join(MAZE_SOLVERS)}")
    parser.add_argument('-t', '--debugtraces', default=False, action='store_true',
                        help="show debug back traces information when something goes wrong.")

    args = parser.parse_args()
    try:
        maze_name = args.name or MAZE_NAME_DEFAULT
        load_maze = not args.create
        print_maze = args.print
        rows = args.rows and int(args.rows) or None
        columns = args.columns and int(args.columns) or None
        if not load_maze:
            rows = rows or MAZE_ROWS_DEFAULT
            columns = columns or MAZE_COLUMNS_DEFAULT
        solver = args.solver

        input_validator = InputValidator(maze_name, load_maze, rows, columns, solver)
        validate_input_errors = input_validator.validate_input()
        if validate_input_errors:
            for input_error in validate_input_errors:
                log.error(input_error)
            return

        mazes(maze_name, load_maze, rows, columns, print_maze, solver)
    except Exception as e:
        if args.debugtraces:
            traceback.print_tb(e.__traceback__)
        log.critical(f'Error: {e}')


if __name__ == "__main__":
    main()
