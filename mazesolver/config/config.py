from collections import namedtuple
import logging
import os

from mazesolver.model.cell import Cell
from mazesolver.solver import calc_a_star, calc_bfs, calc_dfs
from mazesolver.version import version

APP_NAME = 'mazesolver'

MAZE_ROWS_COLS_MAX = 2000
MAZE_ROWS_COLS_MIN = 4

MAZE_ROWS_DEFAULT = 32
MAZE_COLUMNS_DEFAULT = 12
MAZE_SPARSENESS_ROWS_COLS_BASE = 12 * 12
MAZE_SPARSENESS_DEFAULT = 0.03
CELL_SEPARATOR = '  '

MAZE_NAME_DEFAULT = 'maze_01'
MAZE_IMAGE_NAME_DEFAULT = 'maze_braid_51'

MAZE_SOLVERS = ['astar', 'bfs', 'dfs']
MAZE_SOLVER_DEFAULT = 'bfs'

MazeSolverMapping = namedtuple('maze_solver_mapping', ['name', 'method'])
MAZE_SOLVER_MAPPING = {
    'astar': MazeSolverMapping('astar', calc_a_star),
    'bfs': MazeSolverMapping('bfs', calc_bfs),
    'dfs': MazeSolverMapping('dfs', calc_dfs),
    }

SOLVER_FUNCTIONS_WITH_DISTANCE_CALC = [calc_a_star]

CELL_IMAGE_MAPPING = {
    1: Cell.EMPTY.value,
    0: Cell.WALL.value,
    }

FILE_INPUT_PATH = os.path.join('files', 'input')
FILE_OUTPUT_PATH = os.path.join('files', 'output')
FILE_TXT_EXT = 'txt'
FILE_IMAGE_EXT = 'png'

LOGGER_FORMAT = '%(asctime)s %(levelname)s: %(message)s'
logging.basicConfig(format=LOGGER_FORMAT)
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

LOG_START_APP_MSG = f"Start app {APP_NAME} version: {version.get_version()}"
LOG_END_APP_MSG = f"End app {APP_NAME}"

LOG_INPUT_ERROR_PREFIX_MSG = "User input error. "
