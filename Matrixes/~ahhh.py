import math

matrix_size = int(input('Введите размер матрицы: '))

matrix = [[1 for _ in range(matrix_size)] for _ in range(matrix_size)]

def paint_circle_in_matrix(matrix, size=None):
    if size is not None:
        rows = size + 2
        cols = size + 2
    else:
        rows = len(matrix)
        cols = len(matrix[0])
    center_x = cols // 2
    center_y = rows // 2
    radius = min(center_x, center_y) - 1
    for y in range(rows):
        for x in range(cols):
            distance = math.sqrt((x - center_x) ** 2 + (y - center_y) ** 2)
            if distance <= radius:
                matrix[y][x] = 0
    return matrix

for row in paint_circle_in_matrix(matrix, int(input('Введите размер круга: '))):
    print('', *row)