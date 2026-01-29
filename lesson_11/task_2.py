# Инициализация словаря с питомцами
pets = {
    1: {
        "Мухтар": {
            "Вид питомца": "Собака",
            "Возраст питомца": 9,
            "Имя владельца": "Павел"
        }
    },
    2: {
        "Каа": {
            "Вид питомца": "желторотый питон",
            "Возраст питомца": 19,
            "Имя владельца": "Саша"
        }
    }
}

#Возвращает информацию о питомце по ID или False, если питомца нет
def get_pet(ID):
    return pets[ID] if ID in pets.keys() else False

#Определяет правильное окончание для слова «год» в зависимости от возраста
def get_suffix(age):
    if 10 <= age % 100 <= 20:
        return "лет"
    elif age % 10 == 1:
        return "год"
    elif 2 <= age % 10 <= 4:
        return "года"
    else:
        return "лет"

#Выводит список всех питомцев в удобном формате
def pets_list():
    if not pets:
        print("В базе нет ни одного питомца.")
        return
    
    print("\n=== Список всех питомцев ===")
    for pet_id, pet_info in pets.items():
        for name, data in pet_info.items():
            species = data["Вид питомца"]
            age = data["Возраст питомца"]
            owner = data["Имя владельца"]
            suffix = get_suffix(age)
            print(f"[ID: {pet_id}] Это {species} по кличке \"{name}\". Возраст питомца: {age} {suffix}. Имя владельца: {owner}")

#Добавляет нового питомца в словарь pets
def create():
    # Получаем последний ID без collections
    if pets:
        last_id = max(pets.keys())  # берём максимальный ключ — это последний ID
        new_id = last_id + 1
    else:
        new_id = 1

    name = input("Введите кличку питомца: ").strip()
    if not name:
        print("Кличка питомца не может быть пустой!")
        return

    species = input("Введите вид питомца: ").strip()
    if not species:
        print("Вид питомца не может быть пустым!")
        return

    while True:
        age_input = input("Введите возраст питомца (целое число): ").strip()
        if not age_input.isdigit():
            print("Пожалуйста, введите корректное целое положительное число!")
            continue
        age = int(age_input)
        if age < 0:
            print("Возраст не может быть отрицательным!")
            continue
        break

    owner = input("Введите имя владельца: ").strip()
    if not owner:
        print("Имя владельца не может быть пустым!")
        return

    # Добавляем нового питомца
    pets[new_id] = {
        name: {
            "Вид питомца": species,
            "Возраст питомца": age,
            "Имя владельца": owner
        }
    }
    print(f"Питомец {name} успешно добавлен с ID {new_id}!\n")

#Выводит информацию о питомце по указанному ID
def read():
    pet_id_input = input("Введите ID питомца, информацию о котором хотите посмотреть: ").strip()
    
    if not pet_id_input.isdigit():
        print("ID должен быть целым числом!")
        return
    
    pet_id = int(pet_id_input)
    pet = get_pet(pet_id)
    
    if not pet:
        print(f"Питомец с ID {pet_id} не найден!")
        return
    
    # Извлекаем данные
    for name, data in pet.items():
        species = data["Вид питомца"]
        age = data["Возраст питомца"]
        owner = data["Имя владельца"]
        suffix = get_suffix(age)
        print(f"Это {species} по кличке \"{name}\". Возраст питомца: {age} {suffix}. Имя владельца: {owner}")

#Обновляет информацию о питомце с указанным ID
def update():
    pet_id_input = input("Введите ID питомца, которого хотите обновить: ").strip()
    
    if not pet_id_input.isdigit():
        print("ID должен быть целым числом!")
        return
    
    pet_id = int(pet_id_input)
    pet = get_pet(pet_id)
    
    if not pet:
        print(f"Питомец с ID {pet_id} не найден!")
        return
    
    # Извлекаем текущее имя питомца
    current_name = list(pet.keys())[0]
    current_data = pet[current_name]
    
    print(f"Текущие данные питомца {current_name}:")
    print(f"Вид: {current_data['Вид питомца']}")
    print(f"Возраст: {current_data['Возраст питомца']}")
    print(f"Владелец: {current_data['Имя владельца']}")
    
    # Запрашиваем новые данные
    new_name = input(f"Введите новую кличку (или оставьте как есть — {current_name}): ").strip()
    if not new_name:
        new_name = current_name

    new_species = input(f"Введите новый вид (или оставьте как есть — {current_data['Вид питомца']}): ").strip()
    if not new_species:
        new_species = current_data["Вид питомца"]

    while True:
        age_input = input(f"Введите новый возраст (или оставьте как есть — {current_data['Возраст питомца']}): ").strip()
        if not age_input:
            new_age = current_data["Возраст питомца"]
            break
        if not age_input.isdigit():
            print("Пожалуйста, введите корректное целое положительное число!")
            continue
        new_age = int(age_input)
        if new_age < 0:
            print("Возраст не может быть отрицательным!")
            continue
        break

    new_owner = input(f"Введите новое имя владельца (или оставьте как есть — {current_data['Имя владельца']}): ").strip()
    if not new_owner:
        new_owner = current_data["Имя владельца"]
    
    # Обновляем запись
    pets[pet_id] = {
        new_name: {
            "Вид питомца": new_species,
            "Возраст питомца": new_age,
            "Имя владельца": new_owner
        }
    }
    print(f"Информация о питомце {new_name} (ID: {pet_id}) успешно обновлена!\n")

#Удаляет питомца с указанным ID
def delete():
    pet_id_input = input("Введите ID питомца, которого хотите удалить: ").strip()
    
    if not pet_id_input.isdigit():
        print("ID должен быть целым числом!")
        return
    
    pet_id = int(pet_id_input)
    pet = get_pet(pet_id)
    
    if not pet:
        print(f"Питомец с ID {pet_id} не найден!")
        return
    
    # Извлекаем имя питомца для вывода
    pet_name = list(pet.keys())[0]
    del pets[pet_id]
    print(f"Питомец {pet_name} (ID: {pet_id}) успешно удалён!\n")

# Основной цикл программы
def main():
    while True:
        print("\nВыберите действие:")
        print("1. Добавить питомца (create)")
        print("2. Посмотреть информацию о питомце (read)")
        print("3. Обновить информацию о питомце (update)")
        print("4. Удалить питомца (delete)")
        print("5. Показать список всех питомцев")
        print("6. Выход (stop)")
        
        command = input("Ваш выбор (1-6 или stop): ").strip().lower()
        
        if command == "stop" or command == "6":
            print("До свидания!")
            break
        elif command == "1":
            create()
        elif command == "2":
            read()
        elif command == "3":
            update()
        elif command == "4":
            delete()
        elif command == "5":
            pets_list()
        else:
            print("Некорректный выбор. Пожалуйста, введите 1, 2, 3, 4, 5")