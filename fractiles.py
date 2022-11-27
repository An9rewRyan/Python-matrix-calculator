from fractions import Fraction

def beauti_fraction(devidend: int, devider: int) -> int | Fraction | None :
    """Проверяет является ли число 'допустимой' дробью: 
       1) Делитель и делимое являются натуральными числами
       2) Делитель не равен нулю

       Возвращает: 
       1) None, ксли число не является дробью
       2) int, если дробь можно сократить до целого без дробной части
       3) Fraction если является несократимой дробью
    """
    try:
        int(devidend)
        int(devider)
    except:
        return None
    if devider == 0:
        return None
    if Fraction(devidend, devider) == int(Fraction(devidend, devider)):
        return int(Fraction(devidend, devider))
    return Fraction(devidend, devider)


