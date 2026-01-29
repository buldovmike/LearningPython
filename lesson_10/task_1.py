pets = {}

while True:
    print("\nВыберите действие:")
    print("1. Добавить питомца")
    print("2. Посмотреть всех питомцев")
    print("3. Выход")
    
    choice = input("Ваш выбор (1-3): ").strip()
    
    if choice == "1":
        # Ввод данных о питомце
        name = input("Введите кличку питомца: ").strip()
        if not name:
            print("Кличка питомца не может быть пустой!")
            continue
        
        species = input("Введите вид питомца: ").strip()
        if not species:
            print("Вид питомца не может быть пустым!")
            continue
        
        age_input = input("Введите возраст питомца (целое число): ").strip()
        # Проверяем, что ввод не пустой и состоит только из цифр
        if not age_input or not age_input.isdigit():
            print("Пожалуйста, введите корректное целое положительное число!")
            continue
        
        age = int(age_input)
        if age < 0:
            print("Возраст не может быть отрицательным!")
            continue
        
        owner = input("Введите имя владельца: ").strip()
        if not owner:
            print("Имя владельца не может быть пустым!")
            continue
        
        # Добавляем питомца в словарь
        pets[name] = {
            "Вид питомца": species,
            "Возраст питомца": age,
            "Имя владельца": owner
        }
        
        print(f"Питомец {name} успешно добавлен!\n")
        
    elif choice == "2":
        # Вывод информации о всех питомцах
        if not pets:
            print("В базе нет ни одного питомца.")
            continue
        
        print("\n=== Информация о питомцах ===")
        for name, info in pets.items():
            species = info["Вид питомца"]
            age = info["Возраст питомца"]
            owner = info["Имя владельца"]
            
            # Определяем правильное окончание для слова "год"
            if 10 <= age % 100 <= 20:
                age_suffix = "лет"
            elif age % 10 == 1:
                age_suffix = "год"
            elif 2 <= age % 10 <= 4:
                age_suffix = "года"
            else:
                age_suffix = "лет"
            
            print(f"Это {species} по кличке \"{name}\". Возраст питомца: {age} {age_suffix}. Имя владельца: {owner}")
            
    elif choice == "3":
        print("До свидания!")
        break
        
    else:
        print("Некорректный выбор. Пожалуйста, введите 1, 2 или 3.")