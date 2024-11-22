from random import randint

def bubble_sort(numbers):
    for i in range(len(numbers) - 1):
        for j in range(len(numbers) - 1, i, -1):
            if numbers[j - 1] > numbers[j]:
                temp = numbers[j - 1]
                numbers[j - 1] = numbers[j]
                numbers[j] = temp

list_ = [randint(1, 100) for _ in range(30)]

count = 0
for i in range(1, len(list_) - 1):
    if list_[i] > list_[i - 1] and list_[i] > list_[i + 1]:
        count += 1

print("Количество элементов, которые больше своих соседей в неотсортированном списке:", count)

bubble_sort(list_)

unique_numbers = sorted(set(list_), reverse=True)

if len(unique_numbers) >= 3:
    print("Второе по величине число:", unique_numbers[1])
    print("Индекс третьего по величине числа:", list_.index(unique_numbers[2]))
else:
    print("Недостаточно уникальных чисел для определения второго и третьего по величине.")
