from determinant import get_determinant
from copy import deepcopy
from actions import transpose_matrix, devide_matrix, multiply_matrix
from minors import get_minor_matrix
from creator import get_beauty_matrix
from fractions import Fraction

def get_alg_add_matrix(matrix: list[list[int]]) -> list[list[int]]:
    """Возвращает матрицу алгебраических дополнений"""
    alg_add_matrix = []
    for i in range(len(matrix)):
        alg_add_matrix.append([])
        for j in range(len(matrix)):
            if (i + j + 2) % 2 == 0:
                alg_add_matrix[i].append(matrix[i][j])
            else:
                alg_add_matrix[i].append(matrix[i][j]*(-1))
    return alg_add_matrix

def output_rev_matrix(calcs: str, det: int,
                      *mxs: list[list[int|float|Fraction]] #Принимает 7 матриц, выделение каждой матрицы отдельным аргументом убрано в целях удобочитаемости
                      ) -> None:
    """Принимает вычислительный путь определителя матрицы, сам определеитель и семь матриц в строгом порядке: 
    1) Исходная матрица
    2) Матрица миноров
    3) Матрица алегбраических дополнений
    4) Транспонированная матрица алгебраических дополнений
    5) Свободные переменные
    6) Матрица результатов

    Выводит все матрицы в консоли, возвращает None
    """
    mxs_c = []
    for matrix in mxs:
        mxs_c.append(get_beauty_matrix(matrix))
    print(
    f'Матрица:\n{mxs_c[0]}\nМатрица миноров:\n{mxs_c[1]}\nМатрица алгебраических доплнений:\n{mxs_c[2]}',
    f'\nТранспонированная матрица алгебраических дополнений:\n{mxs_c[3]}\nДетерминант матрицы:\n{calcs} = {det}',
    f'\n\nРезультат: \n{mxs_c[3]}*\n{mxs_c[4]} /\n {det} \n=\n{mxs_c[5]}'
    )
    
    return 

def reverse_matrix(matrix: list[list[int]]):
    """Функция собирает все значения из функций модуля и возвращает корни системы методом обратной матрицы"""
    free_vars = [deepcopy(transpose_matrix(matrix)[-1])]
    unfree_vars = deepcopy(transpose_matrix(transpose_matrix(matrix)[:-1]))
    minor_matrix = get_minor_matrix(unfree_vars)
    alg_add_matrix = get_alg_add_matrix(minor_matrix)
    transposed_matrix = transpose_matrix(alg_add_matrix)

    det, calcs = get_determinant(unfree_vars)
    res_matrix = devide_matrix(multiply_matrix(transposed_matrix, free_vars), det)
    output_rev_matrix(calcs, det, matrix, minor_matrix, alg_add_matrix, transposed_matrix, free_vars, res_matrix)
    return res_matrix

reverse_matrix([[1, 2, 3, 4],[6, 7, 9, 1],[5, 2, 3, 8]])