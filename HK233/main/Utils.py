from main.AST import Type
from typing import List


class Utils:
    def lookup(self, name, lst, func):
        for x in lst:
            if name == func(x):
                return x
        return None
