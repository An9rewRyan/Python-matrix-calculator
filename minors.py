from determinant import get_determinant
from actions import transpose_matrix
from copy import deepcopy

def get_var_minor_matrix(matrix: list[list[int]], row: int, col: int) -> list[list[int]] | int:
    """Выделяет минор из копии матрицы по координатам(row, col), возвращает матрицу минора либо число, если матрица 2x2"""
    mx = deepcopy(matrix)
    #Обрубить проще, чем пересобрать
    del mx[row]
    mx = transpose_matrix(mx)
    del mx[col]
    if len(mx) == 1 and len(mx[0]) == 1:
        return mx[0][0]
    return mx

def get_minor_matrix(matrix: list[list[int]]) -> list[list[int]]:
    """Вовзвращает матрицу миноров для исходной матрицы"""
    minor_matrix = []
    for i in range (len(matrix)):
        minor_matrix.append([])
        for j in range(len(matrix[i])):
            min_mx = get_var_minor_matrix(matrix, i, j)
            if type(min_mx) == int:
                det = min_mx
            else:
                det, _ = get_determinant(min_mx)
            minor_matrix[i].append(det)
    return minor_matrix









        


        
