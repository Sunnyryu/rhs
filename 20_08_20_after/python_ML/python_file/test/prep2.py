def vector_size_check(*vector_variables):
    return all(len(vector_variables[0]) == x for x in [len(vector) for vector in vector_variables[1:]])

print(vector_size_check([1,2,3], [4,5,6], [7,8,9]))

def vector_addition(*vector_variables):
    if vector_size_check(*vector_variables) == False:
        raise ArithmeticError
    return [sum(elements) for elements in zip(*vector_variables)]

print(vector_size_check([1,2,3], [2,3,4], [5,6,7])) # Expected value: True
print(vector_size_check([1, 3], [2,4], [6,7])) # Expected value: True
print(vector_size_check([1, 3, 4], [4], [6,7])) # Expected value: False

def vector_subtraction(*vector_variables):
    if vector_size_check(*vector_variables) == False:
        raise ArithmeticError
    z = 0
    v = 0
    a = []
    for i in zip(*vector_variables):
        if len(i) == 2:
            k = i[0] - i[1]
            a.append(k)
        elif len(i) >= 3:
            for m in i:
                if z == 0:
                    v = m
                    z += 1
                elif z > 0:
                    v = v-m
                    z += 1
                    if len(i) == z:
                        z = 0
            a.append(v)
    return a

print(vector_subtraction([1, 3], [2, 4])) # Expected value: [-1, -1]
print(vector_subtraction([1, 5], [10, 4], [4, 7])) # Expected value: [-13, -6]


def scalar_vector_product(alpha, vector_variable):
    a = []
    for element in vector_variable:
        a.append(alpha* element)
    return a 
print (scalar_vector_product(5,[1,2,3])) # Expected value: [5, 10, 15]
print (scalar_vector_product(3,[2,2])) # Expected value: [6, 6]
print (scalar_vector_product(4,[1])) # Expected value: [4]
from itertools import zip_longest
def matrix_size_check(*matrix_variables):
    for i in zip_longest(*matrix_variables):
        for v in range(len(i)):
            if i[v] == None:
                return False
    return True

matrix_x = [[2, 2], [2, 2], [2, 2]]
matrix_y = [[2, 5], [2, 1]]
matrix_z = [[2, 4], [5, 3]]
matrix_w = [[2, 5], [1, 1], [2, 2]]
print (matrix_size_check(matrix_x, matrix_y, matrix_z)) # Expected value: False
print (matrix_size_check(matrix_y, matrix_z)) # Expected value: True
print (matrix_size_check(matrix_x, matrix_w)) # Expected value: True

def is_matrix_equal(*matrix_variables):
    return all([ all([len(set(row)) == 1 for row in zip(*matrix)]) for matrix in zip(*matrix_variables)])
matrix_x = [[2, 2], [2, 2]]
matrix_y = [[2, 5], [2, 1]]
print (is_matrix_equal(matrix_x, matrix_y, matrix_y, matrix_y)) # Expected value: False
print (is_matrix_equal(matrix_x, matrix_x)) # Expected value: True

def matrix_addition(*matrix_variables):
    if matrix_size_check(*matrix_variables) == False:
        raise ArithmeticError
    a = []
    b = []
    for matrix in zip(*matrix_variables):
        k = matrix
        #print(k)
        for row in zip(*matrix):
            t = sum(row)
            a.append(t)
            #print(a)
        b.append(a)
        a = []
    return b

matrix_x = [[2, 2], [2, 2]]
matrix_y = [[2, 5], [2, 1]]
matrix_z = [[2, 4], [5, 3]]

print (matrix_addition(matrix_x, matrix_y)) # Expected value: [[4, 7], [4, 3]]
print (matrix_addition(matrix_x, matrix_y, matrix_z)) # Expected value: [[6, 11], [9, 6]]

def matrix_subtraction(*matrix_variables):
    if matrix_size_check(*matrix_variables) == False:
        raise ArithmeticError
    a = []
    b = []
    for matrix in zip(*matrix_variables):
        for row in zip(*matrix):
            if len(row) == 2:
                c = row[0] - row[1]
                a.append(c)
            elif len(row) == 3:
                c = row[0] - row[1] - row[2]
                a.append(c)
        b.append(a)
        a = []
    return b
# 실행결과
matrix_x = [[2, 2], [2, 2]]
matrix_y = [[2, 5], [2, 1]]
matrix_z = [[2, 4], [5, 3]]

print (matrix_subtraction(matrix_x, matrix_y)) # Expected value: [[0, -3], [0, 1]]
print (matrix_subtraction(matrix_x, matrix_y, matrix_z)) # Expected value: [[-2, -7], [-5, -2]]

def matrix_transpose(matrix_variable):
    a = []
    b = []
    for row in zip(*matrix_variable):
        for element in row:
            a.append(element)
        b.append(a)
        a = []
    print(b)
    return b
# 실행결과
matrix_w = [[2, 5], [1, 1], [2, 2]]
matrix_transpose(matrix_w)

