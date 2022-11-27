from fractiles import beauti_fraction
from copy import deepcopy

def devide_matrix(matrix: list[list[int]], devider: int) -> list[list[int]] | None:
    """Делит матрицу на число и возвращает матрицу результатов, если делитель не равен нулю"""
    if devider == 0:
        return None
    return [[beauti_fraction(matrix[i][j], devider) for j in range(len(matrix[0]))] for i in range(len(matrix))]

def add_matrix(matrix_a: list[list[int]], matrix_b: list[list[int]]) -> list[list[int]] | None:
    """Складывает матрицы и возвращает матрицу результатов, если матрицы равны по размерности"""
    if len(matrix_a) == len(matrix_b) and \
       len(matrix_a[0]) == len(matrix_b[0]):
        return [[matrix_a[i][j]+matrix_b[i][j] for j in range(len(matrix_a[0]))] for i in range(len(matrix_a))]
    return None

def multiply_matrix(matrix: list[list[int]], mult: int | list[list[int]]) -> list[list[int]] | None: 
    """Умножает матрицу на число либо другую матрицу (если кол-во строк матрицы 1 = кол-ву столбцов матрицы2)
    
        Возвращает матрицу результатов."""
    mult_matrix = []
    if type(mult) == int:
        return [[elem*mult for elem in matrix] for _ in matrix]
    else:
        mult_copy = deepcopy(mult)
        if len(matrix[0]) != len(transpose_matrix(mult)):
            return None
        """Создает копию матрицы множителя, чтобы избежать изменений при преобразовании"""
        mult_copy = transpose_matrix(mult_copy)
        for i in range(len(matrix)):
            mult_matrix.append([])
            for k in range(len(mult_copy[0])):
                res = 0
                for j in range(len(matrix)):
                    res += (matrix[i][j] * mult_copy[j][k])
                mult_matrix[i].append(res)
    return mult_matrix

def transpose_matrix(row_matrix: list[list[int]]) -> list[list[int]]:
    """Возвращает транспонированную матрицу (делает строки столбаци и наооборот)"""
    return [[row_matrix[j][i] for j in range(len(row_matrix))] for i in range(len(row_matrix[0]))]

def swap_rows(matrix: list[list[int]], curr_id: int, next_id: int) -> list[list[int]]:
    """Меняет местами две строки/столбца матрицы и возвращает измененную копию"""
    mx_copy = deepcopy(matrix)
    mx_copy[curr_id], mx_copy[next_id] = mx_copy[next_id], mx_copy[curr_id]
    return mx_copy
    