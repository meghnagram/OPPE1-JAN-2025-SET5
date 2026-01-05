
def are_orthogonal(t1: tuple, t2: tuple) -> bool:
    '''
    Check if two 2D vectors are orthogonal (perpendicular).

    Args:
        t1 (tuple): The first 2D vector (x, y).
        t2 (tuple): The second 2D vector (x, y).

    Returns:
        bool: True if the vectors are orthogonal, False otherwise.
    '''
    
    return (t1[0] * t2[0] + t1[1] * t2[1]) == 0

# #Another Method
# def are_orthogonal(t1: tuple, t2: tuple) -> bool:
     
#     a,b=t1
#     c,d=t2
    
#     return (a*c)+(b*d)==0

# Check if 2D Vectors are Orthogonal
# Write a function are_orthogonal that takes two tuples t1 and t2 as input. Each tuple represents a 2D vector with two elements (x, y). The function should return True if the vectors are orthogonal (perpendicular), and False otherwise.

# Hint: Two vectors are orthogonal if their dot product is zero. Dot product is the sum of product of the corresponding elements in the vectors.

# Examples

# >>> are_orthogonal((1, 2), (12, -6)) # 1*12 + 2*(-6) = 0, equal to zero
# True 
# >>> are_orthogonal((2, 0), (4, 1)) # 2*4 - 1*0 = 8, not equal to zero
# False
# >>> are_orthogonal((0, 5), (-5, 0)) # 0*(-5) - 5*0 = 0, equal to zero
# True
    
