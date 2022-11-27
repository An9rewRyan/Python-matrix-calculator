from actions import *
from copy import deepcopy

def ladder(matrix: list[list[int]]):
    """Приводит систему к ступенчатому виду и возвращает ее измененную копию"""
    free_vars = [deepcopy(transpose_matrix(matrix)[-1])]
    unfree_vars = deepcopy(transpose_matrix(transpose_matrix(matrix)[:-1]))
    return