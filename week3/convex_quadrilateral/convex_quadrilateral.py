'''
Homework
'''
import math

def lines_intersection(k_1: float|int, c_1: float|int, k_2: float|int, c_2: float|int):
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
    if (((4*(f_1**2)*(f_2**2))-(b_1**2+d_1**2-a_1**2-c_1**2)**2)/16) > 0:
        s = math.sqrt(((4*(f_1**2)*(f_2**2))-(b_1**2+d_1**2-a_1**2-c_1**2)**2)/16)
        return float(f'{round(s,2):.2f}')
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
    if (lines_intersection(k_1, c_1, k_2, c_2) is None or
    lines_intersection(k_2, c_2, k_3, c_3) is None or
    lines_intersection(k_3, c_3, k_4, c_4) is None):
        return 0
    x1, y1 = lines_intersection(k_1, c_1, k_2, c_2)
    x2, y2 = lines_intersection(k_2, c_2, k_3, c_3)
    x3, y3 = lines_intersection(k_3, c_3, k_4, c_4)
    x4, y4 = lines_intersection(k_4, c_4, k_1, c_1)
    a = distance(x1, y1, x2, y2)
    b = distance(x2, y2, x3, y3)
    c = distance(x3, y3, x4, y4)
    d = distance(x4, y4, x1, y1)
    f1 = distance(x1, y1, x3, y3)
    f2 = distance(x2, y2, x4, y4)
    return quadrangle_area(a, b, c, d, f1, f2)
