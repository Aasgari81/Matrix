from multiprocessing.sharedctypes import Value
import unittest
def input_checker (input, wanted_class) :
    if not isinstance(input, wanted_class):
        raise TypeError (f'Input is not valid')



class Integer :
    def __init__(self, value):
        input_checker (value, int)
        self.value = value
    
    def str_to_integer (string) :
        string = string.strip()
        string = Integer(int(string))
        return string
    
    def __add__ (self, other) : 
        if not (isinstance(self, Integer) or isinstance(self, float)):
            raise TypeError ("Input must be Integer or float")
        if not (isinstance(other, Integer) or isinstance(other, float) or isinstance(other, Complex)):
            raise TypeError ("Input must be Integer or float")
        if (isinstance(other, Complex) and isinstance(self, Integer)) :
            return Complex (other.real + self.value, other.imaginary)
        if isinstance(self, Integer) and isinstance(other, Integer):
            return self.value + other.value
        if isinstance(self, Integer) and isinstance(other, float):
            return self.value + other
        if isinstance(self, Integer) and isinstance(other, int):
            return self.value + other
    
    def __sub__ (self, other) : 
        if not (isinstance(self, Integer) or isinstance(self, float)):
            raise TypeError ("Input must be Integer or float")
        if not (isinstance(other, Integer) or isinstance(other, float) or isinstance(other, Complex)):
            raise TypeError ("Input must be Integer or float")
        if (isinstance(other, Complex) and isinstance(self, Integer)) :
            return Complex (-(other.real - self.value), -other.imaginary)
        if isinstance(self, Integer) and isinstance(other, Integer):
            return self.value - other.value
        if isinstance(self, Integer) and isinstance(other, float):
            return self.value - other
        if isinstance(self, Integer) and isinstance(other, int):
            return self.value - other
    
    def __mul__ (self, other) :
        if not (isinstance(self, Integer) or isinstance(self, float)):
            raise TypeError ("Input must be Integer or float")
        if not (isinstance(other, Integer) or isinstance(other, float) or isinstance(other, Complex) or isinstance(other, Matrix)):
            raise TypeError ("Input must be Integer or float")
        if isinstance(other, Integer) :
            return other.value * self.value
        if isinstance(other, float) :
            return self.value * other
        if isinstance (other, Complex) :
            return Complex (self.value * other.real, other.imaginary)
        if isinstance (other, Matrix):
            return other * self
        
        

    def __repr__ (self) :
        return f'{self.value}'

    def __str__ (self) :
        return f'{self.value}'



class Complex :
    def __init__(self, real: float, imaginary: float):
        if not (isinstance(real, float) or isinstance(real, int)):
            raise TypeError ("Real part of number must be integer or float")
        if not (isinstance(imaginary, int) or isinstance(imaginary, float)):
            raise TypeError ("Imaginary part of number must be integer or float")    
        self.real = real
        self.imaginary = imaginary
    
    def str_to_coplex (string) :
        string = string.replace(" ", "")
        imaginary, real = string.strip().split(sep = "+")
        is_imaginary = False
        for letter in imaginary :
            if letter == "i" :
                is_imaginary = True
                imaginary = imaginary.replace("i", '')
        if not is_imaginary :
            imaginary, real = real, imaginary
            imaginary = imaginary.replace("i", '')
        imaginary, real = int(imaginary), int(real)
        return Complex(real, imaginary)


    def __add__ (self, other) :
        if not (isinstance(self, Complex) or isinstance(self, Integer) or isinstance(self, float)):
            raise ValueError("Input must be int or float or complex")
        if not (isinstance(other, Complex) or isinstance(other, Integer) or isinstance(other, float)):
            raise ValueError("Input must be int or float or complex")
        if isinstance(self, Complex) and isinstance(other, Complex):
            return Complex (self.real + other.real, self.imaginary + other.imaginary)
        if (isinstance(self, Complex) and isinstance(other, Integer)) or (isinstance(self, Complex) and isinstance(other, float)) :
            return Complex(Integer(self.real) + other, self.imaginary)


    def __sub__ (self, other) :
        if not (isinstance(self, Complex) or isinstance(self, Integer) or isinstance(self, float)):
            raise ValueError("Input must be int or float or complex")
        if not (isinstance(other, Complex) or isinstance(other, Integer) or isinstance(other, float)):
            raise ValueError("Input must be int or float or complex")
        if isinstance(self, Complex) and isinstance(other, Complex):
            return Complex (self.real - other.real, self.imaginary - other.imaginary)
        if (isinstance(self, Complex) and isinstance(other, Integer)) or (isinstance(self, Complex) and isinstance(other, float)) :
            return Complex(Integer(self.real) - other, self.imaginary)
    
    def __mul__ (self, other) :
        if not (isinstance(self, Complex) or isinstance(self, Integer) or isinstance(self, float)):
            raise ValueError("Input must be int or float or complex")
        if not (isinstance(other, Complex) or isinstance(other, Integer) or isinstance(other, float) or isinstance(other, Matrix)):
            raise ValueError("Input must be int or float or complex")
        if isinstance(other, Complex):
            return Complex(((self.real * other.real) - (self.imaginary * other.imaginary)), ((self.imaginary * other.real) + (self.real * other.imaginary)))
        if isinstance (other, Integer) :
            return other * self
        if isinstance(other, Matrix) :
            return other * self
        if isinstance(other, float) :
            return Complex (self.real * other, self.imaginary)

    def __repr__ (self) :
        return f'{self.imaginary}i + {self.real}'
    
    def __str__ (self):
        return f'{self.imaginary}i + {self.real}'



