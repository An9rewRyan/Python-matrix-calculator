from fractions import Fraction
from types import NoneType
from fractiles import beauti_fraction

def create_matrix(cols: int, rows: int) -> list[list]:
    """Возвращает матрицу заполненную нулями в соответсвии с переданной размерностью (cols, rows)"""
    return [[0 for _ in range(cols)] for _ in range(rows)]

def matrix_to_list(matrix: list[list[int]]) -> list:
    """Вовзращает матрицу в виде списка"""
    return [elem for row in matrix for elem in row]

def deviders_from_str(num: str) -> tuple[int, int] | tuple[None, None]:
    """Возвращает делимое и делитель, если строка является дробью, иначе возвращается пустая последвательность"""
    if "/" in num:
        slash_id = num.index("/")
        print(num[:slash_id], num[slash_id:])
        if all(n.isnumeric() for n in num[:slash_id]) and all(n.isnumeric() for n in num[slash_id+1:]):
            return int(num[:slash_id]), int(num[slash_id+1:])
        return None, None 
    return None, None 

def is_float(num: str) -> bool:
    """Проверяет на то, является ли строка действительным числом с плавающей точкой"""
    try:
        float(num)
        if float(num) == int(num):
            return False
        return  True
    except:
        return False

def validate_number(num: str) -> tuple[bool, type]:
    """Проверяет строку на то, является ли она 'допустимым' числом (float, int, Fraction)
        
        Возвращает последовательность из boolean и типа числа (float, int, Fraction)
    """
    if is_float(num):
        return True, float
    devidend, devider = deviders_from_str(num)
    if devidend != None and devider != None:
        num = beauti_fraction(devidend, devider)
        if type(num) != None:
            if type(num) == Fraction:
                return True, Fraction
    try:
        int(num)
        return True, int
    except:
        return False, NoneType

def get_input_number(row: int, col: int) -> int:
    """Принимает ввод числа на позиции(row, col) и возвращает его, если число проходит проверку"""
    while True:
        num =  input(f'Введите число на позиции: строка - {row+1}; столбец - {col+1}: ')
        num_correct, num_type = validate_number(num)
        if not num_correct:
            print("Число должно быть числом!")
        else:
            return num_type(num)

def fill_matrix(matrix: list[list[int]]) -> list[list[int]]:
    """Вовзращает заполненную матрицу, каждый элемент вводится и проверяется через get_unput_number()"""
    return [[get_input_number(i, j) for j in range(len(matrix[0]))] for i in range(len(matrix))]

def validate_cols_and_rows(cols:str, rows:str) -> tuple[bool, str]:
    """Проверяет на то, являются ли введенные размерности(cols, rows) допустимыми:
    - Не являются float
    - Не вяляются нечисловыми строками
    - Значения больше нуля
    - Размерности представляют собой квадратную матрицу

    Возвращает True/False и сообщение об успехе/ошибке в зависимости от результата
    """
    if is_float(cols) or is_float(rows):
        return False, "Числа должны быть целыми!"
    try:
        int(cols)
        int(rows)
    except ValueError:
        return False, "Числа должны быть числами!"
    if int(cols) <= 0 or int(rows) <= 0:
        return False, "Числа должны быть больше нуля!"
    if int(cols) != int(rows)+1:
        return False, "Метод Крамера нельзя применить на неквадратной матрице!"
    return True, "Размерность введена корректно"

print(is_float("3"))

def get_beauty_matrix(matrix: list[list[int]]) -> list[list[str]]:
    """Принимает матрицу и возвращает список со со строками, которые представляют матрицу и ее визальные границы"""
    mx_len_list = list(map(len, matrix_to_list([[str(matrix[i][j]) for j in range (0, len(matrix[0]))] for i in range(0, len(matrix))])))
    fixed_len = max(mx_len_list) + 2
    beauti_matrix = []
    for row in matrix:
        f_elem= "|"
        for elem in row:
            elem_str = f' {elem} '
            if len(elem_str) < fixed_len:
                elem_str+=" "*(fixed_len-len(elem_str))
            f_elem += elem_str+"|"
        beauti_matrix.append(f_elem+"\n")
        beauti_matrix.append("-"*(len(max(beauti_matrix))-1)+"\n")
    beauti_matrix.insert(0, "-"*(len(max(beauti_matrix))-1)+"\n")
    
    return "".join(beauti_matrix)

def get_cols_and_rows() -> tuple[int, int]:
    """Принимает ввод размерности матрицы, проверяет допустимость значений и вовзращает их"""
    while True:
        cols = str(input("Введите кол-во переменных (включая свободные): "))
        rows = str(input("Введите кол-во уравнений (число): "))
        input_correct, err_msg = validate_cols_and_rows(cols, rows)
        if input_correct:
            return int(cols), int(rows)
        else:
            print(err_msg)

def get_matrix() -> list[list[int]]:
    """Функция объединяет функциональность модуля: 
      - Принимает ввод размерности матрицы
      - Создает матрицу заполненную нулями
      - Принимает пользовательский ввод для всех полей матрицы
      
      Возвращает заполненную пользователем матрицу
    """
    cols, rows = get_cols_and_rows()
    matrix = create_matrix(cols, rows)
    matrix = fill_matrix(matrix)

    return matrix
