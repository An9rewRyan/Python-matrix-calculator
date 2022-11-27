def get_determinant(matrix: list[list[int]]) -> tuple[int, str] | None:
    """Вычисляет детерминант(определитель) у квадаратных матриц. Если матрицы неквадратная, возвращает None.
        
        Иначе, возвращает детерминант и все вычисления, проделанные, чтобы его получить."""
    if len(matrix) != len(matrix[0]):
        return None
    det = 0
    calcs = ""
    #Счетчик проходов по диагонали матрицы: в обычном случае мы проходимся кол-во строк*2)раза
    #В случае с двойкой эта формула не работает, мы проходимся по матрице только два раза
    if len(matrix) == 2:
        max_i = 2
    else:
        max_i = len(matrix) * 2 
    for i in range(max_i):
        diag = 1 #счетчик для результата, полученного на диагонали
        calc_elems = [] 
        #Если мы прошли все "плюсовые диагонали", то в последующие разы мы будем вычитать диаганоли из получившегося результата
        if i > len(matrix) - 1 or \
           (max_i == 2 and i == 1): 
            for j in range(len(matrix)):
                coef = -j -i + len(matrix)
                if coef < -len(matrix):
                    coef += len(matrix) 
                diag *= matrix[j][coef]
                calc_elems.append(matrix[j][coef]) #добавляем переменные в пул вычислений
        #Иначе мы все еще на "плюсовых диагоналях"
        else:   
            for j in range(len(matrix)):
                coef = j + i
                if coef > len(matrix) -1:
                    coef -= len(matrix)
                diag *= matrix[j][coef]
                calc_elems.append(matrix[j][coef]) #добавляем переменные в пул вычислений
        #проходимся по пулу и добавляем в строку вычислений переменные со знаком *
        for k in range(len(calc_elems)):
            if k != 0:
                calcs += f'* {calc_elems[k]} '
            else:
                calcs += f'{calc_elems[k]} '

        if i > len(matrix) - 1 or \
           (max_i == 2 and i == 1): #Если мы дошли до "минусовых диагоналей"
            det -= diag #То далее мы отнимаем текущий результат от общего
            if not(i == (max_i - 1)):
                calcs += "- "
        else:
            det += diag
            if not i == (max_i - 1) or max_i == 2:
                if i > len(matrix) - 2 or (i == 0 and max_i == 2): #В случае если на следующем шаге мы перейдем за половину вычислений, минус нужен уже на этом шаге
                    calcs += "- "
                else:
                    calcs += "+ "
    return det, calcs
        
    


