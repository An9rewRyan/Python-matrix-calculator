from determinant import get_determinant
from creator import get_beauty_matrix
from actions import transpose_matrix, swap_rows
from fractiles import beauti_fraction
from copy import deepcopy

def get_var_matrix(matrix: list[list[int]], var_id: int) -> list[list[int]]:
    """ Возвращает матрицу элемента (матрицу со столбцом переменной и результатов, которые поменяли местами)"""
    row_matrix = deepcopy(matrix)
    row_matrix = transpose_matrix(row_matrix)
    row_matrix = swap_rows(row_matrix, var_id, -1)
    return transpose_matrix(row_matrix)

def output_kramer(detM: int, detM_calcs: str, var_res: dict) -> None:
    """Выводит визуальную репрезентацию проделанных рассчетов при использовании метода Крамера"""
    print(f'det Матрицы = {detM_calcs}= {detM}') 
    for i in range(len(var_res)):
        print(f'det x{i+1} =\n{var_res[i]["mx"]} = {var_res[i]["calcs"]} = {var_res[i]["det"]}')
    for j in range(len(var_res)):
        print(f'x{j+1} = {var_res[j]["det"]}/{detM} = {var_res[j]["res"]}')
    return

def kramer(matrix: list[list[int]]) -> list:
    """Расчитывает корни матрицы методом крамера, выводит проделанные рассчеты и вовзращает список ответов"""
    results = []
    free_vars = []
    #Копируем свободные и несвободные переменные матрицы, чтобы избежать изменения оригинала
    free_vars.append(deepcopy(transpose_matrix(matrix)[-1]))
    unfree_vars = deepcopy(transpose_matrix(transpose_matrix(matrix)[:-1]))
    #Вычисляем детерминант основной матрицы
    detM, detM_calcs = get_determinant(unfree_vars)
    if detM == 0:
        return "Определитель равен нулю! Метод крамера не может быть использован!"
    var_results = {}
    for i in range(0, len(matrix)):
        det_var, var_calcs = get_determinant(
            transpose_matrix(get_var_matrix(matrix, i))[:-1]
        )
        res_var = beauti_fraction(det_var, detM)
        #Данные о каждой переменной хранятся во вложенном списке, необходимо для функции вывода
        var_results[i] = {  "det": det_var, 
                            "mx": get_beauty_matrix(get_var_matrix(matrix, i)), 
                            "calcs" : var_calcs,
                            "res": res_var
                        }
        results.append(res_var)
    output_kramer(detM, detM_calcs, var_results)

    return results