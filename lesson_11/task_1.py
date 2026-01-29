#Вычисляет факториал натурального числа n
def factorial(n):
    if n < 0:
        print("Ошибка: факториал определен только для неотрицательных чисел.")
        return None
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

#Принимает натуральное число, вычисляет его факториал,
#затем формирует список факториалов от этого значения до 1 в убывающем порядке
def get_factorial_sequence(start_num):
    """
    Принимает натуральное число, вычисляет его факториал,
    затем формирует список факториалов от этого значения до 1 в убывающем порядке.
    
    Args:
        start_num (int): Натуральное число
        
    Returns:
        list or None: Список факториалов в убывающем порядке или None при ошибке
    """
    # Шаг 1: Находим факториал входного числа
    initial_factorial = factorial(start_num)
    
    # Если factorial вернул None (ошибка), прерываем выполнение
    if initial_factorial is None:
        return None
    
    # Шаг 2: Создаем список факториалов от initial_factorial до 1
    result_list = []
    for num in range(initial_factorial, 0, -1):
        fact = factorial(num)
        # Если факториал не удалось вычислить (маловероятно, но на всякий случай)
        if fact is None:
            return None
        result_list.append(fact)
    
    return result_list

# Пример использования
if __name__ == "__main__":
    input_number = 3
    
    result = get_factorial_sequence(input_number)
    
    if result is not None:
        print(f"Входное число: {input_number}")
        print(f"Факториал числа {input_number}: {factorial(input_number)}")
        print(f"Список факториалов от {factorial(input_number)} до 1: {result}")
    else:
        print("Не удалось вычислить результат из‑за ошибки ввода.")