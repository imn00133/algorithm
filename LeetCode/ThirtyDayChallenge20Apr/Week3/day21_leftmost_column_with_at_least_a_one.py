#
# Solved Date:


class BinaryMatrix(object):
    # """
    # This is BinaryMatrix's API interface.
    # You should not implement it, or speculate about its implementation
    # """
    def get(self, x: int, y: int) -> int:
        pass

    def dimensions(self):
        pass


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        row, column = binaryMatrix.dimensions()
        # x = row, y = column
        index = -1
        exit_signal = False
        pointer = [0, column-1]
        while not exit_signal:
            x, y = pointer
            if binaryMatrix.get(x, y):
                index = y
                y -= 1
            else:
                x += 1
            pointer = [x, y]
            if y == 0:
                exit_signal = True
            elif x == row - 1 and not binaryMatrix.get(x, y-1):
                exit_signal = True
        if binaryMatrix.get(*pointer):
            index = pointer[1]
        return index
