import random


def create_empty_matrix(size):
    return [['~' for _ in range(size)] for _ in range(size)]


def is_valid_island(matrix, shape):
    for x, y in shape:
        if x < 1 or y < 1 or x >= len(matrix) - 1 or y >= len(matrix) - 1:
            return False
    width = max(x for x, y in shape) - min(x for x, y in shape) + 1
    height = max(y for x, y in shape) - min(y for x, y in shape) + 1
    if width == height:
        return False
    return True


def generate_random_shape(matrix):
    size = len(matrix)
    shape = set()

    start_x = random.randint(2, size - 3)
    start_y = random.randint(2, size - 3)
    shape.add((start_x, start_y))

    # Генерируем случайную форму острова
    while len(shape) < 20:  # Увеличиваем до 20 клеток
        x, y = random.choice(list(shape))
        direction = random.choice([(0, 1), (1, 0), (0, -1), (-1, 0)])
        new_x = x + direction[0]
        new_y = y + direction[1]

        if 1 <= new_x < size - 1 and 1 <= new_y < size - 1 and (new_x, new_y) not in shape:
            shape.add((new_x, new_y))

    return shape


def fill_island(matrix, shape):
    height_map = {}
    for idx, (x, y) in enumerate(shape):
        # Устанавливаем высоту от 1 до 4 для всех клеток, кроме крайних
        if idx == 0:  # Первая клетка (стартовая) будет иметь высоту 1
            height_map[(x, y)] = 1
        else:
            height_map[(x, y)] = random.randint(1, 4)  # Высота от 1 до 4 для остальных клеток

    for (x, y), height in height_map.items():
        matrix[y][x] = str(height)


def calculate_area_and_perimeter(matrix):
    area = 0
    perimeter = 0
    size = len(matrix)

    for i in range(size):
        for j in range(size):
            if matrix[i][j] not in ['~', ' ']:  # Проверяем только клетки с высотой
                area += 1
                if i == 0 or matrix[i - 1][j] == '~':  # Сверху
                    perimeter += 1
                if i == size - 1 or matrix[i + 1][j] == '~':  # Снизу
                    perimeter += 1
                if j == 0 or matrix[i][j - 1] == '~':  # Слева
                    perimeter += 1
                if j == size - 1 or matrix[i][j + 1] == '~':  # Справа
                    perimeter += 1

    return area, perimeter


def print_matrix(matrix):
    for row in matrix:
        print(' '.join(row))  # Добавляем пробелы между символами


def main():
    size = 20
    matrix = create_empty_matrix(size)

    while True:
        shape = generate_random_shape(matrix)
        if is_valid_island(matrix, shape):
            fill_island(matrix, shape)
            break
        else:
            print("Generated shape is invalid, generating a new one.")

    print("Generated island matrix:")
    print_matrix(matrix)

    area, perimeter = calculate_area_and_perimeter(matrix)
    print(f"Area of the island: {area} km²")
    print(f"Perimeter of the island: {perimeter} km")


if __name__ == "__main__":
    main()
