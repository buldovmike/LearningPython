class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"Вместимость одного автобуса {self.name}: {capacity} пассажиров"

class Autobus(Transport):
    #Переопределённый метод, устанавливающий значение capacity по умолчанию равным 50
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)

# Создаём объект Autobus
autobus = Autobus("Renaul Logan", 180, 12)

# Вызываем переопределённый метод (без указания capacity — используется значение по умолчанию)
print(autobus.seating_capacity())
