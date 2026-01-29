import random

#Создаёт матрицу заданной размерности со случайными значениями
def generate_matrix(rows, cols, min_val=0, max_val=10):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(random.randint(min_val, max_val))
        matrix.append(row)
    return matrix

#Выводит матрицу на экран с заголовком
def print_matrix(matrix, name="Матрица"):
    print(f"{name}:")
    for row in matrix:
        print(row)
    print()  # пустая строка для разделения

#Складывает две матрицы одинаковой размерности
def add_matrices(matrix1, matrix2): 
    # Проверяем, что матрицы имеют одинаковую размерность
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("Ошибка: матрицы имеют разную размерность, сложение невозможно!")
        return None
    
    # Создаём результирующую матрицу
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    
    return result

def main():
    print("Программа для работы с матрицами\n")
    
    # Пример для матриц 10x10
    print("Пример 1: матрицы 10×10")
    matrix_a = generate_matrix(10, 10, 1, 50)
    matrix_b = generate_matrix(10, 10, 1, 50)
    
    print_matrix(matrix_a, "Матрица A (10×10)")
    print_matrix(matrix_b, "Матрица B (10×10)")
    
    matrix_c = add_matrices(matrix_a, matrix_b)
    if matrix_c is not None:
        print_matrix(matrix_c, "Сумма матриц A + B (10×10)")
    
    # Пример для матриц 4x3
    print("Пример 2: матрицы 4×3")
    matrix_x = generate_matrix(4, 3, 1, 20)
    matrix_y = generate_matrix(4, 3, 1, 20)
    
    print_matrix(matrix_x, "Матрица X (4×3)")
    print_matrix(matrix_y, "Матрица Y (4×3)")
    
    matrix_z = add_matrices(matrix_x, matrix_y)
    if matrix_z is not None:
        print_matrix(matrix_z, "Сумма матриц X + Y (4×3)")

if __name__ == "__main__":
    main()