import random


def get_matrix_size():
    size = int(input('Enter the size of the square matrix: '))
    return size


def find_min_in_diagonals(matrix):
    n = len(matrix)
    min_main_diagonal = float('inf')  # Инициализируем максимально возможным значением
    min_secondary_diagonal = float('inf')  # Инициализируем максимально возможным значением

    for i in range(n):
        # Проверяем элементы главной диагонали
        if matrix[i][i] < min_main_diagonal:
            min_main_diagonal = matrix[i][i]

        # Проверяем элементы побочной диагонали
        if matrix[i][n - 1 - i] < min_secondary_diagonal:
            min_secondary_diagonal = matrix[i][n - 1 - i]

    return min_main_diagonal, min_secondary_diagonal


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

    min_main, min_secondary = find_min_in_diagonals(matrix)

    print(f"Min in main diagonal: {min_main}")
    print(f"Min in secondary diagonal: {min_secondary}")


if __name__ == "__main__":
    main()
