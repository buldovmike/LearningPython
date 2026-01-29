# Чтение N
n = int(input())

# Проверка диапазона N
if n < 1 or n > 100000:
    print("Ошибка: N должно быть от 1 до 100000")
else:
    # Чтение строки с числами
    line = input().strip()
    
    # Проверка, что строка не пустая
    if not line:
        print("Ошибка: не введено ни одного числа")
    else:
        # Разбиение строки и преобразование в числа
        parts = line.split()
        numbers = []
        max_val = 2 * 10**9  # 2 000 000 000
        
        # Проверка количества чисел
        if len(parts) != n:
            print(f"Ошибка: ожидалось {n} чисел, введено {len(parts)}")
        else:
            valid = True
            # Преобразуем строки в числа и проверяем модуль
            for part in parts:
                # Проверка, что строка — корректное целое число
                if not (part.isdigit() or (part[0] == '-' and part[1:].isdigit())):
                    print("Ошибка: введены некорректные данные (ожидаются целые числа)")
                    valid = False
                    break
                
                num = int(part)
                # Проверка модуля числа
                if abs(num) > max_val:
                    print(f"Ошибка: число {num} превышает допустимый модуль 2 000 000 000")
                    valid = False
                    break
                numbers.append(num)
            
            # Если все проверки пройдены — считаем уникальные числа
            if valid:
                unique_count = len(set(numbers))
                print(unique_count)