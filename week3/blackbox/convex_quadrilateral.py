'''
Homework
'''
def lines_intersection(k_1: float|int, c_1: float|int, k_2: float|int, c_2: float|int)\
    -> (float|int, float|int):
    '''
    float|int, float|int, float|int, float|int -> float|int, float|int
    This function takes four numbers (each of the numbers
    is an integer or a floating point) and returns a tuple of
    two floating point numbers - the values of the coordinates (x,y)
    the intersection points of two lines (numbers are rounded to 2
    decimal places). If the lines are parallel or coincide, the function
    should return None.
    
    >>> lines_intersection('l', 'j', 'j', 'k')

    '''
    if isinstance(k_1, float|int) and isinstance(c_1, float|int) \
        and isinstance(k_2, float|int) and isinstance(c_2, float|int):
        if k_1 != k_2:
            x_k1 = (c_2 - c_1) / (k_1 - k_2)
            y_k1 = k_1 * x_k1 + c_1
            x_k2 = round(x_k1, 2)
            y_k2 = round(y_k1, 2)
            return (x_k2, y_k2)
    return None


def distance(x_1: float|int, y_1: float|int, x_2: float|int, y_2: float|int)\
    -> float|int:
    '''
    float|int, float|int, float|int, float|int -> float|int
    This function takes four numbers (each an integer or a
    floating point) that are the coordinates of two points.
    The function returns the distance between these points.
    
    >>> distance('l', 'j', 'j', 'k')
    
    '''
    if isinstance(x_1, float|int) and isinstance(y_1, float|int)\
        and isinstance(x_2, float|int)\
        and isinstance(y_2, float|int):
        dis_1 = ((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2) ** 0.5
        dis_2 = round(dis_1, 2)
        return dis_2
    return None

def quadrangle_area(a_1: float|int, b_1: float|int, c_1: float|int,
                    d_1: float|int, f_1: float|int, f_2: float|int)\
                        -> float|int:
    '''
    float|int,float|int,float|int, float|int, float|int, float|int -> float|int
    This function takes six numbers(each integer or floating point) representing
    the lengths of the sides and diagonals of a quadrilateral and returns
    the area of the quadrilateral (rounded to 2 decimal places).
    
    >>> quadrangle_area('l', 'j', 'j', 'k', 'j', 'k')
    
    '''
    if isinstance(a_1, float|int) and isinstance(b_1, float|int)\
        and isinstance(c_1, float|int)\
        and isinstance(d_1, float|int) and isinstance(f_1, float|int)\
        and isinstance(f_2, float|int):
        s_11 = 4 * (f_1 ** 2) * (f_2 **2)
        s_12 = (b_1 ** 2 + d_1 ** 2 - a_1 ** 2 - c_1 **2)**2
        s_1 = ((s_11 - s_12)**0.5)/4
        if s_12 != 0 and s_11 > s_12:
            s_2 = round(s_1, 2)
            return s_2
    return None
def four_lines_area(k_1: float|int, c_1: float|int, k_2: float|int,
                    c_2: float|int, k_3: float|int, c_3: float|int,
                    k_4: float|int, c_4: float|int) -> float|int:
    '''
    float|int, float|int, float|int, float|int, float|int, float|int, float|int,
    float|int -> float|int
    Find the area of a convex quadrilateral, If such a quadrilateral does
    not exist(three parallel lines), the function must return0 Each of the sides
    of the quadrilateral is given by the equation of the line to
    which this side belongs. 
    
    >>> four_lines_area('l', 'j', 'j', 'k', 'j', 'k', 'j', 's')
    
    '''
    if isinstance(k_1, float|int) and isinstance(c_1, float|int)\
        and isinstance(k_2, float|int) and isinstance(c_2, float|int)\
        and isinstance(k_3, float|int) and isinstance(c_3, float|int)\
        and isinstance(k_4, float|int) and isinstance(c_4, float|int):
        if ((k_1 != k_2 != k_3) and
            (k_1 != k_2 != k_4) and
            (k_2 != k_3 != k_4) and
            (k_1 != k_3 != k_4)):
            x_1, y_1 = lines_intersection(k_1, c_1, k_2, c_2)
            x_2, y_2 = lines_intersection(k_2, c_2, k_3, c_3)
            x_3, y_3 = lines_intersection(k_3, c_3, k_4, c_4)
            x_4, y_4 = lines_intersection(k_4, c_4, k_1, c_1)

            a_1 = distance(x_1, y_1, x_2, y_2)
            b_1 = distance(x_2, y_2, x_3, y_3)
            c_1 = distance(x_3, y_3, x_4, y_4)
            d_1 = distance(x_4, y_4, x_1, y_1)
            f_1 = distance(x_1, y_1, x_3, y_3)
            f_2 = distance(x_2, y_2, x_4, y_4)

            s_out = quadrangle_area(a_1, b_1, c_1, d_1, f_1, f_2)
            return s_out
        return 0
    return None
if __name__ == '__main__':
    import doctest
    doctest.testmod()
