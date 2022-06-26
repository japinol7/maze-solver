from mazesolver.config.config import (
    LOG_INPUT_ERROR_PREFIX_MSG,
    MAZE_ROWS_COLS_MAX,
    MAZE_ROWS_COLS_MIN,
    )


class InputValidator:

    def __init__(self, maze_name, load_maze, rows, columns):
        self.maze_name = maze_name
        self.load_maze = load_maze
        self.rows = rows
        self.columns = columns
        self.input_errors = []

    def validate_input(self):
        self.validate_load_maze()
        self.validate_rows_cols()
        return self.input_errors

    def validate_load_maze(self):
        if not self.load_maze:
            return

        if self.rows or self.columns:
            self.input_errors += [
                    f"{LOG_INPUT_ERROR_PREFIX_MSG}"
                    "When loading a maze, rows and columns parameters cannot be used."]

    def validate_rows_cols(self):
        if self.rows is None or self.columns is None:
            return

        if (self.rows < MAZE_ROWS_COLS_MIN or self.rows > MAZE_ROWS_COLS_MAX
                or self.columns < MAZE_ROWS_COLS_MIN or self.columns > MAZE_ROWS_COLS_MAX):
            self.input_errors += [
                    f"{LOG_INPUT_ERROR_PREFIX_MSG}"
                    f"Rows and columns min size: {MAZE_ROWS_COLS_MIN}. Max size: {MAZE_ROWS_COLS_MAX}"]
