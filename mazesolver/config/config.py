from collections import namedtuple
import logging
import os

from mazesolver.solver import calc_dfs, calc_bfs
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

MAZE_SOLVERS = ['bfs', 'dfs']
MAZE_SOLVER_DEFAULT = 'bfs'
MazeSolverMapping = namedtuple('maze_solver_mapping', ['name', 'method'])
MAZE_SOLVER_MAPPING = {
    'bfs': MazeSolverMapping('bfs', calc_bfs),
    'dfs': MazeSolverMapping('dfs', calc_dfs),
    }

FILE_INPUT_PATH = os.path.join('files', 'input')
FILE_OUTPUT_PATH = os.path.join('files', 'output')
FILE_TXT_EXT = 'txt'

LOGGER_FORMAT = '%(asctime)s %(levelname)s: %(message)s'
logging.basicConfig(format=LOGGER_FORMAT)
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

LOG_START_APP_MSG = f"Start app {APP_NAME} version: {version.get_version()}"
LOG_END_APP_MSG = f"End app {APP_NAME}"

LOG_INPUT_ERROR_PREFIX_MSG = "User input error. "
