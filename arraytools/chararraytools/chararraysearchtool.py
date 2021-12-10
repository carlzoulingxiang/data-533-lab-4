"""
Character Array searching tool

@Author: Nelson Tang
@Date: Nov 25, 2021
"""
from arraytools.chararraytools.chararraytools import CharArrayTools


class CharArraySearchTool(CharArrayTools):
    def __init__(self, arr):
        CharArrayTools.__init__(self, arr)

    def search_min(self):
        return min(self.arr)

    def search_max(self):
        return max(self.arr)

    def search_key(self, target):
        """
        Search a character in the array by implementing a linear search
        :param target: a character
        :return:  The index of the target, if not found return -1.
        """
        for i in range(0, len(self.arr)):
            if self.arr[i] == target:
                return i
        return -1

