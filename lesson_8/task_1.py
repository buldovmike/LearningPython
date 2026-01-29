n = int(input("Введите кол-во чисел "))
numbers = []

# считываем N чисел
for _ in range(n):
    num = int(input("Введите число "))
    numbers.append(num)

# переворачиваем массив и выводим числа через перевод строки
for num in reversed(numbers):
    print(num)