class Matrix :
    def __init__(self, numbers: list, row: Integer):
        input_checker(numbers, list)
        input_checker(row, Integer)
        for i in numbers:
            if  not (isinstance(i, Integer) or  isinstance(i, complex) or  isinstance(i, float)) :
                raise TypeError ("Elements must be integer or float or comlex")
            else :
                continue
        if not (len(numbers)/ row.value).is_integer():
            raise ValueError ("Invalid Input for row")
        column = Integer(int((len(numbers)) / row.value))
        matrix = []
        for element_of_each_row in range(row.value):
            each_row = []
            for nubmer_of_elements in (0 for i in range(column.value)):
                 each_row.append(numbers[nubmer_of_elements])
                 del numbers[nubmer_of_elements]
            matrix.append(each_row)        
        self.matrix = matrix
        self.column = column
        self.row = row

    def make_unit_matrix (n):
        if n <= 0 :
            raise ValueError ("Invalid Input")
        matrix = []
        for rows in range(n):
            row = []
            for column in range(n):
                if rows == column :
                    row.append(1)
                elif rows != column :
                    row.append(0)
            matrix.append(row)
        return matrix
    

    def get_ith_row (matrix, i:int):
        if i < 1 :
            raise ValueError ("Invalid Input For Row")
        if not bool(matrix) :
            raise ValueError ("Invalid Input For Matrix it should not be empty")
        len_of_each_row = len(matrix[0])
        for row in matrix :
            if len(row) != len_of_each_row:
                raise ValueError ("Invalid Input for matrix (The rows Does't have same length)")
        return matrix[i-1]
    

    def get_ith_col (matrix, i: int):
        if i < 1 :
            raise ValueError ("Invalid Input For Row")
        if not bool(matrix) :
            raise ValueError ("Invalid Input For Matrix it should not be empty")
        len_of_each_row = len(matrix[0])
        for row in matrix :
            if len(row) != len_of_each_row:
                raise ValueError ("Invalid Input for matrix (The rows Does't have same length)")
        col = []
        for m in matrix:
            col.append(m[i-1])
        return col

    def is_zero_matrix (matrix) :
        result = True
        for row in matrix :
            for element in row :
                if element != 0 :
                    result = False
        return result
    
    def is_unit_matrix (matrix) :
        n = 0
        result = True

        for rows in matrix :
            for column in range(len(rows)) :
                if column == n :
                    if rows[column] != 1 :
                        result = False
                else :
                    if rows[column] != 0:
                        result = False
            n += 1
        return result
    
    def is_top_triangle_matrix (matrix):
        i = 0
        result = True
        for row in matrix :
            for column in range(len(row)) :
                if column < i :
                    if row [column] != 0 :
                        result = False
            i += 1
        return result
    
    def is_bottom_triangle_matrix (matrix):
        i = 0
        result = True
        for row in matrix :
            for column in range(len(row)) :
                if column > i :
                    if row [column] != 0 :
                        result = False
            i += 1
        return result
    
    def make_matrix_from_string (string):
        string = string.strip()
        matrix = list(string.split(sep = ","))
        final_matrix = []
        for rows in matrix:
            row = []
            for element in rows.split(sep = " "):
                if element.isinteger() :
                    element = Integer.str_to_integer(element)
                else :
                    for letter in element :
                        if letter == "i" :
                            element = Complex.str_to_coplex(element)
                row.append(element)
            final_matrix.append(row)
        return final_matrix

    def __add__ (self, other):
        input_checker(self, Matrix)
        input_checker(other, Matrix)
        if len(self.matrix) != len(other.matrix):
            raise ValueError("Two matrixes must have same rows")
        if len(self.matrix[0]) != len(other.matrix[0]) :
            raise ValueError ('Two matrixes must have same columns')
        result = []
        for rows in zip(self.matrix, other.matrix) :
            row = []
            first, second = rows
            row = [first[i] + second[i] for i in range(len(first))]
            result.append(row)
        return result
    
    def __mul__ (self, other) :
        if not (isinstance(other, Integer) or isinstance(other, float) or isinstance(other, Complex)):
            if self.column.value != other.row.value : 
                raise ValueError ("The number of first matrix column must be equal with the number of the row of second one")
        result_matrix = []
        if isinstance(other, Matrix):
            cols = []
            for column in range(other.column.value):
                cols.append(Matrix.get_ith_col(other.matrix, column + 1 ))
            for row in self.matrix :
                each_row = []
                for column in cols :
                    elements = []
                    for element1, element2 in zip(row, column) :
                        elements.append(element1 * element2)
                    each_row.append(sum(elements))
                result_matrix.append(each_row)
            return result_matrix
              
        if isinstance(other, Integer) or isinstance(other, float) or isinstance(other, Complex) :
            each_row = []
            for row in self.matrix :
                each_row = [i*other for i in row]
                result_matrix.append(each_row)
            return result_matrix
    
    def __sub__ (self, other):
        input_checker(self, Matrix)
        input_checker(other, Matrix)
        if len(self.matrix) != len(other.matrix):
            raise ValueError("Two matrixes must have same rows")
        if len(self.matrix[0]) != len(other.matrix[0]) :
            raise ValueError ('Two matrixes must have same columns')
        result = []
        for rows in zip(self.matrix, other.matrix) :
            row = []
            first, second = rows
            row = [first[i] - second[i] for i in range(len(first))]
            result.append(row)
        return result
    
    def __repr__ (self) : 
        return f'{self.matrix}'
    def __str__ (self) :
        return f'{self.matrix}'



