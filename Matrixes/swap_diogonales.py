import random

def get_matrix_size():
    size = int(input('Enter the size of the square matrix: '))
    return size

def swap_diagonals(matrix):
    n = len(matrix)
    for i in range(n):
        matrix[i][i], matrix[i][n - 1 - i] = matrix[i][n - 1 - i], matrix[i][i]

def print_matrix(matrix):
    for row in matrix:
        print('\t'.join(map(str, row)))  # Используем join для более удобного вывода
    print()

def main():
    size = get_matrix_size()
    
    # Создаем квадратную матрицу с случайными числами
    matrix = [[random.randint(0, 9) for _ in range(size)] for _ in range(size)]

    print("Original matrix:")
    print_matrix(matrix)

    swap_diagonals(matrix)

    print("Matrix after swapping diagonals:")
    print_matrix(matrix)

if __name__ == "__main__":
    main()
