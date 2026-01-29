#Считываем первый список чисел
first_line = input().strip()
first_list = list(map(int, first_line.split()))

# Считываем второй список чисел
second_line = input().strip()
second_list = list(map(int, second_line.split()))

# Преобразуем списки в множества
first_set = set(first_list)
second_set = set(second_list)

# Находим пересечение множеств (общие элементы)
common_elements = first_set & second_set

# Выводим количество общих элементов
print(len(common_elements))