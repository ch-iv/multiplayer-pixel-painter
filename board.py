from typing import Tuple, List
import os
import pickle


class Board:
    """
    The Board class represents the arrangement of pixels and their colors.
    It also provides functions for modifying pixels on the board.
    """

    def __init__(
        self,
        width: int,
        height: int,
        fill_color: Tuple[int, int, int],
        load=True,
        filename="board.pickle",
    ) -> None:
        if load and filename in os.listdir():
            # load board pixels from a binary file if the file is present
            with open(filename, "rb") as f:
                self.pixels = pickle.load(f)
        else:
            self.pixels: List[List[Tuple[int, int, int]]] = [
                [fill_color for _ in range(width)] for _ in range(height)
            ]

    def set(self, x: int, y: int, color: Tuple[int, int, int]) -> None:
        """Set the color of a specific pixel based on its coordinates."""
        self.pixels[y][x] = color

    def dump(self, filename="board.pickle"):
        """Dumps the board's pixels into a binary file"""
        with open(filename, "wb") as f:
            pickle.dump(self.pixels, f)

    def __getitem__(self, val: int):
        return self.pixels[val]

    def __repr__(self):
        return str(self.pixels)

    def __str__(self) -> str:
        return str(self.pixels)
