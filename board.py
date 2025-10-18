class Board:
    """
    Defines a board with
    Parameters: num_cells cells and num_mines mines.
    """
    def __init__(self, num_rows, num_cols, num_mines):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.num_mines = num_mines
        self.grid = [[None for _ in range(num_cols)] for _ in range(num_rows)] # Initialize grid with empty cells


    def get_cells(self):
        """Returns the total number of cells on the board."""
        return self.num_rows * num_cols

    def get_mines(self):
        """Returns the number of mines on the board."""
        return self.num_mines

    def get_cell(self, row, col):
        """Returns the cell at the specified coordinates."""
        return self.grid[row][col]

    def set_cell(self, row, col, val):
        """Sets the value of the cell at the specified coordinates."""
        self.grid[row][col] = val

    