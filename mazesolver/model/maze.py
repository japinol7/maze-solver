"""Module maze."""
__author__ = 'Joan A. Pinol  (japinol)'

import os
import random

from PIL import Image

from mazesolver.config.config import (
    MAZE_ROWS_DEFAULT,
    MAZE_COLUMNS_DEFAULT,
    MAZE_SPARSENESS_ROWS_COLS_BASE,
    MAZE_SPARSENESS_DEFAULT,
    CELL_SEPARATOR,
    CELL_IMAGE_MAPPING,
    FILE_INPUT_PATH,
    FILE_OUTPUT_PATH,
    FILE_TXT_EXT,
    FILE_IMAGE_EXT,
    )
from mazesolver.model.cell import Cell
from mazesolver.utils.utils import Point


class Maze:
    def __init__(self, name):
        self.name = name
        self.rows = None
        self.columns = None
        self.start = None
        self.goal = None
        self.sparseness = None
        self.grid = None
        self.file_name = f'{self.name}.{FILE_TXT_EXT}'
        self.file_image_name = f'{self.name}.{FILE_IMAGE_EXT}'
        self.image = None

    def create(self, rows=MAZE_ROWS_DEFAULT, columns=MAZE_COLUMNS_DEFAULT,
               start=None, goal=None, sparseness=MAZE_SPARSENESS_DEFAULT, ):
        self.rows = rows
        self.columns = columns
        self.start = Point(start[0], start[1]) if start else Point(random.randint(0, self.columns - 1), 0)
        self.goal = Point(goal[0], goal[1]) if goal else Point(random.randint(0, self.columns - 1), self.rows - 1)
        if MAZE_SPARSENESS_ROWS_COLS_BASE < rows * columns:
            ratio = MAZE_SPARSENESS_ROWS_COLS_BASE / (rows * columns)
        else:
            ratio = 1
        self.sparseness = sparseness * ratio
        self.grid = None

        self._create()

    def _create(self):
        self._clean_grid()
        for i in range(self.rows):
            self._random_fill()
            self.grid[self.start.y][self.start.x] = Cell.START.value
            self.grid[self.goal.y][self.goal.x] = Cell.GOAL.value

    def _clean_grid(self):
        self.grid = [[Cell.EMPTY.value for _ in range(self.columns)]
                     for r in range(self.rows)]

    def _random_fill(self):
        for i in range(self.rows):
            for j in range(self.columns):
                if random.uniform(0, 1.0) < self.sparseness:
                    self.grid[i][j] = Cell.WALL.value

    def load(self):
        file_path_name = os.path.join(FILE_INPUT_PATH, self.file_name)
        with open(file_path_name, 'r', encoding='utf8') as fin:
            rows = fin.readlines()

        self.grid = []
        for row in rows:
            self.grid.append(row.strip().split(CELL_SEPARATOR))

        self.rows = len(self.grid)
        self.columns = len(self.grid[0])
        self.start = Point(self.grid[0].index(Cell.START.value), 0)
        self.goal = Point(self.grid[-1].index(Cell.GOAL.value), len(self.grid) - 1)

    def load_image(self):
        file_path_name = os.path.join(FILE_INPUT_PATH, self.file_image_name)
        self.image = Image.open(file_path_name)
        self.columns, self.rows = self.image.size
        data = list(self.image.getdata(0))

        self.grid = []
        for y in range(self.rows):
            row_offset = y * self.columns
            self.grid.append([CELL_IMAGE_MAPPING[data[row_offset + x]] for x in range(self.columns)])

        self.start = Point(self.grid[0].index(Cell.EMPTY.value), 0)
        self.goal = Point(self.grid[-1].index(Cell.EMPTY.value), len(self.grid) - 1)

    def save(self, save_as_input=False):
        file_path = FILE_INPUT_PATH if save_as_input else FILE_OUTPUT_PATH
        file_path_name = os.path.join(file_path, self.file_name)
        with open(file_path_name, 'w', encoding='utf8') as fout:
            fout.write(str(self))

    def save_image(self, path=None):
        file_path = FILE_OUTPUT_PATH
        file_path_name = os.path.join(file_path, self.file_image_name)
        if path:
            self.image = self.image.convert('RGB')
            im_pixels = self.image.load()
            path_len = len(path)
            for i, location in enumerate(path):
                blue_green = int(i / path_len * 255)
                rgb_color = (0, blue_green, 255 - blue_green)
                im_pixels[location.x, location.y] = rgb_color
        self.image.save(file_path_name, format='PNG')

    def save_with_no_solution(self, save_as_input=False):
        file_path = FILE_INPUT_PATH if save_as_input else FILE_OUTPUT_PATH
        file_path_name = os.path.join(file_path, self.file_name)
        with open(file_path_name, 'w', encoding='utf8') as fout:
            fout.write("No solutions found. Original maze:\n")
            fout.write(str(self))

    def calc_destination_locations(self, location):
        """Calculate viable neighbour destination locations."""
        point = location
        locations = []
        if point.y + 1 < self.rows and self.grid[point.y + 1][point.x] != Cell.WALL.value:
            locations += [Point(point.x, point.y + 1)]
        if point.y - 1 >= 0 and self.grid[point.y - 1][point.x] != Cell.WALL.value:
            locations += [Point(point.x, point.y - 1)]
        if point.x + 1 < self.columns and self.grid[point.y][point.x + 1] != Cell.WALL.value:
            locations += [Point(point.x + 1, point.y)]
        if point.x - 1 >= 0 and self.grid[point.y][point.x - 1] != Cell.WALL.value:
            locations += [Point(point.x - 1, point.y)]
        return locations

    def check_goal(self, location):
        return location == self.goal

    def mark_path(self, path):
        for location in path:
            self.grid[location.y][location.x] = Cell.PATH.value
        self.grid[self.start.y][self.start.x] = Cell.START.value
        self.grid[self.goal.y][self.goal.x] = Cell.GOAL.value

    def clean_path(self, path):
        for location in path:
            self.grid[location.y][location.x] = Cell.EMPTY.value
        self.grid[self.start.y][self.start.x] = Cell.START.value
        self.grid[self.goal.y][self.goal.x] = Cell.GOAL.value

    def __str__(self):
        res = ''
        for row in self.grid:
            res += CELL_SEPARATOR.join([cell for cell in row]) + '\n'
        return res

    def __repr__(self):
        return self.__str__()
