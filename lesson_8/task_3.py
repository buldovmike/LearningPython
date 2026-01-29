# Чтение и проверка m
try:
    m = int(input())
    if not (1 <= m <= 10**6):
        print("Ошибка: m должно быть от 1 до 1 000 000")
        exit()
except ValueError:
    print("Ошибка: m должно быть целым числом")
    exit()

# Чтение и проверка n
try:
    n = int(input())
    if not (1 <= n <= 100):
        print("Ошибка: n должно быть от 1 до 100")
        exit()
except ValueError:
    print("Ошибка: n должно быть целым числом")
    exit()

weights = []

# Чтение весов рыбаков с проверкой
for i in range(n):
    try:
        ai = int(input())
        if not (1 <= ai <= m):
            print(f"Ошибка: вес рыбака #{i+1} должен быть от 1 до {m}")
            exit()
        weights.append(ai)
    except ValueError:
        print(f"Ошибка: вес рыбака #{i+1} должен быть целым числом")
        exit()

# Алгоритм: сортировка и два указателя
weights.sort()
boats = 0
left = 0
right = n - 1

while left <= right:
    if weights[left] + weights[right] <= m:
        left += 1  # берём лёгкого
    right -= 1  # всегда берём тяжёлого
    boats += 1

print(boats)