def Multiply (first_input, second_input) :
    if isinstance(first_input, float) :
        return second_input * first_input

    else :
        return first_input * second_input



def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

class Testclass(unittest.TestCase):
    def test_creating_Integer1 (self) :
        i = Integer(5)
        self.assertEqual(i.value, 5)
    
    def test_creating_Integer2 (self) :
        with self.assertRaises(TypeError) :
            i = Integer ([51,6])

    def test_creating_INteger2 (self) : 
        with self.assertRaises(TypeError):
            i = Integer(2.5)
    
    def test_str_to_Integer1 (self) :
        m = Integer.str_to_integer(" 5 ")
        self.assertEqual(m.value, 5)

    def test_str_to_Integer1 (self) :
        m = Integer.str_to_integer("   56516  ")
        self.assertEqual(m.value, 56516)

    def test_adding_two_INteger (self):
        m = Integer(9)
        s = Integer (8)
        self.assertEqual(m + s, 17)
    
    def test_adding_INteger_and_Complex (self) :
        m = Integer(5)
        c = Complex(5, 2)
        self.assertEqual(str(m + c), '2i + 10')
    
    def test_adding_INteger_and_float (self):
        m = 2.4
        s = Integer(23)
        self.assertEqual (s + m, 25.4)
    
    def test_substracting_two_INtegers (self) :
        m = Integer(52)
        s = Integer(27)
        self.assertEqual(m - s, 25)
    
    def test_subtracting_INteger_Complex (self) :
        m = Integer (32)
        s = Complex (5, 2)
        self.assertEqual(str(m - s), '-2i + 27')
    
    def test_subtracting_Integer_and_Complex (self) :
        m = Integer(36)
        f = Complex (32, 5)
        self.assertEqual(str(m - f), '-5i + 4')
        
    def test_subtracting_Integer_and_float (self) :
        m = Integer (12)
        s = 2.5
        self.assertEqual(m - s, 9.5)
    
    def test_multiplying_two_Integers (self) :
        k = Integer(25)
        m = Integer (6)
        self.assertEqual(m * k, 150)
        self.assertEqual(k * m, 150)
    
    def test_multiplying_Integer_and_complex (self) : 
        k = Integer(2)
        s = Complex (3, 2)
        self.assertEqual(str(k * s), '2i + 6')
    
    def test_multiplying_Integer_and_Float (self) :
        k = Integer (3)
        j = 2.4
        self.assertEqual(k * j, 7.199999999999999)
    
    def test_creating_Complex_object (self) :
        m = Complex(5, 6)
        self.assertEqual(str(m), '6i + 5')
        self.assertEqual(m.imaginary, 6)
        self.assertEqual(m.real, 5)
    
    def test_creating_complex_object (self) :
        with self.assertRaises(TypeError) :
            m = Complex("61", "65")

    def test_string_to_complex (self) :
        m = Complex.str_to_coplex("2i+5")
        k = Complex.str_to_coplex("5+2i")
        j = Complex.str_to_coplex("2 i + 6" )
        self.assertEqual(str(m), '2i + 5')
        self.assertEqual(str(k), '2i + 5')
        self.assertEqual(str(j), '2i + 6')
    
    def test_adding_complex_with_Integer_and_float (self) : 
        m = Complex (4, 2)
        g = Integer(5)
        k = 5.2
        self.assertEqual(str(m + g), '2i + 9')
        self.assertEqual(str(m + k), "2i + 9.2")
    
    def test_subtracting_Comlpex_with_complex_and_Integer_and_float (self) :
        m = Complex (23, 10)
        q = Complex (13, 5)
        k = Integer(5)
        s = 5.5
        self.assertEqual(str(m - k), '10i + 18')
        self.assertEqual(str (m - s), '10i + 17.5')
        self.assertEqual (str(m - q), '5i + 10')
    
    def test_multiplying_complex_and_complex_and_Integer_and_float (self) :
        m = Complex (23, 10)
        q = Complex (13, 5)
        k = Integer(5)
        s = 5.5
        self.assertEqual (str (m * q), '245i + 249')
        self.assertEqual (str(m * k), '10i + 115')
        self.assertEqual (str(m * s), '10i + 126.5')
    
    def test_creating_Matrix1 (self) :
        with self.assertRaises(TypeError) :
            m = Matrix  (["m", 2, 6], Integer(2))
    
    def test_creating_Matrix2 (self) :
        with self.assertRaises(ValueError) :
            m = Matrix ([Integer(1),Integer(2),Integer(3),Integer(4)], Integer(5) )
    
    def test_creating_Maatrix3 (self) :
        m = Matrix ([Integer(2), Integer(30), Integer(40), Integer(10), Integer(15), Integer(12)], Integer(3))
        self.assertEqual(str(m.column), '2')
        self.assertEqual(str(m.row), '3')
    
    def test_make_unit_matrix1 (self) :
        f = Matrix.make_unit_matrix(5)
        self.assertEqual(f, [[1,0,0,0,0], [0,1,0,0,0], [0,0,1,0,0], [0,0,0,1,0], [0,0,0,0,1]])
    
    def test_make_unit_matrix2 (self) :
        with self.assertRaises(ValueError) :
            f = Matrix.make_unit_matrix (0)
    
    def test_make_unit_matrix2 (self) :
        with self.assertRaises(ValueError) :
            f = Matrix.make_unit_matrix (-2)
    
    def test_get_ith_row1 (self) :
        with self.assertRaises(ValueError) :
            f = Matrix.get_ith_row([], 1)
    
    def test_get_ith_row2 (self) :
        with self.assertRaises (ValueError) :
            f = Matrix.get_ith_col([[1,2], [3]], 1)
    
    def test_get_ith_row (self) :
        f = Matrix.get_ith_row([[1,2], [3,4], [5,6], [7,8]], 2)
        self.assertEqual(f, [3,4])
    
    def test_get_ith_col1 (self) :
        with self.assertRaises(ValueError) :
            f = Matrix.get_ith_col([], 1)
    
    def test_get_ith_col2 (self) :
        with self.assertRaises (ValueError) :
            f = Matrix.get_ith_col([[1,2], [3]], 1)
    
    def test_get_ith_col (self) :
        f = Matrix.get_ith_col([[1,2], [3,4], [5,6], [7,8]], 2)
        self.assertEqual(f, [2,4,6,8])
    
    def test_is_zero_matrix (self) :
        f = Matrix.is_zero_matrix([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
        self.assertEqual(f, True)
    
    def test_is_zero_matrix1 (self) :
        f = Matrix.is_zero_matrix([[0,0,1,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
        self.assertEqual(f, False)
    
    def test_is_unit_matrix3 (self) :
        f = Matrix.is_unit_matrix([[1,0,0],[0,1,0],[0,0,1]])
        self.assertEqual(f, True)
    
    def test_is_unit_matrix2 (self) :
        f = Matrix.is_unit_matrix([[1,1,0],[0,1,0],[0,0,1]])
        self.assertEqual(f, False)
    
    def test_is_unit_matrix1 (self) :
        f = Matrix.is_unit_matrix([[3,0,0],[0,3,0],[0,0,3]])
        self.assertEqual(f, False)
    
    def test_is_top_triangle (self) :
        f = Matrix.is_top_triangle_matrix([[1,2,3],[0,2,3], [0,0,8]])
        self.assertEqual(f, True)
    
    def test_is_top_triangle1 (self) :
        f = Matrix.is_top_triangle_matrix([[1,2,3],[0,2,3], [0,2,8]])
        self.assertEqual(f, False)
    
    def test_is_bottom_triangle (self) :
        f = Matrix.is_bottom_triangle_matrix ([[1,2,3],[0,2,3], [0,2,8]])
        self.assertEqual(False, f)
    
    def test_is_bottom_triangle2 (self) :
        f = Matrix.is_bottom_triangle_matrix([[2,0,0], [1,2,0], [1,2,3]])
        self.assertEqual(f, True)

    def test_adding_two_matrix (self) :
        f = Matrix ([Integer(3),Integer(2),Integer(1),Integer(3),Integer(4),Integer(5),Integer(7),Integer(8),Integer(9)], Integer (3))
        s = Matrix ([Integer(4),Integer(5),Integer(6),Integer(7),Integer(2),Integer(3),Integer(1),Integer(19),Integer(20)],  Integer(3))
        self.assertEqual(f + s, [[7,7,7], [10,6,8], [8,27,29]])
    
    def test_adding_two_matrix2 (self) :
        f = Matrix([Integer(1),Integer(2),Integer(3),Integer(4),Integer(5),Integer(6),Integer(7),Integer(8)], Integer(4))
        s = Matrix([Integer(2),Integer(3),Integer(4),Integer(5),Integer(6),Integer(8),Integer(1),Integer(2)], Integer(2))
        with self.assertRaises(ValueError) :
            f + s
    def test_subtracting_two_matrix1 (self) :
        f = Matrix([Integer(1),Integer(2),Integer(3),Integer(4),Integer(5),Integer(6),Integer(7),Integer(8)], Integer(4))
        s = Matrix([Integer(2),Integer(3),Integer(4),Integer(5),Integer(6),Integer(8),Integer(1),Integer(2)], Integer(2))
        with self.assertRaises(ValueError) :
            f + s
    
    def test_subtrscting_two_matrix2 (self) :
        f = Matrix ([Integer(3),Integer(2),Integer(1),Integer(3),Integer(4),Integer(5),Integer(7),Integer(8),Integer(9)], Integer (3))
        s = Matrix ([Integer(4),Integer(5),Integer(6),Integer(7),Integer(2),Integer(3),Integer(1),Integer(19),Integer(20)],  Integer(3))
        self.assertEqual(f - s, [[-1,-3,-5], [-4,2,2], [6,-11,-11]])
    
    def test_multiplying_two_matrixes (self) :
        f = Matrix([Integer(2),Integer(4),Integer(8),Integer(3),Integer(2),Integer(5),Integer(4),Integer(3),Integer(3)], Integer(3))
        s = Matrix([Integer(7),Integer(6),Integer(2),Integer(1),Integer(3),Integer(1),Integer(5),Integer(4),Integer(2)], Integer(3))
        self.assertEqual(f*s, [[58,56,24],[48,44,18],[46,45,17]])
        
    def test_multiplying_two_matrixes1 (self) :
        f = Matrix([Integer(2),Integer(4),Integer(8),Integer(3),Integer(2),Integer(5),Integer(4),Integer(3),Integer(3)], Integer(3))
        s = Matrix([Integer(7),Integer(3),Integer(1),Integer(5),Integer(4),Integer(2)], Integer(3))
        with self.assertRaises(ValueError) :
            s * f
    
run_tests(Testclass)