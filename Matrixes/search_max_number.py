import random

def get_matrix_size():
    size = int(input('Enter the size of the square matrix: '))
    return size

def find_max_in_diagonals(matrix):
    n = len(matrix)
    max_main_diagonal = float('-inf')
    max_secondary_diagonal = float('-inf')

    for i in range(n):
        if matrix[i][i] > max_main_diagonal:
            max_main_diagonal = matrix[i][i]
        
        if matrix[i][n - 1 - i] > max_secondary_diagonal:
            max_secondary_diagonal = matrix[i][n - 1 - i]

    return max_main_diagonal, max_secondary_diagonal

def print_matrix(matrix):
    for row in matrix:
        print('\t'.join(map(str, row)))
    print()

def main():
    size = get_matrix_size()
    matrix = [[random.randint(0, 9) for _ in range(size)] for _ in range(size)]

    print("Original matrix:")
    print_matrix(matrix)

    max_main, max_secondary = find_max_in_diagonals(matrix)

    print(f"Max in main diagonal: {max_main}")
    print(f"Max in secondary diagonal: {max_secondary}")

if __name__ == "__main__":
    main()
