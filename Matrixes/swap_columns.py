import random

def get_matrix_dimensions():
    width = int(input('Enter the width of matrix: '))
    height = int(input('Enter the height of matrix: '))
    return width, height

def swap_columns(matrix):
    for row in matrix:
        row[0], row[-1] = row[-1], row[0]  # Меняем местами первый и последний элементы в каждой строке

def print_matrix(matrix):
    for row in matrix:
        print('\t'.join(map(str, row)))  # Используем join для более удобного вывода
    print()

def main():
    width, height = get_matrix_dimensions()
    
    # Создаем матрицу с случайными числами
    matrix = [[random.randint(0, 9) for _ in range(width)] for _ in range(height)]

    print("Original matrix:")
    print_matrix(matrix)

    swap_columns(matrix)

    print("Matrix after swapping columns:")
    print_matrix(matrix)

if __name__ == "__main__":
    main()
