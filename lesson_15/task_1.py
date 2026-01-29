class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


# Создаём класс-наследник Autobus, который наследует от Transport
class Autobus(Transport):
    # Можно оставить пустым — все методы и атрибуты уже унаследованы
    pass

# Создаём объект Autobus
autobus = Autobus("Renaul Logan", 180, 12)


# Выводим требуемую информацию
print(f"Название автомобиля: {autobus.name} Скорость: {autobus.max_speed} Пробег: {autobus.mileage}")